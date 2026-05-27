
def score():

    prof = input("Do you have prof? (y/n)").lower()
    if prof == "y":
        bonus = 1
            
    else:
        bonus = 0

    print("Digite o valor do dado:")
    dice = float(input()) + bonus

    print("Digite o valor do Fator Roleplay:")
    roleplay = float(input()) + bonus

    results = dice / 4 * roleplay
    print(f"Sua nota de rolepay foi {roleplay} e seu dado representa {dice} . Totalizando {results} pontos")

score()




            



        
