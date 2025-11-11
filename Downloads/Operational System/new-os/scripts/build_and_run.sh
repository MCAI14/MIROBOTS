#!/usr/bin/env bash
# Script to build the kernel and run it in QEMU (run this inside WSL/Ubuntu)
# Requirements (inside WSL):
#   rustup toolchain install nightly
#   rustup component add rust-src
#   cargo install bootimage --version ^0.10
#   sudo apt install qemu-system-x86
# Usage:
#   chmod +x scripts/build_and_run.sh
#   ./scripts/build_and_run.sh

set -euo pipefail
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

# Ensure nightly and rust-src
rustup toolchain install nightly
rustup default nightly
rustup component add rust-src

# Install bootimage if missing
if ! command -v cargo-bootimage >/dev/null 2>&1; then
  cargo install bootimage --version 0.10.0 || true
fi

# Build a bootable image (uses the local target JSON)
cargo bootimage --target kernel/x86_64-blog_os.json

# Run with QEMU (adjust memory/arguments as needed)
qemu-system-x86_64 -drive format=raw,file=target/x86_64-blog_os/debug/bootimage-kernel.bin -serial stdio -display none
