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
    nombre_viejo = input("Ingresa el nombre del heroe a actualizar: ")
    nombre_nuevo = input("Ingresa el nuevo nombre del heroe: ")
    resultado = coleccionmongo.update_one(
        {"nombre": nombre_viejo},
        {"$set": {"nombre": nombre_nuevo}}
    )
    if resultado.modified_count > 0:
        print("Héroe actualizado")
    else:
        print("No se encontró el héroe")
except Exception as e:
    print(f"No se pudo actualizar: {e}")

finally:
     if 'clienteconn' in locals():
          clienteconn.close()
          print("Chinguesumadre")
