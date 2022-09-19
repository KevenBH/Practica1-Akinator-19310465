from tkinter import Y
import sys

database = [
    {"name":"Nezuko", "human":False, "power":True, "hairlarge":True , "sing":False, "hairblack":True, "hat":False},

    {"name":"Megumin", "human":True, "power":True, "hairlarge":False , "sing":False, "hairblack":False, "hat":True},

    {"name":"Nico Yasawa", "human":True, "power":False, "hairlarge":True , "sing":True, "hairblack":False, "hat":False},

    {"name":"Rimuru", "human":False, "power":True, "hairlarge":False , "sing":False, "hairblack":True, "hat":False},
    
    {"name":"Nino", "human":True, "power":False, "hairlarge":False , "sing":False, "hairblack":False, "hat":False},
    
    {"name":"Hu Tao", "human":True, "power":True, "hairlarge":False , "sing":False, "hairblack":True, "hat":True},

    {"name":"Paimon", "human":False, "power":False, "hairlarge":False , "sing":False, "hairblack":False, "hat":False},

    {"name":"Hanamaru", "human":True, "power":False, "hairlarge":False , "sing":True, "hairblack":True, "hat":False},

    {"name":"Anya", "human":True, "power":True, "hairlarge":False , "sing":False, "hairblack":False, "hat":False},

    {"name":"Shiro", "human":True, "power":False, "hairlarge":False , "sing":False, "hairblack":True, "hat":False}
]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("Tu Mona China es "+database[0]["name"])
        print("Gracias Por Jugar")
        sys.exit(input())

        
    
ans = input("¿Tu Mona China es humana?(y,n)")
take_chance(ans, "human")

ans = input("¿Tu Mona China utiliza y/o tiene poderes?(y,n)")
take_chance(ans, "power")

ans = input("¿Tu Mona China tiene el cabello negro?(y,n)")
take_chance(ans,"hairlarge")

ans = input("¿Tu Mona China canta?(y,n)")
take_chance(ans,"sing")

ans = input("¿Tu Mona China tiene el cabello largo?(y,n)")
take_chance(ans,"hairblack")

ans = input("¿Tu Mona China lleva puesto un sombrero/gorra?(y,n)")
take_chance(ans,"hat")