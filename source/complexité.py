# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:39:27 2024

@author: merrinicolasdematons
"""
import matplotlib.pyplot as plt
#créer le graphique de la complexité de la tour de hanoï pour le mettre dans règles
fig=plt.figure()
xcomplex=[i for i in range(1,20)]
ycomplex=[2**j-1 for j in xcomplex]
plt.title("Complexité de la Tour de Hanoï")
plt.ylabel("nombre de coup")
plt.xlabel("nombre de disque")
plt.plot(xcomplex,ycomplex,"b-",label='Complexité')
plt.legend()
plt.show()
fig.savefig("données/schéma_complexité.png")