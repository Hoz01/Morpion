#################################
#       Auteur : Hoz01          #
#       Le : 21/01/2020         #
#################################


from tkinter import *
from tkinter import messagebox


def Clique(event):
    global a, Colonne1, Colonne2, Colonne3, Colonne1RC, Colonne1R, Colonne2RC, Colonne2R, Colonne3RC, Colonne3R, Ligne1RC, Ligne1R, Ligne2RC, Ligne2R, Ligne3RC, Ligne3R, Ligne1, Ligne2, Ligne3
#Permet de récupérer la position du curseur de la souris
    X = event.x
    Y = event.y

#Si a = 0 on place une croix
    if a == 1:
        if X < 100:
            if Y < 100:
                if Colonne1[0] == 2:
                    a = 0
                    Colonne1[0] = 1
                    Ligne1[0] = 1
                    Croix(50, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')
            else:
                if Y < 200:
                    if Colonne1[1] == 2:
                        a = 0
                        Colonne1[1] = 1
                        Ligne2[0] = 1
                        Croix(50, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')
                else:
                    if Colonne1[2] == 2:
                        a = 0
                        Colonne1[2] = 1
                        Ligne3[0] = 1
                        Croix(50, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

        if X < 200 and X > 100:
            if Y < 100:
                if Colonne2[0] == 3:
                    a = 0
                    Colonne2[0] = 1
                    Ligne1[1] = 1
                    Croix(150, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')
            else:
                if Y < 200:
                    if Colonne2[1] == 3:
                        a = 0
                        Colonne2[1] = 1
                        Ligne2[1] = 1
                        Croix(150, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')
                else:
                    if Colonne2[2] == 3:
                        a = 0
                        Colonne2[2] = 1
                        Ligne3[1] = 1
                        Croix(150, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

        if X < 300 and X > 200:
            if Y < 100:
                if Colonne3[0] == 4:
                    a = 0
                    Colonne3[0] = 1
                    Ligne1[2] = 1
                    Croix(250, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

            else:
                if Y < 200:
                    if Colonne3[1] == 4:
                        a = 0
                        Colonne3[1] = 1
                        Ligne2[2] = 1
                        Croix(250, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

                else:
                    if Colonne3[2] == 4:
                        a = 0
                        Colonne3[2] = 1
                        Ligne3[2] = 1
                        Croix(250, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

#Si a = 1 alors on place un rond
    else:
        if X < 100:
            if Y < 100:
                if Colonne1[0] == 2:
                    a = 1
                    Colonne1[0] = 0
                    Ligne1[0] = 0
                    Cercle(50, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

            else:
                if Y < 200:
                    if Colonne1[1] == 2:
                        a = 1
                        Colonne1[1] = 0
                        Ligne2[0] = 0
                        Cercle(50, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

                else:
                    if Colonne1[2] == 2:
                        a = 1
                        Colonne1[2] = 0
                        Ligne3[0] = 0
                        Cercle(50, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

        if X < 200 and X > 100:
            if Y < 100:
                if Colonne2[0] == 3:
                    a = 1
                    Colonne2[0] = 0
                    Ligne1[1] = 0
                    Cercle(150, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

            else:
                if Y < 200:
                    if Colonne2[1] == 3:
                        a = 1
                        Colonne2[1] = 0
                        Ligne2[1] = 0
                        Cercle(150, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

                else:
                    if Colonne2[2] == 3:
                        a = 1
                        Colonne2[2] = 0
                        Ligne3[1] = 0
                        Cercle(150, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

        if X < 300 and X > 200:
            if Y < 100:
                if Colonne3[0] == 4:
                    a = 1
                    Colonne3[0] = 0
                    Ligne1[2] = 0
                    Cercle(250, 50)
                else:
                    messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')
            else:
                if Y < 200:
                    if Colonne3[1] == 4:
                        a = 1
                        Colonne3[1] = 0
                        Ligne2[2] = 0
                        Cercle(250, 150)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')

                else:
                    if Colonne3[2] == 4:
                        a = 1
                        Colonne3[2] = 0
                        Ligne3[2] = 0
                        Cercle(250, 250)
                    else:
                        messagebox.showinfo(title='Impossible', message='La case est déjà occupée !')


#Fonction qui permet d'afficher les ronds
def Cercle(x1, y1):
    global Colonne1, Colonne2, Colonne3
    Canvas.create_oval(x1 - 45, y1 - 45, x1 + 45, y1 + 45, fill = "red")
    Verif()


#Fonction qui permet d'afficher les croix
def Croix(x1, y1):
    global C1, C2, C3
    Canvas.create_line(x1 - 45, y1 - 45, x1 + 45, y1 + 45, fill = "blue")
    Canvas.create_line(x1 + 45, y1 - 45, x1 - 45, y1 + 45, fill = "blue")
    Verif()


#Fonction qui permet de compter les points
def Verif():
    global Colonne1, Colonne2, Colonne3, Colonne1RC, Colonne1R, Colonne2RC, Colonne2R, Colonne3RC, Colonne3R, Ligne1RC, Ligne1R, Ligne2RC, Ligne2R, Ligne3RC, Ligne3R, Ligne1, Ligne2, Ligne3
    Colonne1RC = Colonne1.count(1)
    Colonne1R = Colonne1.count(0)
    Colonne2RC = Colonne2.count(1)
    Colonne2R = Colonne2.count(0)
    Colonne3RC = Colonne3.count(1)
    Colonne3R = Colonne3.count(0)

    Ligne1RC = Ligne1.count(1)
    Ligne1R = Ligne1.count(0)
    Ligne2RC = Ligne2.count(1)
    Ligne2R = Ligne2.count(0)
    Ligne3RC = Ligne3.count(1)
    Ligne3R = Ligne3.count(0)

    # ici on affiche le joueur qui a gagner
    if Colonne1RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Colonne1R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')
    if Colonne2RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Colonne2R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')
    if Colonne3RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Colonne3R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')

    if Colonne1[0] == 1 and Colonne2[1] == 1 and Colonne3[2] == 1:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Colonne1[2] == 1 and Colonne2[1] == 1 and Colonne3[0] == 1:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')

    if Colonne1[0] == 0 and Colonne2[1] == 0 and Colonne3[2] == 0:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')
    if Colonne1[2] == 0 and Colonne2[1] == 0 and Colonne3[0] == 0:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')

    if Ligne1RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Ligne1R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')
    if Ligne2RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Ligne2R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')
    if Ligne3RC == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 1 qui remporte la victoire !')
    if Ligne3R == 3:
        messagebox.showinfo(title='Victoire', message='C\'est le joueur 2 qui remporte la victoire !')


# ici on initialise les colones et les lignes

Colonne1RC, Colonne1R, Colonne2RC, Colonne2R, Colonne3RC, Colonne3R, Ligne1RC, Ligne1R, Ligne2RC, Ligne2R, Ligne3RC, Ligne3R = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

a = 1

Colonne1 = [2, 2, 2]
Ligne1 = [2, 2, 2]

Colonne2 = [3, 3, 3]
Ligne2 = [3, 3, 3]

Colonne3 = [4, 4, 4]
Ligne3 = [4, 4, 4]


#Créer la fenêtre TKinter
Fenetre = Tk()
Fenetre.title("Tic-Tac-Toe")

#Permet de définir la hauteur et la largeur de la fenêtre TKinter grâce a une variable
Largeur = 300
Hauteur = 300
Canvas = Canvas(Fenetre, width=Largeur, height=Hauteur, bg="bisque")


#Permet de lier la fonction "clique" au clique de la souris
Canvas.bind("<Button-1>", Clique)
Canvas.pack(padx=5, pady=5)


#Délimitation des colonnes et des lignes

Canvas.create_line(0, 100, 300, 100, fill="black", width=4)

Canvas.create_line(0, 200, 300, 200, fill="black", width=4)

Canvas.create_line(100, 300, 300, -100000, fill="black", width=4)

Canvas.create_line(200, 300, 300, -100000, fill="black", width=4)

#Permet de demander si l'on veut vraiment quitter le jeu
def Fermeture():
    if messagebox.askokcancel("Quitter", "Voulez vous vraiment quitter ?"):
        Fenetre.destroy()
Fenetre.protocol("WM_DELETE_WINDOW", Fermeture)

def Rejouer():
    ok = messagebox.askquestion("Rejouer", "Voulez-vous rejouer ?")
    if ok == "no":
        Fenetre.destroy()
    elif ok == "yes":
        Canvas.delete("ALL")

#Création du bouton quitter

Button(Fenetre, text = "Quitter", command = Fermeture, bg = "bisque", relief = GROOVE).pack(side = LEFT, padx = 5, pady = 5)

#Creation du bouton rejouer
Button(Fenetre, text = "Rejouer", command = Rejouer, bg = "bisque", relief = GROOVE).pack(side = LEFT, padx = 5, pady = 5)

Fenetre.mainloop()
