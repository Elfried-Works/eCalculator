# coding:utf-8
#Script Name : Calculator
#Author : Elfried (Viper75)
#Version : 1.0.0
#Downloads : www.elfriedworks.go.yo.fr


from tkinter import *
from tkinter.messagebox import *
import sys

x = Tk()
x.title("eCalcultor")
x.resizable(width=False, height=False)
expression = ""
tableau = StringVar() #Variable de controle associèe avec le Label (le tableau d'affichage)
history = {}

#Fonction qui gère le calcul....

def gerer(exp):
	global tableau
	global expression
	global history
	if exp == "=":
		try:
			resultat = eval(expression)
			tableau.set(resultat)
			var_history = expression
			expression = str(resultat)
			history[var_history] = resultat
		except:
			expression = "Erreur !"
			tableau.set(expression)
			expression = ""
	else:
		expression += str(exp)
		tableau.set(expression)
		
#Fonction effacer (clear)

def clear():
	global expression
	expression = ""
	tableau.set(expression)
	
#Calculatrice .....

def calc():
	
	text = Label(x, textvariable=tableau,height=3, bg="black", fg="white", ).grid(row=2, column=0, columnspan = 3, sticky="news")
	c = Button(x, text="C",fg="blue",width=10,height=5, bg="black",command = lambda:clear()).grid(row=2, column=3, sticky="news")
	b1 = Button(x,text="1",width=10,height=5, command = lambda:gerer(1)).grid(row=3, column = 0,sticky = "news")
	b2 = Button(x,text="2",width=10,height=5, command = lambda: gerer(2)).grid(row=3, column = 1,sticky = "news")
	b3 = Button(x,text="3",width=10,height=5, command = lambda: gerer(3)).grid(row=3, column = 2,sticky = "news")
	b4 = Button(x,text="4",width=10,height=5, command = lambda: gerer(4)).grid(row=4, column = 0,sticky = "news")
	b5 = Button(x,text="5",width=10,height=5,  command = lambda: gerer(5)).grid(row=4, column = 1,sticky = "news")
	b6 = Button(x,text="6",width=10,height=5,  command = lambda: gerer(6)).grid(row=4, column = 2,sticky = "news")
	b7 = Button(x,text="7",width=10,height=5,  command = lambda: gerer(7)).grid(row=5, column = 0,sticky = "news")
	b8 = Button(x,text="8",width=10,height=5,  command = lambda: gerer(8)).grid(row=5, column = 1,sticky = "news")
	b9 = Button(x,text="9",width=10,height=5, command = lambda: gerer(9)).grid(row=5, column = 2,sticky = "news")
	b10 = Button(x,text="0",width=10,height=5, command = lambda: gerer(0)).grid(row=6, column = 1,sticky = "news")
	b11 = Button(x,text=".",width=10,height=5, command = lambda: gerer(".")).grid(row=6, column=0,sticky = "news")
	b12 = Button(x,text="=",width=10,height=5,  command = lambda: gerer("=")).grid(row=6, column=2,sticky = "news")
	b13 = Button(x,text="+",width=10,height=5, command = lambda: gerer("+")).grid(row=3, column=3,sticky = "news")
	b14 = Button(x,text="-",width=10,height=5, command = lambda: gerer("-")).grid(row=4, column=3, sticky="news")
	b15 = Button(x,text="x",width=10,height=5, command = lambda: gerer("*")).grid(row=5, column=3,sticky = "news")
	b16 = Button(x,text="÷",width=10,height=5, command = lambda: gerer("/")).grid(row=6, column=3,sticky = "news")
	btn_propos = Button (x,text = "A propos", command = infos, fg = "white", bg = "navy").grid(row=7, column=0, columnspan=2, sticky = "news")
	btn_quitter = Button(x, text="Quitter",command = quitter, fg = "white", bg = "navy").grid(row=7, column=2,columnspan=2, sticky = "news")
	btn_update = Button(x, text="Update",fg = "white", bg = "navy").grid(row = 8, column = 0, columnspan=2, sticky="news")
	btn_noads = Button(x, text="Don",fg = "white", bg = "navy" ).grid(row = 8, column = 2, columnspan = 2, sticky = "news")

#Information ...

def infos():
	help = """Nom du logiciel : eCalculator \nAuteur : Elfried (V1P3R 75) \nVersion : 1.0.0 \nSite : github.com/Elfried-Works\nContacts : \n \tGitHub: ElfriedWorks \n \tYoutube : ElfriedWorks \n \tEmail: elfried@works.com"""
	
	showinfo("À propos de eCalculator", help)

def quitter():
        reply = askquestion("Quitter", "Voulez-vous vraiment quitter ?")
        if reply == "yes":
                x.destroy()
        else:
                pass

calc()
x.mainloop()
