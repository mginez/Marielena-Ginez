#MARIELENA GINEZ NRO CARNET: 20221110395 mginez@correo.unimet.edu.ve

from Electrodomestico import Lavadora, Microondas, Nevera, Licuadora


def obtener_objetos(edd):
    objetos = []
    for key, value in edd.items():
        if key == 'washer': #codigo_producto, precio, marca, color, capacidad
            for item in value:
                electrodomestico = Lavadora('Lavadora', item['cod_p'], item['price'], item['brand'], item['color'], item['capacity'])
                objetos.append(electrodomestico)
        elif key == 'microwave': #codigo_producto, precio, marca, color, control
            for item in value:
                electrodomestico = Microondas('Microondas', item['cod_p'], item['price'], item['brand'], item['color'], item['digital'])
                objetos.append(electrodomestico)
        elif key == 'fridge': #codigo_producto, precio, marca, color, inc_congelador, compartimientos
            for item in value:
                electrodomestico = Nevera('Nevera', item['cod_p'], item['price'], item['brand'], item['color'], item['cooler'], item['comp'])
                objetos.append(electrodomestico)
        elif key == 'blender': #codigo_producto, precio, marca, color, material_vaso, velocidades
            for item in value:
                electrodomestico = Licuadora('Licuadora', item['cod_p'], item['price'], item['brand'], item['color'], item['cup'], item['speeds'])
                objetos.append(electrodomestico)
    return objetos

def print_inventario(objetos):
    for item in objetos:
        if item.tipo == 'Lavadora':
            key_list = ['Producto', 'Código de Producto', 'Precio', 'Marca', 'Color', 'Capacidad']
            posicion = objetos.index(item)
            lavadora = Lavadora.obtener_lavadora(objetos[posicion])
            count = 0
            for item in lavadora:
                print(f'{key_list[count]}: {item}')
                count = count + 1
            print('')

        elif item.tipo == 'Microondas':
            key_list = ['Producto', 'Código de Producto', 'Precio', 'Marca', 'Color', 'Es digital']
            posicion = objetos.index(item)
            microondas = Microondas.obtener_microondas(objetos[posicion])
            count = 0
            for item in microondas:
                print(f'{key_list[count]}: {item}')
                count = count + 1
            print('')

        elif item.tipo == 'Nevera':
            key_list = ['Producto', 'Código de Producto', 'Precio', 'Marca', 'Color', 'Incluye congelador', 'Compartimientos']
            posicion = objetos.index(item)
            nevera = Nevera.obtener_nevera(objetos[posicion])
            count = 0
            for item in nevera:
                print(f'{key_list[count]}: {item}')
                count = count + 1
            print('')
        
        elif item.tipo == 'Licuadora':
            key_list = ['Producto', 'Código de Producto', 'Precio', 'Marca', 'Color', 'Material del vaso', 'Velocidades']
            posicion = objetos.index(item)
            licuadora = Licuadora.obtener_licuadora(objetos[posicion])
            count = 0
            for item in licuadora:
                print(f'{key_list[count]}: {item}')
                count = count + 1
            print('')

def obtener_producto_costoso(objetos):
    maximo_precio = 0
    for item in objetos:
        if item.precio > maximo_precio:
            maximo_precio = item.precio
    for item in objetos:
        if item.precio == maximo_precio:
            return item


def main():

    option = ''
    is_valid = False
    edd = {
        "washer":
        [
            {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
            {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
        ],
        "microwave":
        [
            {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
            {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
        ],
        "fridge":
        [
            {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
            {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
        ],
        "blender":
        [
            {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
            {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
        ]
    }

    while option != '3':

        objetos = obtener_objetos(edd)
        option = input('¡Bienvenido a Electrodomésticos Ventas Naranja! Escoja una opción:\n1. Leer inventario\n2. Borrar un producto defectuoso\n3. Salir del sistema\n-> ')

        if option == '1':
            print('')
            print_inventario(objetos)
            producto_costoso = obtener_producto_costoso(objetos)
            print('El producto más costoso es: ', producto_costoso)


        if option == '2':
            defectuoso = input('\nPor favor ingrese el código del producto defectuoso:\n-> ')
            for item in objetos:
                if item.codigo_producto == defectuoso:
                    print(item.codigo_producto) #print de prueba
                    indice = objetos.index(item) #debería agarrar el indice para borrar el objeto que está en esa posición
                    objetos.pop(indice)
                    is_valid = True
                    print('\nProducto eliminado exitosamente.\n')
                    
            if is_valid == False:
                print('\nPor favor escoge una opción válida.\n')
            
            

        if option != '1' and option != '2' and option != '3':
            print('\nPor favor escoge una opción válida.\n')
                

            



main()