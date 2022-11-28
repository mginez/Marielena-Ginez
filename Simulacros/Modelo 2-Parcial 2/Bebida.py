class Bebida:
    def __init__(self, id, nombre, precio, es_alcoholica):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.es_alcoholica = es_alcoholica

    def mostrar_bebida(self):
        print(f'''
        {self.id} - {self.nombre} - {self.precio}$''') 