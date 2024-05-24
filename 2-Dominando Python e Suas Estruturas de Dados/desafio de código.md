
### #1
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

```py
consumo = float(input())
def recomendar_plano(consumo: float) -> str:
    if consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'

    elif consumo > 10 and consumo <= 20:
        return 'Plano Prata Fibra - 100Mbps'

    return 'Plano Premium Fibra - 300Mbps'

print(recomendar_plano(consumo))
```
### #2
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

Entrada
O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

```py
lista_equipamentos = []
for i in range(3):
    item = input()
    if item != '':
        lista_equipamentos.append(item)
print("Lista de Equipamentos:")
for item in lista_equipamentos:
    print(f"- {item}")

```

### #3:

Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

Formato esperado:
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

```py
import re
def validate_numero_telefone(phone_number):
    pattern = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')
    if re.match(pattern, phone_number):
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'
#
phone_number = input()
result = validate_numero_telefone(phone_number)
print(result)

```