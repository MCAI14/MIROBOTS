#![no_std]
#![no_main]

use core::panic::PanicInfo;

use bootloader::{entry_point, BootInfo};

entry_point!(kernel_main);

fn kernel_main(_boot_info: &'static BootInfo) -> ! {
    use x86_64::instructions::hlt;

    // Escreve uma mensagem simples no buffer VGA (texto - modo 80x25)
    let message = b"Hello from the Rust OS (VM)!";
    let vga_buffer = 0xb8000 as *mut u8;
    unsafe {
        for (i, &byte) in message.iter().enumerate() {
            // cada célula de texto tem 2 bytes: char e atributo
            core::ptr::write_volatile(vga_buffer.add(i * 2), byte);
            core::ptr::write_volatile(vga_buffer.add(i * 2 + 1), 0x0f);
        }
    }

    loop {
        hlt();
    }
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
