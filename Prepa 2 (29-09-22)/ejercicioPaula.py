infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}

print("Bienvendio al sistema de transito")
option = ""
z = 1
i = 1
while option != "4":
    option = input("¿Qué deseas? Selecciona el número correspondiente.\n1. Registrar infractor\n2. Eliminar infractor\n3. Mostrar infractores\n4. Salir\n")
    if option == "1":
        print("Tipo de infracción")
        for num, type in infraction.items():
            for k, v in type.items():
                name = type.get("name")
                cost = type.get("cost")
            print(f"Infraction: {name}, Cost: {cost}")
        infraction1 = input("introduzca el costo infraccción correspondiente: ")
        if infraction1 == type.get("cost"):
            infraction1 = cost
            tipo = name
        print("Oficial que puso la multa")
        for key, value in officers.items():
            i = str(i)
            for k2, v2 in value.items():
                name2 = value.get("name")
                last_name = value.get("LastName")
                ci = value.get("ci")
            print(i + "." + f"Nombre del oficial: {name2}, Apellido del oficial: {cost}, Ci del oficial: {ci}")
            i = int(i)
            i+=1
        officer = input("introduzca el ci del oficial que le puso la multa: ").title()
        if officer == value.get("name"):
            officer = name2

        Registro = {"Nombre": input("Introduzca su nombre: "), "Cédula": input("Introduzca su cédula: "), "Infraccción": name, "CI del oficial": officer, "Monto a pagar": infraction1}
        db.update({z : Registro})
        print(db)
        z+=1
    if option == "2":
        for a, b in Registro.items():
            print(a, ": ", b)
        
    if option == "3":
        for a, b in Registro.items():
            print(a, ": ", b)