import sqlite3 as sql

def createDB():
    conn = sql.connect("monaschinas.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("monaschinas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE MONAS_CHINAS (
            name  text,
            human integer,
            power integer,
            hairl integer,
            sing  integer,
            hairb integer,
            hat   integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, human, power, hairl, sing, hairb, hat):
    conn = sql.connect("monaschinas.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MONAS_CHINAS VALUES ('{nombre}', {human}, {power}, {hairl}, {sing}, {hairb}, {hat})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


if __name__=="__main__":
    #createDB()
    #createTable()
    insertRow("Rimuru", False, True, True, False, False, False)

