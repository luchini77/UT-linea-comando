import sqlite3

def crearBBDD():
    conexion=sqlite3.connect("Ubicaciones Tecnicas.db")
    cursor=conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE ubicaciones(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       buzon VARCHAR(50) UNIQUE NOT NULL,
                       ubicacion VARCHAR(50) UNIQUE NOT NULL
        )''')
    except sqlite3.OperationalError:
        print("La tabla ya existe.")

    else:
        print("La tabla a sido creada correctamente")

    conexion.close()

def insertar():

    conexion=sqlite3.connect("Ubicaciones Tecnicas.db")
    cursor=conexion.cursor()

    buzon=input("Ingrese nuevo Buzón\n")
    ubicacion=input("Ingrese su ubicacion tecnica\n")

    try:

        cursor.execute("INSERT INTO ubicaciones VALUES (NULL, '{}', '{}')".format(buzon, ubicacion))
    except sqlite3.IntegrityError:
        print("El buzón '{}' ya existe.".format(buzon))
    else:
        print("Buzón '{}' creado correctamente.".format(buzon))

    conexion.commit()
    conexion.close()

def consultar():

    conexion=sqlite3.connect("Ubicaciones Tecnicas.db")
    cursor=conexion.cursor()

    buzon=input("Ingrese buzón a consultar?\n")

    bzn=cursor.execute("SELECT * FROM ubicaciones WHERE buzon='{}'".format(buzon)).fetchall()

    for b in bzn:
        print("\tBuzón {} \n\tUbicacion Tecnica {}".format(b[1],b[2]))


# crearBBDD()

while True:
    print("\nBienvenido al gestor de Ubicaciones Tecnicas")
    opcion=input("\nIntroduce una opcion:\n[1] Agregar buzon\n[2] Consultar buzon\n[3] Salir\n\n")

    if opcion == "1":
        insertar()
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        print("Nos vemos!!")
        break
    else:
        print("Opcion Incorrecta")
