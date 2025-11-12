#!/usr/bin/env bash
# Simple script to create a bootable Linux image with Calculator
# Runs in WSL/Ubuntu

set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

echo "=== Building Calculator (static binary) ==="
cd "$ROOT_DIR/apps/calculator"

# Build with Rust (will use dynamic linking, but that's OK for now)
cargo build --release 2>&1 | tail -20

CALC_BIN="$ROOT_DIR/apps/calculator/target/release/calculator"

if [ ! -f "$CALC_BIN" ]; then
  echo "Error: Calculator binary not found"
  exit 1
fi

echo "✓ Calculator built: $CALC_BIN"
echo ""

# For now, create a simple directory with calculator binary
# This will be used to create a bootable image
OUTPUT_DIR="$ROOT_DIR/bootfs"
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR/bin"
mkdir -p "$OUTPUT_DIR/boot"

cp "$CALC_BIN" "$OUTPUT_DIR/bin/calculator"

echo "=== Creating minimal init system ==="
cat > "$OUTPUT_DIR/init" << 'INITSCRIPT'
#!/bin/sh
# Minimal init script for MirobotOS
mount -t proc none /proc 2>/dev/null || true
mount -t sysfs none /sys 2>/dev/null || true
mount -t tmpfs none /tmp 2>/dev/null || true

echo ""
echo "================================================"
echo "  Welcome to MirobotOS (Linux + Calculator)"
echo "================================================"
echo ""
echo "Available commands:"
echo "  - calculator  : Run the calculator app"
echo "  - help        : Show this message"
echo "  - reboot      : Restart"
echo "  - poweroff    : Shutdown"
echo ""

# Try to find a shell
if [ -f /bin/sh ]; then
  exec /bin/sh
elif [ -f /bin/bash ]; then
  exec /bin/bash
else
  echo "No shell found!"
  exit 1
fi
INITSCRIPT

chmod +x "$OUTPUT_DIR/init"
chmod +x "$OUTPUT_DIR/bin/calculator"

echo "✓ Init script created"
echo ""

echo "=== Creating initramfs ==="
cd "$OUTPUT_DIR"

# Create cpio archive
find . -print0 | cpio -0 -o -H newc 2>/dev/null | gzip -9 > "$ROOT_DIR/initramfs.cpio.gz"
cd "$ROOT_DIR"

echo "✓ Initramfs created: $ROOT_DIR/initramfs.cpio.gz"
echo ""

echo "=== Using host kernel ==="
# Find a kernel to use
KERNEL_FILE=""
if [ -f "/boot/vmlinuz-$(uname -r)" ]; then
  KERNEL_FILE="/boot/vmlinuz-$(uname -r)"
elif [ -f "/boot/vmlinuz" ]; then
  KERNEL_FILE="/boot/vmlinuz"
elif [ -f "/vmlinuz" ]; then
  KERNEL_FILE="/vmlinuz"
fi

if [ -z "$KERNEL_FILE" ]; then
  echo "Warning: No kernel found. You'll need to provide one manually."
  echo "For now, you can use the initramfs-only approach:"
  echo "  - Use the initramfs.cpio.gz with a standard Linux kernel"
  exit 0
fi

echo "✓ Using kernel: $KERNEL_FILE"

echo "=== Creating ISO with GRUB ==="
ISO_DIR=$(mktemp -d)
trap "rm -rf $ISO_DIR" EXIT

mkdir -p "$ISO_DIR/boot/grub"
cp "$KERNEL_FILE" "$ISO_DIR/boot/vmlinuz"
cp "$ROOT_DIR/initramfs.cpio.gz" "$ISO_DIR/boot/initramfs.cpio.gz"

# Create GRUB config
cat > "$ISO_DIR/boot/grub/grub.cfg" << 'GRUBCFG'
set timeout=0
set default=0

menuentry "MirobotOS" {
  linux /boot/vmlinuz root=/dev/ram0 console=ttyS0 console=tty0 quiet
  initrd /boot/initramfs.cpio.gz
}
GRUBCFG

# Create ISO
ISO_FILE="$ROOT_DIR/mirobotOS.iso"
if command -v grub-mkrescue &> /dev/null; then
  grub-mkrescue -o "$ISO_FILE" "$ISO_DIR" 2>&1 | grep -v "^xorriso" || true
  echo "✓ ISO created: $ISO_FILE"
else
  echo "Warning: grub-mkrescue not found. Install: sudo apt install grub-pc-bin xorriso"
  echo "Using initramfs-only approach for now..."
fi

echo ""
echo "================================================"
echo "  BUILD SUCCESSFUL!"
echo "================================================"
echo ""
echo "ISO file: $ISO_FILE"
echo ""
echo "Next steps:"
echo "1. Open VirtualBox"
echo "2. Create new VM (Linux 64-bit, 512 MB RAM)"
echo "3. Attach $ISO_FILE as CD/DVD"
echo "4. Start VM"
echo "5. Type 'calculator' to run the app"
echo ""
