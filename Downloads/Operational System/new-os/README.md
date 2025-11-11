# New OS (Rust) skeleton

Este repositório foi resetado: o conteúdo anterior foi movido para `archive_YYYYMMDD_HHMMSS`.

Este directório `new-os/` contém um esqueleto inicial em Rust para começares a desenvolver um sistema operativo ou userspace em Rust.

O esqueleto atual é intencionalmente minimal e serve como ponto de partida:

- `kernel/` — um projecto Rust com um binário de exemplo (`println!(...)`) que podes converter em `no_std` e transformar num kernel propriamente dito seguindo tutoriais.
- `run_qemu.bat` — script Windows com dicas para arrancar em QEMU (requeres builds específicos para kernel e imagem).
- `run_qemu.bat` — script Windows com suporte a QEMU nativo: tenta usar a imagem criada em `new-os/target/...` se existir; caso contrário instrui a usar o script WSL.

Apps / Calculadora

Existe um exemplo simples de app em Rust em `new-os/apps/calculator`. É um binário normal (usa `std`) e pode ser executado no Windows, WSL ou em qualquer sistema compatível com Rust. Para executar na tua máquina Windows:

```powershell
cd "new-os/apps/calculator"
cargo run --release
```

Se quiseres integrar este binário dentro de uma imagem initramfs ou userspace dentro de uma VM, diz-me e eu preparo instruções para empacotar o binário (ex.: compilação estática com musl e criação de initramfs).  

Próximos passos sugeridos

1. Instalar o Rust toolchain (nightly recomendado para OS dev) e `cargo-binutils`/`llvm-tools-preview` se queres gerar imagens de kernel.
2. Seguir um tutorial como "Writing an OS in Rust" (Philipp Oppermann) para converter o binário em `no_std` e criar um bootável.
3. Testar em QEMU usando `run_qemu.bat` (exige gerar imagem/ELF do kernel primeiro).

Notas

- As instruções de build/boot deverão ser adaptadas ao teu ambiente (WSL2 é recomendado no Windows para ferramentas de Linux e QEMU).
- Se quiseres, eu posso automatizar a criação de um kernel `no_std` mínimo e os scripts de build/boot (GRUB / bootloader / Makefile).
