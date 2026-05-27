import tkinter as tk
from tkinter import messagebox


def score():

    prof = prof_var.get()

    if prof == "y":
        bonus = 1
            
    else:
        bonus = 0

    try:
        dice = float(entry_dice.get()) + bonus
        roleplay = float(entry_roleplay.get()) + bonus

        results = (dice / 4) * roleplay
        messagebox.showinfo( "Resultado", f"Sua nota de roleplay foi {roleplay} e seu dado representa {dice} . Totalizando {results} pontos")
    
        print(f"Sua nota de rolepay foi {roleplay} e seu dado representa {dice} . Totalizando {results} pontos")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para o dado e o fator de roleplay.")
   
        
#Criar janela principal

window = tk.Tk()
window.title("D20")
window.geometry("400x300")

#Proficiencia check

prof_var = tk.BooleanVar()
prof_check = tk.Checkbutton(
                        window, 
                        text="Proficiencia", 
                        variable=prof_var
                        )

prof_check.pack(pady=10)


#Entrada de dados

label_dice = tk.Label(window,
                     text="Valor do Dado:"
                     )
label_dice.pack()

entry_dice = tk.Entry(window)
entry_dice.pack()


label_roleplay = tk.Label(
                        window, 
                        text="Fator Roleplay:"
                        )
                        
label_roleplay.pack()

entry_roleplay = tk.Entry(window)
entry_roleplay.pack()

#botão para calcular

botao = tk.Button(
                window, 
                text="Calcular", command=score
                )

botao.pack(pady=20)

window.mainloop()









        
