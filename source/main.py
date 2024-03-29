# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:22:05 2024

@author: merrinicolasdematons
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *    
import time as time
from deplacement import*
from classes import Perso, Felicitation, Boite, Comptagepoint, Sortir

#création de la fenêtre 

fen=Tk()
fen.title("Tour de Hanoï")
fen.geometry("1300x750")
fen.wm_iconbitmap('données/charactere-musclé-de-fin.ico')

#fonction générale pour la suite du programme servant dans les différents modes de jeu

def creationdisque(arriereplan,nombre):
    '''créer les disques en fonction du nombre entré et de l arriere plan choisi
    et initialise les dictionnaires place et equivalence ainsi que la liste 
    lpositiondepart'''
    global n,d,coup,lpositiondepart,l1,l2,l3,place,point_label4,point_label6,equivalence,nettoyage
    nettoyage()
    points2.point_label2.config(text=str(coup))
    points3.point_label2.config(text=str(coup))
    nombresplt=list(nombre.get())#nombre de disque choisi
    if len(nombresplt)>1:
        n=(ord(nombresplt[0])-ord("0"))*10+ord(nombresplt[1])-ord("0")#nombre de disque en int
    else :
        n=ord(nombre.get())-ord("0")#nombre de disque en int
    for i in range(n):
        #création des photos de disques de différentes tailles
        disque1=disque.resize((50+20*i,40))
        disque2=ImageTk.PhotoImage(disque1, master=fen)
        d.append(disque2)
    for j in range(n):
        disque3=Perso(arriereplan,d[n-j-1],350,600-30*j)#création des Perso disques
        #rajout des photo dans les différentes listes
        l1.append(disque3)
        equivalence[disque3]=n-j
    place[1]=l1
    place[2]=l2
    place[3]=l3
    lpositiondepart.extend(place[1])
    points2.point_label4.config(text=str(2**n-1))
    points3.point_label4.config(text=str(2**n-1))
    point_label6.config(text=str(2**n-1))
    point_label6.config(text=str(2**n-1))
    nbsec=(2**n-1)*3#calcul du temps de résolution pour le mode résolution
    ans=nbsec//(3600*24*365)
    jours=(nbsec-(3600*24*365)*ans)//(24*3600)
    heures=(nbsec-(3600*24*365)*ans-jours*24*3600)//3600
    minutes=(nbsec-(3600*24*365)*ans-jours*24*3600-heures*3600)//60
    secondes=nbsec-(3600*24*365)*ans-jours*24*3600-heures*3600-minutes*60
    tempsvaleur.config(text=f"{ans}ans, {jours}j, {heures}h, {minutes}min, {secondes}s")
    
def nettoyage():
    '''réinitialise les listes et les variables pour supprimer les bugs'''
    global d,coup,lpositiondepart,l1,l2,l3,place, equivalence, arrivee, porter
    coup=0#réinitialisation des scores
    d=[]
    lpositiondepart=[]
    l1=[]
    l2=[]
    l3=[]
    place=dict()
    place.clear()
    equivalence=dict()
    equivalence.clear()
    arrivee=1
    porter=None

#mise en place des disques et des listes utilisées quand l'utilisateur a choisi le nombre de disques
arrivee=1#tour de depart
disque=Image.open("données/Big Disque(1).png")#image du disque de depart
d=[]#liste de transition qui ne servira que dans la fonction creation disque
#listes de departs qui contiendront les images des disques en fonction de leur position dans le canevas
l1=[]
l2=[]
l3=[]
n=3#nombre de disques
lpositiondepart=[]#liste des images des disques dans l'ordre pour que la tour soit complète
place=dict()#renvoie la liste associée au nombre (1,2 ou 3) qui contiennent les images des disques
# du canevas correspondants aux emplacements de ces disques dans le jeu
equivalence=dict()#renvoie la taille du disque avec pour clé l'image du disque
stop=False#variable d'arrêt du programme solution
#variable pour demander le nombre de disque
nombre=StringVar()
nombre.set("3")
h=400#hauteur du soulever de disque du sportif
#creation d'une variable comptant le nombre de coup
coup=0

