binario = input('Ingrese su número en binario: ').replace(' ', '')


lista_binario = list(binario)
lista_binario = lista_binario[::-1]
num_decimal = 0




for i in range(len(lista_binario)):
    if lista_binario[i] == '1':
        num_decimal = num_decimal + 2**int(i)
        
        

        
        
        
    

print(num_decimal)
    
