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
// Este código é um simples calculador que soma dois números inteiros fornecidos pelo usuário.
// Ele lê os números da entrada padrão, converte-os para inteiros e calcula a soma.
// Se a entrada não for válida, ele imprime uma mensagem de erro.
// O código utiliza a função readLine() para ler a entrada do usuário e o operador de coalescência nula (??) para fornecer um valor padrão caso a conversão falhe.
// O resultado da soma é impresso na saída padrão.
// O código é escrito em Swift, uma linguagem de programação desenvolvida pela Apple.
// O código é um exemplo simples de como lidar com entrada e saída em Swift, além de realizar operações matemáticas básicas.
// O código pode ser executado em um ambiente de desenvolvimento Swift, como o Xcode ou o Swift Playgrounds.
// O código é um exemplo básico de como criar um programa interativo em Swift.
// O código pode ser expandido para incluir outras operações matemáticas, como subtração, multiplicação e divisão.
// O código pode ser melhorado para lidar com entradas inválidas de forma mais robusta, como verificar se os números são realmente inteiros antes de tentar convertê-los.
// O código pode ser modificado para permitir que o usuário escolha a operação a ser realizada, em vez de apenas somar.
// O código pode ser adaptado para funcionar com números de ponto flutuante, em vez de apenas inteiros.
// O código pode ser melhorado para incluir tratamento de erros, como capturar exceções durante a conversão de tipos.
// O código pode ser otimizado para evitar a repetição de código, como criar uma função para lidar com a entrada do usuário.
//FIM