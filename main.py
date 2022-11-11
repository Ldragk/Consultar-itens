inventario = []

def entrada (entrada):        
    while entrada == "S" or entrada == "SIM": 
        itens = [input("\nItem: ").upper(),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ").upper()]   
        inventario.append(itens)                     
        entrada = input("\nAdicionar mais itens? ").upper()                     

entrada(input("Adicionar itens? ").upper()) 

for elemento in inventario: 
          
    def elementoUnico (a):
        elemento_0 = elemento[0][0].upper() + elemento[0].strip(elemento[0][0]).lower()
        elemento_3 = elemento[3][0].upper() + elemento[3].strip(elemento[3][0]).lower() 
        unitarios = [
            "Nome.........: ",  elemento_0, 
            "Valor........: ", str(elemento[1]),        
            "Serial.......: ", str(elemento[2]),        
            "Departamento.: ", elemento_3,
            "Novo valor..: ", str(round((elemento[1] * 0.95),2)),
            "Novo valor..: ", str(round((elemento[1] * 0.9),2)),
            "Novo valor..: ", str(round((elemento[1] * 0.85),2)),
            "Novo valor..: ", str(round((elemento[1] * 0.8),2)) 
        ]            
        return print(unitarios[a], unitarios[a + 1])                     
                
    def elementos ():   
        elemento_0 = elemento[0][0].upper() + elemento[0].strip(elemento[0][0]).lower()
        elemento_3 = elemento[3][0].upper() + elemento[3].strip(elemento[3][0]).lower()                             
        print("Nome.........: ", elemento_0)  
        print("Valor........: ", elemento[1])        
        print("Serial.......: ", elemento[2])        
        print("Departamento.: ", elemento_3)      

print("\n")
print("Itens adicionados:")
for elemento in inventario:
    print("\n")
    elementos() 

resposta = "S"
while resposta == "S" or resposta == "SIM": 
    print("\n")
    print("1 - Para adicionar mais itens.\
        \n2 - Para buscar um item. \
        \n3 - Para excluir um item.  \
        \n4 - Para atribuir desconto à um item. \
        \n5 - Para obter informações dos itens. \
        \n6 - Para exibir todo o estoque. \
        \n7 - Para desligar o programa.")
    
    opcoes = int(input("\nO que deseja fazer? "))

    if opcoes == 1:        
         entrada ("S")    
       
    elif opcoes == 2:
        print("\n")
        busca = input("Digite o nome, serial ou departamento do(s) equipamento(s) que deseja buscar: ").upper()   
        for elemento in inventario:         
            if busca == elemento[0] or busca == elemento[3] or busca == str(elemento[2]):
                print("\n")                
                elementos()                             

    elif opcoes == 3:
        print("\n")
        excluir = input("Digite o serial ou nome do(s) equipamento(s) que deseja excluir: ").upper()
        for elemento in inventario: 
            elemento_0 = elemento[0][0].upper() + elemento[0].strip(elemento[0][0]).lower()
            if excluir == str(elemento[2]) or excluir == elemento[0]:
                inventario.remove(elemento)                
                print("\n")
                print("Item " + elemento_0 + " - Exluido!")
                            
    elif opcoes == 4:
        print("\n")
        desconto = input("Digite o nome do item que deseja atribuir desconto: ").upper()   
        for elemento in inventario:      
            if desconto == elemento[0] or desconto == str(elemento[2]): 
                inventario.remove(elemento)  
                print("\n")
                print("Opções: 5% - 10% - 15% - 20%")  
                qnt = str(input("Quanto deseja descontar? "))                
                                         
                if qnt == "5%" or qnt == "5":
                    print("\n")              
                    elementoUnico(0)         
                    print("Valor antigo: ", elemento[1])                  
                    elementoUnico(8)                         
                    elemento[1] = round((elemento[1] * 0.95),2)
                    elemento.append(elemento[1])
                    inventario.append(elemento)    
                    break                
                elif qnt == "10%" or qnt == "10":
                    print("\n")              
                    elementoUnico(0)         
                    print("Valor antigo: ", elemento[1])                
                    elementoUnico(10) 
                    elemento[1] = round((elemento[1] * 0.9),2)
                    elemento.append(elemento[1])
                    inventario.append(elemento)     
                    break               
                elif qnt == "15%" or qnt == "15":
                    print("\n")              
                    elementoUnico(0)         
                    print("Valor antigo: ", elemento[1])
                    elementoUnico(12) 
                    elemento[1] = round((elemento[1] * 0.85),2)
                    elemento.append(elemento[1])
                    inventario.append(elemento)      
                    break              
                elif qnt == "20%" or qnt == "20":
                    print("\n")              
                    elementoUnico(0)         
                    print("Valor antigo: ", elemento[1])
                    elementoUnico(14)
                    elemento[1] = round((elemento[1] * 0.8),2)
                    elemento.append(elemento[1])
                    inventario.append(elemento)   
                    break                 
                else:
                    print("Opção invalida!")
                    qnt = str(input("Quanto deseja descontar? "))                   
                    
    elif opcoes == 5:
        valores=[]
        quantidade=[]
        for elemento in inventario:
            valores.append(elemento[1]) 
            quantidade.append(elemento[0]) 
        if len(valores) > 0:
            print("\n")
            print("O equipamento mais caro custa: R$",max(valores))
            print("O equipamento mais barato custa: R$",min(valores))
            print("A soma do valor de todo o estoque: R$",round(sum(valores),2))
        if len(quantidade) > 0:
            print("A quantidade de itens em estoque: ",len(quantidade))                        
    elif opcoes == 6:
        for elemento in inventario:
            print("\n") 
            elementos()             
    else:
        print("\n")
        print("Programa desligado!")
        print("\n")
        break
        