#interface d'accueil
def callback():
    '''demande si l utilisateur veut reellement quitter le jeu'''
    if askyesno('Tour de Hanoï', 'Êtes-vous sûr de vouloir quitter le jeu ?'):
        fen.destroy()

def modejeu():
    '''affiche l arriereplan correspondant au mode de jeu voulu s il a été selectionne
    sinon redemande le mode de jeu voulu'''
    global porter
    if mode.get()=="1":
        arriereplan.pack_forget()
        arriereplan1.pack()
        boite1.afficherboite()
        
    elif mode.get()=="2":
        arriereplan.pack_forget()
        arriereplan2.pack()
        boite2.afficherboite()
        fen.bind("<Key>", clavier)
        porter=None
        
    else:
        reponse=Label(cadre, text="Aucun mode n'a été sélectionné.")
        reponse.pack()

def regleapparition():
    '''fait apparaitre l arriere plan contenant les regles du jeu'''
    arriereplan.pack_forget()
    arriereplan4.pack()
    
def scoreapparition():
    '''Fait apparaître l'arriere plan des scores'''
    arriereplan.pack_forget()
    arriereplan5.pack()

arriereplan = Canvas(fen, width=1300, height=750)
arriereplan.pack()
cadre=Frame(fen,bg="blue", border=20, relief=RAISED)
cadre.pack(side=TOP, pady=30)
nom=Label(cadre,text="Sélectionner un mode", font="Calibri 17")
nom.pack()  
mode=StringVar()
mode.set("0")
mode1=Radiobutton(cadre,text="solution", font="Calibri 15",variable=mode, value="1")
mode1.pack()
mode2=Radiobutton(cadre,text="jeu libre", font="Calibri 15",variable=mode, value="2")
mode2.pack()
jouer=Button(cadre,text="jouer", font="Calibri 15", command=modejeu)
jouer.pack(pady=10)
regle_bouton=Button(cadre, text="Règles du jeu", font="Calibri 15",command=regleapparition)
regle_bouton.pack(pady=10)
score_bouton=Button(cadre, text="Scores", font="Calibri 15", command=scoreapparition)
score_bouton.pack(pady=10)
acceuil=arriereplan.create_window(525,250,window=cadre,  anchor = "nw")
image=Image.open("données/Décor2.png")
image1=image.resize((1300,750))
image2=ImageTk.PhotoImage(image1, master=fen)
imagePlan=arriereplan.create_image( 0, 0, image = image2, anchor = "nw")
cadre1=Frame(fen,bg="blue", border=10)
sortie=Button(cadre1,text="Retour", font="Calibri 12", command=callback)
sortie.pack()
sortie_canvas=arriereplan.create_window(1150,600,window=cadre1)


#Règles du jeu

def quitterRegles():
    '''quitte l'écran affichant les regles du jeu et renvoie à l'écran d'acceuil'''
    arriereplan4.pack_forget()
    arriereplan.pack()
    

#mise en place de l'arriereplan avec le regles du jeu   
arriereplan4 = Canvas(fen, width=1300, height=750, background='white')
reglesTexte1=arriereplan4.create_text(600,50, text="Règles du jeu", font ="Arial 20 italic")
reglesTexte2=arriereplan4.create_text(600,175, text="""
Le but du jeu est de déplacer des disques de diamètres différents
d'une tour de départ à une tour d arrivée en passant par une tour intermédiaire 
et ceci en un minimum de coups, tout en respectant les
règles suivantes :
-On ne peut déplacer plus d'un disque à la fois
-On ne peut placer un disque que sur un disque plus grand ou sur un emplacement vide""", font ="Arial 16 italic")
sortie=Button(fen,text="Retour", font="Calibri 15",bg='white', command=quitterRegles)
sortie.pack()
sortie_canvas=arriereplan4.create_window(1150,600,window=sortie)
imageC=Image.open("données/schéma_complexité.png")
imageC1=imageC.resize((500,300))
imageC2=ImageTk.PhotoImage(imageC1, master=fen)
arriereplan4.create_image( 200, 300, image = imageC2, anchor = "nw")


