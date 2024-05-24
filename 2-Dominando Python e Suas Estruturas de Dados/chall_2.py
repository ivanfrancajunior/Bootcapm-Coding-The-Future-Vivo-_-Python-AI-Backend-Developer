total_amount_in_bank: float = 0.0
operations_total_limit = 3
amount_limit_value: float = 500


def deposit(amount: float, total: float, limit: int) -> float:
    result = 0.0
    if (limit <= 0):
        print("Valor inválido total de operações: ", limit)

    result = total + amount
    return result


def witdraw(amount: float, total: float, limit: int) -> float:
    if (limit <= 0):
        print("Valor inválido total de operações: ", limit)

    total = total - amount
    return total


def balance(total: float) -> float:
    return total


while True:
    print("Bem-vindo! Seu saldo atual é: ", total_amount_in_bank)
    print("Digite 'DEPOSITO' ou 'SAQUE' ou 'SALDO' ou 'SAIR': ")
    operation = input()

    if operation.upper().strip().strip() == "DEPOSITO":
        print("Digite o valor para depositar: ")
        operation_amount = float(input())

        total_amount_in_bank = deposit(
            operation_amount, total_amount_in_bank, operations_total_limit)

    elif operation.upper().strip() == "SAQUE":
        print("Digite o valor para sacar: ")

        operation_amount = float(input())
        if operation_amount > total_amount_in_bank:
            print("Saldo insuficiente!")
        elif operation_amount > amount_limit_value:
            print("Limite de saque excedido!")

        elif operations_total_limit == 0:
            print("Limite de saques excedido!")
        else:
            total_amount_in_bank = witdraw(
                operation_amount, total_amount_in_bank, operations_total_limit)

            operations_total_limit = operations_total_limit - 1
    elif operation.upper().strip() == "SALDO":
        print(balance(total_amount_in_bank))
    elif operation.upper().strip() == "SAIR":
        break

    else:
        print("Operação inválida!")
