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
    print("Ekizde")

try:
    heroes = coleccionmongo.find()
    for hero in heroes:
        print(hero)
except Exception as e:
    print(f"No se pudo leer: {e}")

finally:
     if 'clienteconn' in locals():
          clienteconn.close()
          print("Chinguesumadre")