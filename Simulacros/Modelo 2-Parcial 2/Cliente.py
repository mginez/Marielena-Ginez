class Cliente:
    def __init__(self, nombre, id, edad):
        self.nombre = nombre
        self.id = id 
        self.edad = edad 
    def mostrar_cliente(self):
        print(f'''
    Nombre: {self.nombre}
    ID: {self.id}
    Edad: {self.edad}
        ''')