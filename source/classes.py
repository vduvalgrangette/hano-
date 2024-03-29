# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:26:19 2024

@author: merrinicolasdematons
"""
from tkinter import*
from PIL import Image, ImageTk


class Perso():
    '''classe pour déplacer les personnages sur les canevas'''
    def __init__(self,plan,personnage,x,y):
        '''créaton du personnage'''
        self.x = x
        self.y = y
        self.plan=plan
        self.personnage=personnage
        self.canevas=self.plan.create_image(self.x,self.y,  image =self.personnage)
        
    def nouveaudebut(self,xn,yn,nimage):
        '''supprime l'image et la remplace par nimage aux coordonées xn et yn'''
        self.nimage=nimage
        self.xn=xn
        self.yn=yn
        self.plan.delete(self.canevas)
        self.canevas=self.plan.create_image(self.xn,self.yn,  image =self.nimage)
        self.x=self.xn
        self.y=self.yn

class Boite():
    '''affiche la boite des parametres avec le nombre de disque et les modes de jeu'''
    def __init__(self,plan,nombre,creationdisque,modeL,fen):
        '''créer la boite sans l'afficher'''
        global arriereplan2,arriereplan3
        self.plan=plan
        self.nombre=nombre
        self.creationdisque=creationdisque
        self.affiche=False
        self.modeL=modeL
        self.fen=fen
        self.nbdisque=20
        
    def afficherboite(self):
        '''affiche la boite '''
        self.cadreNombre1=Frame(self.plan, bg="red", border=20, relief=RAISED)
        self.cadreNombre1.pack()
        self.nombreLabel1=Label(self.cadreNombre1, text="Veuillez choisir le nombre de disque", font="Calibri 15")
        self.nombreLabel1.pack()
        self.nombre_Box1 = Spinbox(self.cadreNombre1, from_=3, to=self.nbdisque)
        self.nombre_Box1.config(textvariable=self.nombre)
        self.nombre_Box1.pack()
        if self.modeL==True:
            '''affiche les boutons des modes pour les jeux en mode libre'''
            self.modeLabel1=Label(self.cadreNombre1, text="Veuillez choisir le mode de jeu", font="Calibri 15")
            self.modeLabel1.pack(pady=15)
            self.modeLvaleur=StringVar()
            self.modeLvaleur.set("1")
            self.modeL1=Radiobutton(self.cadreNombre1,text="déplacer les disques avec le sportif", font="Calibri 15",variable=self.modeLvaleur, value="1")
            self.modeL1.pack()
            self.modeL2=Radiobutton(self.cadreNombre1,text="déplacer les disques avec la souris", font="Calibri 15",variable=self.modeLvaleur, value="2")
            self.modeL2.pack()
        self.nombreValider1=Button(self.cadreNombre1,text="Valider", font="Calibri 15", command=self.nombrevalide)
        self.nombreValider1.pack()
        self.nombre_canvas1=self.plan.create_window(650,250, window=self.cadreNombre1)
        self.affiche=True
        
    def initialisation(self,plan2,plan3,souris):
        '''rajoute des données utilisées dans nombrevalide() pour le jeu en mode libre'''
        self.drag_start=souris[0]
        self.drag_motion=souris[1]
        self.drag_drop=souris[2]
        self.plan2=plan2
        self.plan3=plan3
        
    def nombrevalide(self):
        '''lance le jeu en fonction des données rentrées'''
        self.cadreNombre1.destroy()
        if self.modeL==True :
            if self.modeLvaleur.get()=="1" and self.plan==self.plan3:
                self.plan3.pack_forget()
                self.plan2.pack()
                self.creationdisque(self.plan2,self.nombre)
                self.fen.unbind("<Button-1>")
                self.fen.unbind("<B1-Motion>")
                self.fen.unbind("<ButtonRelease>")
            elif self.modeLvaleur.get()=="2" and self.plan==self.plan2:
                self.plan2.pack_forget()
                self.plan3.pack()
                self.creationdisque(self.plan3,self.nombre)
                self.fen.bind("<Button-1>",self.drag_start)
                self.fen.bind("<B1-Motion>",self.drag_motion)
                self.fen.bind("<ButtonRelease>",self.drag_drop)
            else :
                self.creationdisque(self.plan,self.nombre)
        else :
            self.creationdisque(self.plan,self.nombre)
        self.affiche=False
        
class Comptagepoint():
    '''creation du cadre de comptage de point 
    et du score optimal pour le mode de jeu libre'''
    def __init__(self,plan,coup):
        self.plan=plan
        self.coup=coup
        self.cadrepoint=Frame(self.plan,bg="yellow", border=20, relief=RAISED)
        self.cadrepoint.pack()
        self.point_label1=Label(self.cadrepoint,bg="white", text="Score",font="Calibri 15")
        self.point_label1.grid(column=0,row=0,padx=10)
        self.point_label2=Label(self.cadrepoint,bg="white", text=str(self.coup),font="Calibri 15")
        self.point_label2.grid(column=0,row=1,padx=10)
        self.point_label3=Label(self.cadrepoint,bg="white", text="Score optimal",font="Calibri 15")
        self.point_label3.grid(column=1,row=0,padx=10)
        self.point_label4=Label(self.cadrepoint,bg="white", text="",font="Calibri 15")
        self.point_label4.grid(column=1,row=1,padx=10)
        self.point_canevas=self.plan.create_window(30,30,window=self.cadrepoint,  anchor = "nw",)

class Sortir():
    '''bouton pour revenir à l'écran d'acceuil'''
    def __init__(self,plan,arriereplan,lpositiondepart):
        self.plan=plan
        self.arriereplan=arriereplan
        self.lpositiondepart=lpositiondepart
        self.sortie=Button(self.plan,text="Retour", font="Calibri 15", command=self.quitter)
        self.sortie.pack()
        self.sortie_canvas=self.plan.create_window(1150,600,window=self.sortie)
        self.initialise=False
        self.initialise2=False
        self.initialise3=False
        
    def initialisation2(self,reinitialisation,boite1):
        '''rajoute des données utilisées dans la fonction quitter'''
        self.boite1=boite1
        self.reitialisation=reinitialisation
        self.initialise2=True
        
    def initialisation(self,fen):
        '''rajoute des données utilisées dans la fonction quitter'''
        self.fen=fen
        self.initialise=True
        
    def initialisation3(self,boite,porter):
        '''rajoute des données utilisées dans la fonction quitter'''
        self.initialise3=True
        self.boite=boite
        self.porter=porter
        
    def quitter(self):
        '''supprime les disques du mode solution,
        quitte le mode du jeu solution et ramène à l'écran d'accueil'''
        if self.initialise2==True :
            self.reitialisation()
            self.boite1.cadreNombre1.destroy()
            self.boite1.affiche=False
        else :
            for i in self.lpositiondepart:
                self.plan.delete(i.canevas)
        if self.initialise3==True :
            if self.porter!=None :
                self.plan.delete(self.porter.canevas)
                self.porter=False
            if self.boite.affiche==True :
                self.boite.cadreNombre1.destroy()
                self.boite.affiche=False
        self.plan.pack_forget()
        self.arriereplan.pack()
        if self.initialise==True :
            self.fen.unbind("<Button-1>")
            self.fen.unbind("<B1-Motion>")
            self.fen.unbind("<ButtonRelease>")

class Felicitation():
    '''cadre pour féliciter le joueur quand il termine le jeu'''
    def __init__(self,arriereplan2):
        self.arriereplan2=arriereplan2
        self.affiche=False
    def afficherfelicitation(self):
        '''affiche le cadre de félicitation'''
        if self.affiche==False :
            self.fincadre=Frame(self.arriereplan2, bg="red", border=20, relief=RAISED)
            self.fincadre.pack()
            self.finlabel=Label(self.fincadre,text="Bravo vous avez réussi", font="Calibri 15")
            self.finlabel.pack()
            self.finsuite=Button(self.fincadre,text="continuer à jouer",command=self.continuerjeu)
            self.finsuite.pack()
            self.fincanevas=self.arriereplan2.create_window(650,150, window=self.fincadre)
            self.afficher=True
            
    def continuerjeu(self):
        '''supprime le cadre de félicitation'''
        self.fincadre.destroy()
        self.affiche=False
