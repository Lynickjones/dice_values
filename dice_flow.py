import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def roll():

    value = random.randint(1, 20)

    entry_dice.delete(0, tk.END)
    entry_dice.insert(0, value)


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
window.title("flow D20")
window.geometry("400x200")

window_bg = tk.PhotoImage(file=r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\background_1.png")
bg_label = tk.Label(window, image=window_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Proficiencia check

prof_var = tk.BooleanVar()
prof_check = tk.Checkbutton(
                        window, 
                        text="Proficiência", 
                        variable=prof_var,
                        bg = "red",
                        fg = "white",
                        font = ("times new roman", 12, "bold")
                        )

prof_check.pack(pady=1)

botao2 = tk.Button(
    window,
    text="Rolar D20",
    command=roll,
    bg = "red",
    fg = "white",
    font = ("times new roman", 12, "bold") 
)

botao2.pack(pady=2)
#Entrada de dados

label_dice = tk.Label(window,
                     text="Valor do Dado:",
                     bg = "#af5a5e",
                     fg = "white"
                     )
label_dice.pack(pady=2)

entry_dice = tk.Entry(window)
entry_dice.pack(pady=2)


label_roleplay = tk.Label(
                        window, 
                        text="Fator Roleplay:",
                        bg = "#af5a5e",
                        fg = "white"
                        )
                        
label_roleplay.pack(pady=5)

entry_roleplay = tk.Entry(window)
entry_roleplay.pack()

#botão para calcular

botao = tk.Button(
                window, 
                text="Calcular", command=score
                )

botao.pack(pady=5)

window.mainloop()