
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: ").upper())
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()
    print("\n")

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

print("1 - Para buscar um item. \
      \n2 - Para excluir um item.")

opcoes = input("O que deseja fazer? ")

if opcoes == "1":
    busca = input("Digite o nome do equipamento que deseja buscar: ").upper()
    for indice in range(0, len(equipamentos)):
        if busca == equipamentos[indice]:
            print("Valor..: ", valores[indice])
            print("Serial.: ", seriais[indice])

elif opcoes == "2":
    excluir = input(
        "Digite o nome do equipamento que deseja excluir: ").upper()
    for indice in range(0, len(equipamentos)):
        if excluir == equipamentos[indice]:
           del equipamentos[indice]
           del valores[indice]
           del seriais[indice]
           del departamentos[indice]
           print("Item exluido com sucesso!")
    

else:
    print("Opção invalida!")
