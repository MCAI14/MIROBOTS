# New OS (Rust) skeleton

Este repositório foi resetado: o conteúdo anterior foi movido para `archive_YYYYMMDD_HHMMSS`.

Este directório `new-os/` contém um esqueleto inicial em Rust para começares a desenvolver um sistema operativo ou userspace em Rust.

O esqueleto atual é intencionalmente minimal e serve como ponto de partida:

- `kernel/` — um projecto Rust com um binário de exemplo (`println!(...)`) que podes converter em `no_std` e transformar num kernel propriamente dito seguindo tutoriais.
- `run_qemu.bat` — script Windows com dicas para arrancar em QEMU (requeres builds específicos para kernel e imagem).

Próximos passos sugeridos

1. Instalar o Rust toolchain (nightly recomendado para OS dev) e `cargo-binutils`/`llvm-tools-preview` se queres gerar imagens de kernel.
2. Seguir um tutorial como "Writing an OS in Rust" (Philipp Oppermann) para converter o binário em `no_std` e criar um bootável.
3. Testar em QEMU usando `run_qemu.bat` (exige gerar imagem/ELF do kernel primeiro).

Notas

- As instruções de build/boot deverão ser adaptadas ao teu ambiente (WSL2 é recomendado no Windows para ferramentas de Linux e QEMU).
- Se quiseres, eu posso automatizar a criação de um kernel `no_std` mínimo e os scripts de build/boot (GRUB / bootloader / Makefile).