#scores des parties
def quitterscore():
    '''Quitte l'arrière plan des scores, et ramène à l'écran d'acceuil'''
    arriereplan5.pack_forget()
    arriereplan.pack()

#mise en place de l'arriereplan des scores
arriereplan5 = Canvas(fen, width=1300, height=750, background='white')
score_titre=Label(arriereplan5,text="Scores précédents",font="Calibri 20", borderwidth=50,background='white')
score_titre.grid(row=0, column=2)
scores=[]
parties=1

#creation des différents labels
for ligne in range(1,20):
    lLigne=[]
    for colonne in range(1,4):
        t1=Label(arriereplan5, text='',background='white')
        t1.grid(row=ligne, column=colonne,padx=60, pady=10)
        if colonne==1 :
            t1.config(text='Partie '+ str(ligne-1))
        lLigne.append(t1)
    scores.append(lLigne)
scores[0][0].config(text='Parties')
scores[0][1].config(text='Nombre de disques')
scores[0][2].config(text='Score')

#creation du bouton de sortie du tableau des scores
sortie5=Button(arriereplan5, text='Retour', font="Calibri 13",command=quitterscore)
sortie5.grid(row=12,column=4,padx=50)


#mode solution du jeu
def resolution(a,b,c,n):
    '''deplace les disque pour resoudre le probleme de la tour de hanoi'''
    global stop, porter,place
    if stop==True :
        return None 
    if n==1 : 
        #deplace le disque de la position a à la position c
        porter=place[a][len(place[a])-1]
        mouvementv(arriereplan1,porter,300-porter.y)
        porter.y=300
        mouvementh(arriereplan1,porter,50+300*c-porter.x)
        porter.x=50+300*c
        deplacer(place[a],place[c])
        if len(place[c])<1 :
            mouvementv(arriereplan1,porter,300)
            porter.y=600
            porter=None
        else :
            mouvementv(arriereplan1,porter,300-(len(place[c])-1)*30)
            porter.y=600-(len(place[c])-1)*30

    else :
        resolution(a,c,b,n-1)
        
        #deplace le disque de la position a à la position c
        porter=place[a][len(place[a])-1]
        mouvementv(arriereplan1,porter,300-porter.y)
        porter.y=300
        mouvementh(arriereplan1,porter,50+300*c-porter.x)
        porter.x=50+300*c
        deplacer(place[a],place[c])
        if len(place[c])<1 :
            mouvementv(arriereplan1,porter,300)
            porter.y=600
            porter=None

        else :
            mouvementv(arriereplan1,porter,300-(len(place[c])-1)*30)
            porter.y=600-(len(place[c])-1)*30

        resolution(b,a,c,n-1)

def reinitialisation() :
    '''supprime les disques du mode solution'''
    global lancement, stop,nettoyage,lpositiondepart
    nettoyage()
    stop=True
    lancer_bouton.configure(text='lancer la résolution')
    porter=None
    lancement=False
    for i in lpositiondepart:
        arriereplan1.delete(i.canevas)

def lancer():
    '''appelle la fonction de résolution si elle n est pas déja lancée
    Sinon, supprime les disques du canevas et fait apparaitre la boite demandant le nombre de disque'''
    global lancement,stop,nettoyage,lpositiondepart,resolution
    stop=False
    if lancement==False :
        lancer_bouton.configure(text='recommencer')
        lancement=True
        resolution(1,2,3,n)
    else :
        lancer_bouton.configure(text='lancer la résolution')
        porter=None
        lancement=False
        for i in lpositiondepart:
            arriereplan1.delete(i.canevas)
        boite1.afficherboite()
        nettoyage()
        
    
