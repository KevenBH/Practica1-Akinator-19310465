from tkinter import Y
import sqlite3 as sql


def take_chance(answer, property):
    conn = sql.connect("monaschinas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM MONAS_CHINAS"
    cursor.execute(instruccion)
    datos= cursor.fetchall()
    conn.commit()

    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in datos:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        datos.remove(i)

    if len(datos) == 1:
        print("your character is "+datos[0]["name"])
        quit()
    
    conn.close()
    

ans = input("is your character human(y,n)")
take_chance(ans, "human")


ans = input("Is your character Youtuber(y,n)")
take_chance(ans, "youtuber")

ans = input("Is your character in a movie(y,n)")
take_chance(ans,"movie")

ans = input("Is your character original(y,n)")
take_chance(ans,"original")

ans = input("Is your character Inventor(y,n)")
take_chance(ans,"inventor")

ans = input("Is your character Indian(y,n)")
take_chance(ans,"indian")

