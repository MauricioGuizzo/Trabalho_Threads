import threading
import os 
import time

programa = True

while programa:
    def limparTela():
        os.system('cls')

    def conversorBinario(numero):
        resultado = str(bin(numero))
        print(f"O número {numero} em binário é {resultado}")

    def conversorHexadecimal(numero):
        resultado = str(hex(numero))
        print(f"O número {numero} em hexadecimal é {resultado}")

    numero = int(input("Digite um número decimal: "))

    threadBinario = threading.Thread(target=conversorBinario, args=(numero,))
    threadHexadecimal = threading.Thread(target=conversorHexadecimal, args=(numero,))

    threadBinario.start()
    threadHexadecimal.start()

    threadBinario.join()
    threadHexadecimal.join()

    restart = input("Deseja Converter novamente? y/n  ")
    if restart == "y":
        programa = True
        limparTela()

    elif restart == "n":
        programa = False
        limparTela()
        print("Obrigado por usar nosso conversor!")
    
    else:
        programa = False
        print("Error 404")
        time.sleep(2)
        limparTela()