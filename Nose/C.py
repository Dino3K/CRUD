import pymongo

try:
    clienteconn= pymongo.MongoClient("mongodb://localhost:27017")
    mongodb= clienteconn ["Demo1"]

    print("Entramos compadre")
except Exception as e:
    print("No mano se tosto {e}") 

try:
    coleccionmongo=mongodb["Nose"]
    print("Funco")
except Exception as e:

    print("No funco {e}")
try:
    count= int(input("sikas: "))
    for i in range(count):
         hero = {
              "nombre": input("Dijite el nombre del heroe: ")
         }
         insercion = coleccionmongo.insert_one(hero)
    print(f"valor insertado con esta madre ")
except Exception as e:
        print("Maliosal")

finally:
     if 'clienteconn' in locals():
          clienteconn.close()
          print("Chinguesumadre")