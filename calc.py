# calculadora.py

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("Calculadora Simples - HaldenPentester")
    print("Operações disponíveis: soma, subtrai, multiplica, divide")
    operacao = input("Escolha a operação: ").strip().lower()
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == "soma":
        print("Resultado:", soma(a, b))
    elif operacao == "subtrai":
        print("Resultado:", subtrai(a, b))
    elif operacao == "multiplica":
        print("Resultado:", multiplica(a, b))
    elif operacao == "divide":
        print("Resultado:", divide(a, b))
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    main()
