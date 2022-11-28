from funciones import numero_primo, numero_deficiente

class Empleado:
    def __init__(self, nombre, id, mes, horas, cargo, tipo):
        self.nombre = nombre
        self.id = id
        self.mes = mes
        self.horas = horas
        self.cargo = cargo
        self.tipo = tipo

    def mostrar_empleado(self):
        print(f'''
    Nombre: {self.nombre}
    ID: {self.id}
    Mes: {self.mes}
    Horas: {self.horas}
    Tipo: {self.tipo}
        ''')

class Ingeniero(Empleado):
    def __init__(self, nombre, id, mes, horas, cargo, tipo):
        super().__init__(nombre, id, mes, horas, cargo, tipo)
        self.tarifa = 25
        self.monto = 25*self.horas


    def obtener_descuento(self):
        if numero_primo(self.horas, self.horas-1):
            descuento = self.monto*0.15
            return descuento
        else: return 0

    def obtener_recarga(self):
        if numero_deficiente(self.monto, self.monto-1, 0):
            recarga = self.monto*0.10
            return recarga
        else: return 0

class Arquitecto(Empleado):
    def __init__(self, nombre, id, mes, horas, cargo, tipo):
        super().__init__(nombre, id, mes, horas, cargo, tipo)
        self.tarifa = 10
        self.monto = 10*self.horas


    def obtener_descuento(self):
        if numero_primo(self.horas, self.horas-1):
            descuento = self.monto*0.15
            return descuento
        else: return 0

    def obtener_recarga(self):
        if numero_deficiente(self.monto, self.monto-1, 0):
            recarga = self.recarga*0.10
            return recarga
        else: return 0

class Obrero(Empleado):
    def __init__(self, nombre, id, mes, horas, cargo, tipo):
        super().__init__(nombre, id, mes, horas, cargo, tipo)
        self.tarifa = 5
        self.monto = 5*self.horas


    def obtener_descuento(self):
        if numero_primo(self.horas, self.horas-1):
            descuento = self.monto*0.15
            return descuento
        else: return 0

    def obtener_recarga(self):
        if numero_deficiente(self.monto, self.monto-1, 0):
            recarga = self.recarga*0.10
            return recarga
        else: return 0