#mise en place de l'arriere plan du mode jeu solution
arriereplan1 = Canvas(fen, width=1300, height=750, background='white')
arriereplan1.create_image( 0, 0, image = image2, anchor = "nw")
#création de la boite pour demander le nombre de disque
boite1=Boite(arriereplan1,nombre,creationdisque,False,fen)
#création du bouton pour lancer l'algorithme de résolution
lancer_bouton=Button(arriereplan1,bg='white', text='lancer la résolution',font="Calibri 15", anchor=SW, command=lancer) 
lancer_bouton.pack()
lancer_canvas=arriereplan1.create_window(550, 250, window=lancer_bouton,anchor=SW)
lancement=False#variable représentant si le mode résolution est en cours ou non
#mise en place du bouton pour sortir du mode de résolution
varResolution=False
sortie1=Sortir(arriereplan1, arriereplan, lpositiondepart)
sortie1.initialisation2(reinitialisation, boite1)
#creation du cadre du meilleur score pour la résolution
cadrepoint_sol=Frame(fen,bg="yellow", border=20, relief=RAISED)
cadrepoint_sol.pack()
point_label5=Label(cadrepoint_sol,bg="white", text="Score optimal",font="Calibri 15")
point_label5.pack(padx=10)
point_label6=Label(cadrepoint_sol,bg="white", text="",font="Calibri 15")
point_label6.pack(padx=10)
point_sol_canevas=arriereplan1.create_window(30,30,window=cadrepoint_sol,  anchor = "nw",)

#creation du cadre d'estimation du temp de résolution
ans,jours,heures,minutes,secondes=0,0,0,0,0
cadretemps=Frame(fen,bg="yellow", border=20, relief=RAISED)
cadretemps.pack()
tempstexte=Label(cadretemps,bg="white", text="temps de résolution",font="Calibri 15")
tempstexte.pack(padx=10)
tempsvaleur=Label(cadretemps,bg="white", text=f"{ans}ans, {jours}j, {heures}h, {minutes}min, {secondes}s",font="Calibri 15")
tempsvaleur.pack(padx=10)
temps_canevas=arriereplan1.create_window(950,30,window=cadretemps,  anchor = "nw",)


#jeu en mode libre
def clavier(event):
    '''fait bouger le sportif en fonction de la touche pressée
    Si la tour a été entièrement déplacée affiche le cadre de félicitation'''
    global porter,place, coup, deplacement, scores, parties, n, arrivee
    
    if deplacement==False:
        '''vérifie que le sportif ne se deplace pas, ce qui poserait des bugs'''
        deplacement=True
        x=300
        touche = event.keysym
        position=(sportif.x-50)//300
        
        if touche == "Left" and sportif.x!=350:
            if porter == None :
                '''deplace le sportif vers la gauche'''
                animationh(arriereplan2,sportif,-x,costume)
            else:
                '''deplace le sportif et le disque vers la gauche'''
                animation2h(arriereplan2,sportif,porter,-x,costume)
                deplacer(place[position],place[position-1])
                
        elif touche == "Right" and sportif.x!=950:
            if porter==None :
                '''deplace le sportif vers la droite'''
                animationh(arriereplan2,sportif,x,costume)
            else :
                '''deplace le sportif et le disque vers la droite'''
                animation2h(arriereplan2,sportif,porter,x,costume)
                deplacer(place[position],place[position+1])
                
        elif touche=="Up" and porter==None and len(place[position])!=0:
            #soulève le disque 
            porter=place[position][len(place[position])-1]
            soulever(arriereplan2, sportif, porter, h-porter.y, lever)
            porter.y=h
            coup+=1
            points2.point_label2.config(text=str(coup))
            points3.point_label2.config(text=str(coup))
            boite2.porter=True
            
        elif touche=="Down" and porter!=None :
            #pose le disque
            boite2.porter=False
            if len(place[position])<=1 :
                deposer(arriereplan2,sportif,porter,600-h,poser)
                porter.y=600
                porter=None
            elif equivalence[porter]<equivalence[place[position][-2]] :
                deposer(arriereplan2,sportif,porter,600-h-(len(place[position])-1)*30,poser)
                porter.y=600-(len(place[position])-1)*30
                porter=None
            if (place[1]==lpositiondepart or place[2]==lpositiondepart or place[3]==lpositiondepart) and arrivee!=position and porter==None:
                '''affiche le cadre de félicitation'''
                findujeu2.afficherfelicitation()
                #ajoute le score dans le tableau des scores
                scores[parties][1].config(text=str(n))
                scores[parties][2].config(text=str(coup))
                parties+=1
                coup=0
                points2.point_label2.config(text=str(coup))
                points3.point_label2.config(text=str(coup))
                arrivee=position
                
        deplacement=False

