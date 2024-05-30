import random

def linhas():
    print("="*64)

def regras():
    linhas()
    print("1- O computador escolhe um número secreto de 4 algarismos, com\ncada algarismo diferente dos outros.\n2- Sua missão é adivinhar o número secreto em até 8 tentativas.\n3- A cada tentativa, insira um número de 4 algarismos diferen\ntes.\n4- Após cada tentativa, o jogo dará um feedback: Verde: Você acer\ntou um algarismo no lugar certo. Amarelo: Você acertou um alga\nrismo, mas ele está em um lugar errado. Vermelho: O algarismo \nnão faz parte do número secreto.\n5- Continue tentando até acertar o número ou usar todas as 8 ten\ntativas.\n6- Se conseguir adivinhar o número secreto em até 8 tentativas, \nvocê vence.\n7- No final, o jogo revelará o número vencedor.")
    linhas()
    sair = ""
    while sair != "x":
        sair = input("Pressione a tecla (x) para sair: ").lower()
    main()

def creditos():
    linhas()
    print("Agradeço por jogar!\nEste minigame surgiu como uma forma lúdica de exercitar o raciocínio lógico e foi apresentado a mim durante uma disciplina do curso de Análise e Desenvolvimento de Sistemas no campus IFSP Sanca. Espero que tenha se divertido tentando desvendar o número misterioso, assim como eu me diverti durante minhas aulas.\nAté o próximo minigame!\n\nDesenvolvido por: Guilherme A. Mendes")
    linhas()
    sair = ""
    while sair != "x":
        sair = input("Pressione a tecla (x) para sair: ").lower()
    main()
    

def verifica_string(string):
    desempacotador = ""
    for x in string:
        if x not in desempacotador:
            desempacotador += x
    return desempacotador

def game():
    dnv = True
    while dnv == True:
        vetor = []
        NumVencedor = ""
        while len(vetor) != 4:
            NumAlet = random.randint(0, 9)
            if NumAlet not in vetor:
                vetor.append(NumAlet)
                NumVencedor+=str(NumAlet)
        linhas()
        for x in range(8):
            linhas()
            print(f"{x+1}° tentativa")
            i = True
            while i == True:
                NumUser = input("Digite um número de 4 algarismos diferentes: ")
                if len(NumUser) == 4 and NumUser.isdigit() and len(verifica_string(NumUser)) == 4:
                    NumUserFormat = NumUser
                    green = yellow = red = 0
                    for y in range(0, len(NumUserFormat)):
                        if NumUserFormat[y] == NumVencedor[y]:
                            green += 1
                        elif NumUserFormat[y] in NumVencedor:
                            yellow += 1
                        else:
                            red += 1
                    print(f"\nVerde: {green}.\nAmarelo: {yellow}.\nVermelho: {red}.")
                    i = False
                else:
                    linhas()
                    print(f"Ops, número inválido. Lembre-se de usar 4 algarismos distintos. Tente novamente.")
            if NumUserFormat == NumVencedor:
                linhas()
                print("Boa jogada, você adivinhou nosso número parabéns!")
                break

        print(f"O número vencedor era {NumVencedor}. Esperamos te ver novamente jogador.")
        linhas()
        pgt = input("Deseja jogar mais uma vez (s/n)?: ").lower()
        if pgt == "n":
            dnv = False

def main():
    linhas()
    menu = ""
    while menu != "4":
        print("Menu principal\n1- Joga.\n2- Regras.\n3- Créditos.\n4- Sair.")
        opcao = input("Insira o digito do menu desejado: ")
        if opcao == "1":
            game()
        elif opcao == "2":
            regras()
        elif opcao == "3":
            creditos()
        elif opcao == "4":
            menu = "4"
            linhas()
    print("Obrigado por jogar. Volte sempre que quiser!")
    linhas()

main()
