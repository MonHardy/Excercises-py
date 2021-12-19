print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
''')

print("Bem vindo a 'Caça ao Tesouro'. \n Sua missão é encontrar o tesouro final!!\n")
start = input('Você\' quer começar? Digite "Sim" para começar ou "Não" para sair: ').lower()

if start == "s" or start == "sim":
   parte1 = input("\nVamos começar!\n \nVocê está andando em uma estrada deserta e escura até que se depara com uma bifurcação, você não consegue ler as placas por causa da escuridão e a densa neblina que a preenche, mas sabe que à direita há uma placa de madeira polida que parece dizer 'O presente' enquanto que, do lado esquerdo, pôde jurar que viu uma placa desgasta onde leu 'O futuro' e entre as duas, uma terceira placa 'Volte daqui'.\n \n Para qual lado você iria? \nEscolha entre Direita, Esquerda ou Retornar: ").lower()
   if parte1 == "esquerda":
            parte2 = input("A neblina fica ainda mais densa e chega a um ponto no qual você não consegue ver nada, nem mesmo seus próprios pés. A medida que você avança, consegue ouvir uma voz baixinha cantando e vai em direção aquilo. Aos poucos, a neblina começa a desaparecer e você reconhece a luz de um lampião aceso no meio da estrada, junto a um homem sentado no chão com vários objetos espalhados ao seu redor. Você se aproxima dele e ele sorri para você. Como ele sabe que você está ali? Difícil dizer. O homem é cego.\n\n Você percebe que o homem é um vendedor ambulante e pergunta para ele que caminho deve seguir para encontrar o tesouro perdido. O homem sorri e então lhe diz:\n\n'Ah! Outro viajante! Quantos deles vieram? Quantos deles se perderam? E para todos eles eu perguntei: Tem certeza de que seu tesouro não está aqui?'\n\n Então você olha os itens ao redor do homem e percebe alguns objetos: Um relógio de bolso (de ouro), uma bússola (de ouro) e um mapa.\n\n O homem te olha e você tem a possibilidade de roubar um: ").lower()
            if parte2 == "relógio":
               print("Você se abaixa e pega o relógio, quando se levanta o relógio não está mais em sua mão e o homem está te fazendo a mesma pergunta outra vez. Novamente, você se abaixa e pega o relógio, sem entender o que acaba de acontecer e a cena se repete outra e mais outra vez em um loop sem fim. \n\n Fim de jogo!")  
            elif parte2 == "bússola":
               print("Você se abaixa e pega a bússola mas quando se levanta sente vontade de roubar todos os objetos. A raiva inexplicável que cresce em você o domina e você sente as mudanças em seu corpo. Em questão de minutos o homem desaparece, rindo. Você sente sua pele rasgando e pelos crescendo, até que se torna uma besta e não tem mais domínio sobre o próprio corpo ou consciência. Fim de jogo!")
            elif parte2 == "mapa":
               print("Você se abaixa e pega o mapa mas quando se levanta o homem sumiu. Você abre o mapa na esperança de seguir seu caminho mas ele está em branco. Você vira o mapa de todos os lados mas nada acontece, a neblina volta e não importa por onde você vá, nada te leva a lugar nenhum. Fim de jogo!")
            elif parte2 == "nenhum":
               print("\nNão é nobre roubar de um cego, diz o homem. \n\nSe tivesse escolhido o relógio, estaria condenado a viver este momento pelo resto de sua existência pois a culpa te consumiria.\n\n Se tivesse escolhido a bússola, seria obrigado a realizar os seus desejos mais primitivos, pois esta aponta tão somente para a verdade que reside em nós mesmos e aquele que rouba de um cego não é digno de fazer as próprias escolhas. \n\n Se tivesse escolhido o mapa, este estaria em branco, pois o mapa só mostra o tesouro para aquele que sabe o que procura. \n\n Mas aquele que nada leva sempre sai com a certeza da virtude e por isso pode levar todos os objetos e seguir seu caminho, pois o virtuoso não se arrepende de suas ações, conhece a própria índole e sabe porque e o que deseja. Então, o homem desaparece e todos os objetos são agora seus. Parabéns!")
            else:
               print("Você não pode ficar em cima do muro... Há quatro respostas possíveis para essa situação. Pare de ser covarde e tome uma atitude!")  
   elif parte1 == "direita":
      print("\nVocê parte pela direita até chegar a uma estrada onde as árvores tomaram conta do caminho, é possível ouvir os lobos não muito longe dali. Você fica com medo, tenta voltar, mas quanto mais procura pelo caminho de onde veio, mais perdido fica. Você se perdeu na estrada para lugar nenhum de onde ninguém jamais conseguiu voltar. Dizem que este é o caminho dos indecisos, os que tiveram tanto medo da incerteza dos seus futuros que se perderam eternamente entre o passado e o presente. \n Fim de jogo!")
   else:
      print("Você volta para o mesmo lugar mas as placas sumiram e agora há um grupo de ladrões prontos para te roubar. Que azar!")
else: 
   print("Que pena! Foi bom te conhecer!")
