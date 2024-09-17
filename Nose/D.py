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
    nombre = input("Ingresa el nombre del heroe a borrar: ")
    resultado = coleccionmongo.delete_one({"nombre": nombre})
    if resultado.deleted_count > 0:
        print("Héroe borrado")
    else:
        print("No se encontró el heroe")
except Exception as e:
    print(f"No se pudo borrar: {e}")

finally:
     if 'clienteconn' in locals():
          clienteconn.close()
          print("Chinguesumadre")