def parametre(): 
    '''affiche le cadre des parametres du jeu : le nombre de disque et le mode de jeu'''
    global porter
    if  boite2.affiche==False :
        for i in lpositiondepart:
            arriereplan2.delete(i.canevas)
        boite2.afficherboite()
        porter=None
    

#mise en place de l'arriereplan2 du mode de jeu libre
arriereplan2 = Canvas(fen, width=1300, height=750, background='white')
imagePlan2=arriereplan2.create_image( 0, 0, image = image2, anchor = "nw")
#création de la boite pour demander le nombre de disque
boite2=Boite(arriereplan2,nombre,creationdisque,True,fen)
#mise en place du bouton parametre pour changer le nombre de disque
parametre_bouton=Button(fen,text="Parametre", font="Calibri 15",bg='white', command=parametre)
parametre_bouton.pack()
parametre_canevas=arriereplan2.create_window(1150,10,window=parametre_bouton,  anchor = "nw",)
 #creation du cadre de comptage de point et du score optimal pour le mode de jeu libre
points2=Comptagepoint(arriereplan2,coup)
#consignes pour jouer
conseilT2="""Déplacer le sportif en 
utilisant les flèches du clavier"""
conseil2=Label(fen,bg="white", text=conseilT2,font="Calibri 15")
conseil2.pack()
conseil2_canevas=arriereplan2.create_window(850, 65, window=conseil2,anchor=SW)

#mise en place du personnage du sportif et de ses différentes positions
costume=[]#positions de déplacement
costume.append(imagePlan2)
for i in range(1,7):
    costume_image1=Image.open("données/deplacement/Perso-"+str(i)+".png")
    costume_image2=costume_image1.resize((550,1200))
    costume_image3=ImageTk.PhotoImage(costume_image2, master=fen)
    costume.append(costume_image3)

#personnage en lui-même
sportif=Perso(arriereplan2,costume[1],650,300)
porter=None
deplacement=False 

lever=[]#positions pour soulever le disque
lever.append(imagePlan2)
for i in range(1,5):
    lever_image1=Image.open("données/lever/Perso-"+str(i)+".png")
    lever_image2=lever_image1.resize((550,1200))
    lever_image3=ImageTk.PhotoImage(lever_image2, master=fen)
    lever.append(lever_image3)

poser=[]#positions pour poser le disque
poser.append(imagePlan2)
for i in range(10,16):
    costume_image1=Image.open("données/poser/Perso-"+str(i)+".png")
    costume_image2=costume_image1.resize((550,1200))
    costume_image3=ImageTk.PhotoImage(costume_image2, master=fen)
    poser.append(costume_image3)

findujeu2=Felicitation(arriereplan2)
#mise en place du bouton pour sortir du mode de jeu libre
sortie2=Sortir(arriereplan2, arriereplan, lpositiondepart)
sortie2.initialisation3(boite2,porter)


#jeu avec  la souris
def parametre3(): 
    '''Affiche le cadre de parametre'''
    if  boite3.affiche==False :
        for i in lpositiondepart:
            arriereplan3.delete(i.canevas)
        boite3.afficherboite()


