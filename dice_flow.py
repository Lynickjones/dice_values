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

    if prof:
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


       

#Main Window

window = tk.Tk()
window.title("flow D20")
window.geometry("700x220")
window.resizable(False, False)
#Image Files here!

icon = tk.PhotoImage(file=r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\icon1.png")
icon2 = tk.PhotoImage(file=r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\icon2.png") 


window_bg = tk.PhotoImage(file=r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\background_0.png")
bg_label = tk.Label(window, image=window_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

#Proficiencia check

prof_var = tk.BooleanVar()
prof_check = tk.Checkbutton(
                        window, 
                        text="Proficiência", 
                        variable=prof_var,
                        bg = "#af5a5e",
                        font = ("times new roman", 10, "bold")
                        )

prof_check.pack(pady=1)

botao2 = tk.Button(
    window,
    text="Rolar D20",
    command=roll,
    bg = "red",
    fg = "white",
    font = ("times new roman", 12, "bold"),
    image = icon ,
    compound = "left" 
)

botao2.pack(pady=2)
#Entrada de dados

label_dice = tk.Label(window,
                     text="Valor do Dado:",
                     bg = "#af5a5e",
                     fg = "white",
                     image = icon2,
                     compound = "left"
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

img_char = [
    ImageTk.PhotoImage(Image.open(r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\char1.png").resize((70,70), Image.NEAREST)),
    ImageTk.PhotoImage(Image.open(r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\char2.png").resize((70,70), Image.NEAREST)),
    ImageTk.PhotoImage(Image.open(r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\char3.png").resize((70,70), Image.NEAREST)),
    ImageTk.PhotoImage(Image.open(r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\char4.png").resize((70,70), Image.NEAREST))
]



scores_pic = ImageTk.PhotoImage(Image.open(r"C:\Users\Lynick Jones\Desktop\Palythoa_ID\Dice_set\pics\scores.PNG").resize((250 , 150), Image.NEAREST))

frame_img = tk.Frame(window, bg="#af5a5e", width=250, height=150)
frame_img.place(relx=0.98, rely=0.5, anchor="e")

frame_img.pack_propagate(False)


label_img = tk.Label(frame_img, image=scores_pic, bg="#af5a5e")
label_img.pack(expand=True)




def charset(name, x, y, img_char):
    char = tk.Checkbutton(
                        window, 
                        text=name, 
                        variable=img_char,
                        bg = "#5aaf97",
                        font = ("times new roman", 10),
                        image = img_char,
                        compound="top"
                        )
    char.place(relx = x, rely = y)



prof_check.pack(pady=1)

charset("Kyle", 0.05, 0.03, img_char[0])
charset("Leora", 0.23, 0.03, img_char[1])
charset("Mike", 0.05, 0.5, img_char[2])
charset("O J", 0.23, 0.5, img_char[3])


window.mainloop()