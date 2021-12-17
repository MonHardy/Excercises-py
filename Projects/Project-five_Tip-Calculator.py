print("Welcome to the tip calculator!\n")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
peoples = int(input("How many people to split the bill?\n"))

#round - arredonda para o número de dígitos fornecido 
# e retorna o número de ponto flutuante, 
# se nenhum número de dígitos for fornecido para arredondamento, 
# ele arredonda o número para o inteiro mais próximo.

pc = percent / 100 * total + total
pc1 = pc / peoples
pc2 = round(pc1, 2)
pc2 = "{:.2f}".format(pc1)


print(f"Each person should pay: ${pc2}")