def drag_start(event):
    '''fonction lorsque la souris est cliquée, sélectionne le disque voulu'''
    global position
    disque.startX = event.x
    disque.startY = event.y
    if event.x>215 and event.x<465:
        position=1
    elif event.x>515 and event.x<774:
        position=2
    if event.x>860 and event.x<1118:
        position=3


def drag_motion(event):
    '''fonction lorsque la souris se déplace, déplace le disque sélectionné'''
    global position
    x=event.x-place[position][-1].x
    y=event.y-place[position][-1].y
    arriereplan3.move(place[position][-1].canevas,x,y)
    place[position][-1].x=event.x
    place[position][-1].y=event.y


def drag_drop(event):
    '''fonction lorsque la souris est lachée '''
    global position, place, equivalence, coup, parties, n, arrivee
    if position!=0:
        nposition=0
        if event.x>215 and event.x<500:
            nposition=1
        elif event.x>500 and event.x<800:
            nposition=2
        if event.x>800 and event.x<1118:
            nposition=3
        if place[nposition]==[]:
            x=350+300*(nposition-1)
            y=600
            place[position][-1].nouveaudebut(x, y,place[position][-1].personnage)
            deplacer(place[position],place[nposition])
        elif equivalence[place[position][-1]]< equivalence[place[nposition][-1]] :
            x=350+300*(nposition-1)
            y=(600-len(place[nposition])*30)
            place[position][-1].nouveaudebut(x, y,place[position][-1].personnage)
            deplacer(place[position],place[nposition])
        else :
            x=350+300*(position-1)
            y=(600-(len(place[position])-1)*30)
            place[position][-1].nouveaudebut(x, y,place[position][-1].personnage)
        coup+=1 
        points3.point_label2.config(text=str(coup))
        if (place[1]==lpositiondepart or place[2]==lpositiondepart or place[3]==lpositiondepart) and arrivee!=nposition :
            '''affiche le cadre de félicitation'''
            findujeu3.afficherfelicitation()
            scores[parties][1].config(text=str(n))
            scores[parties][2].config(text=str(coup))
            parties+=1
            coup=0
            points2.point_label2.config(text=str(coup))
            points3.point_label2.config(text=str(coup))
            arrivee=nposition
        
        
fonctionssouris=[drag_start,drag_motion,drag_drop]   
position=0 
#mise en place de l'arriere plan du mode jeu avec souris
arriereplan3 = Canvas(fen, width=1300, height=750, background='white')
arriereplan3.create_image( 0, 0, image = image2, anchor = "nw")
#création de la boite pour demander le nombre de disque
boite3=Boite(arriereplan3,nombre,creationdisque,True,fen)
boite2.initialisation(arriereplan2,arriereplan3,fonctionssouris)
boite3.initialisation(arriereplan2,arriereplan3,fonctionssouris)
#mise en place du bouton pour sortir du mode de résolution
sortie3=Sortir(arriereplan3, arriereplan, lpositiondepart)
sortie3.initialisation(fen)
sortie3.initialisation3(boite3,porter)
#mise en place du bouton parametre pour changer le nombre de disque
parametre_bouton3=Button(fen,text="Parametre", font="Calibri 15",bg='white', command=parametre3)
parametre_bouton3.pack()
parametre_canevas3=arriereplan3.create_window(1150,10,window=parametre_bouton3,  anchor = "nw",)
points3=Comptagepoint(arriereplan3, coup)
findujeu3=Felicitation(arriereplan3)
#consignes pour jouer
conseilT3="""Déplacer les disques en 
utilisant la souris"""
conseil3=Label(fen,bg="white", text=conseilT3,font="Calibri 15")
conseil3.pack()
conseil3_canevas=arriereplan3.create_window(850, 65, window=conseil3,anchor=SW)

#lance le programme
fen.mainloop()