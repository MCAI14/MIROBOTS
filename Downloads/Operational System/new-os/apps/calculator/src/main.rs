use std::io::{self, Write};

fn eval_simple(expr: &str) -> Result<f64, &'static str> {
    // Espera expressões simples do tipo: <num> <op> <num>, ex: 2 + 3
    let parts: Vec<&str> = expr.split_whitespace().collect();
    if parts.len() != 3 {
        return Err("Formato inválido — usa: <num> <op> <num>, ex: 2 + 3");
    }
    let a: f64 = parts[0].parse().map_err(|_| "Número inválido (a)")?;
    let op = parts[1];
    let b: f64 = parts[2].parse().map_err(|_| "Número inválido (b)")?;
    match op {
        "+" => Ok(a + b),
        "-" => Ok(a - b),
        "*" | "x" => Ok(a * b),
        "/" => Ok(a / b),
        _ => Err("Operador desconhecido. Usa + - * /")
    }
}

fn print_help() {
    println!("Calculator — modo interativo");
    println!("Exemplos: \t2 + 3\t  10 * 4\t  8 / 2");
    println!("Comandos: help, exit, quit");
}

fn main() {
    println!("Simple Calculator (Rust)");
    print_help();

    let mut input = String::new();
    loop {
        input.clear();
        print!("> ");
        io::stdout().flush().unwrap();
        if io::stdin().read_line(&mut input).is_err() {
            println!("Falha a ler input");
            continue;
        }
        let line = input.trim();
        if line.is_empty() {
            continue;
        }
        match line {
            "exit" | "quit" => break,
            "help" => { print_help(); continue; }
            _ => {}
        }
        match eval_simple(line) {
            Ok(v) => println!("= {}", v),
            Err(e) => println!("Erro: {}", e),
        }
    }
    println!("Saindo...");
}
