import Foundation

print("Digite o primeiro número:")
if let input1 = readLine(), let number1 = Int(input1) {
    print("Digite o segundo número:")
    if let input2 = readLine(), let number2 = Int(input2) {
        let soma = number1 + number2
        print("A soma é \(soma).")
    } else {
        print("Entrada inválida para o segundo número.")
    }
} else {
    print("Entrada inválida para o primeiro número.")
}
