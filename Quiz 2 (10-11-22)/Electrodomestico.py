#MARIELENA GINEZ NRO CARNET: 20221110395 mginez@correo.unimet.edu.ve

class Electrodomestico:
    def __init__(self, tipo, codigo_producto, precio, marca, color): #le puse un tipo jaja
        self.tipo = tipo
        self.codigo_producto = codigo_producto
        self.precio = precio
        self.marca = marca
        self.color = color

class Lavadora (Electrodomestico):
    def __init__(self, tipo, codigo_producto, precio, marca, color, capacidad):
        super().__init__(tipo, codigo_producto, precio, marca, color)
        self.capacidad = capacidad
    def obtener_lavadora(self):
        lavadora = [self.tipo, self.codigo_producto, self.precio, self.marca, self.color]
        return lavadora
    
class Microondas (Electrodomestico):
    def __init__(self, tipo, codigo_producto, precio, marca, color, control):
        super().__init__(tipo, codigo_producto, precio, marca, color)
        self.control = control
    def obtener_microondas(self):
        microondas = [self.tipo, self.codigo_producto, self.precio, self.marca, self.color, self.control]
        return microondas

class Nevera (Electrodomestico):
    def __init__(self, tipo, codigo_producto, precio, marca, color, inc_congelador, compartimientos):
        super().__init__(tipo, codigo_producto, precio, marca, color)
        self.inc_congelador = inc_congelador
        self.compartimientos = compartimientos
    def obtener_nevera(self):
        nevera = [self.tipo, self.codigo_producto, self.precio, self.marca, self.color, self.inc_congelador, self.compartimientos]
        return nevera

class Licuadora (Electrodomestico):
    def __init__(self, tipo, codigo_producto, precio, marca, color, material_vaso, velocidades):
        super().__init__(tipo, codigo_producto, precio, marca, color)
        self.material_vaso = material_vaso
        self.velocidades = velocidades
    def obtener_licuadora(self):
        licuadora = [self.tipo, self.codigo_producto, self.precio, self.marca, self.color, self.material_vaso, self.velocidades]
        return licuadora
    
