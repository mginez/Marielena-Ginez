from Bebida import Bebida
from Cliente import Cliente
from funciones import fibonacci, numero_primo

def bebidas_iniciales():
    lista_bebidas = []
    bebida = Bebida('1','Coca-Cola',2,False)
    lista_bebidas.append(bebida)
    bebida = Bebida('2','Cerveza',1.5,True)
    lista_bebidas.append(bebida)
    bebida = Bebida('3','Red-Bull',3,False)
    lista_bebidas.append(bebida)
    return lista_bebidas

def mostrar_bebidas(lista_bebidas):
    print()
    for bebida in lista_bebidas:
        Bebida.mostrar_bebida(bebida)
    print()

def mostrar_bebidas_no_alcoholicas(lista_bebidas):
    print()
    for bebida in lista_bebidas:
        if not bebida.es_alcoholica:
            Bebida.mostrar_bebida(bebida)
    print()

def obtener_descuento(cliente, monto):
    descuento = 0
    if fibonacci(cliente.edad, 1, 1):
        descuento += (monto * 0.05)
    if numero_primo(monto, monto-1):
        descuento += (monto * 0.10)
    return descuento

def imprimir_factura(cliente, compra, monto, descuento, total):
    Cliente.mostrar_cliente(cliente)
    for bebida in compra:
        Bebida.mostrar_bebida(bebida)
    print(f'''
    Cantidad: {len(compra)}

    Monto: {monto}
    Descuento: {descuento}
    TOTAL: {total}
    ''')

def obtener_mas_vendida(lista_bebidas, lista_venta):
    max = 0
    max_nombre = ''
    for bebida in lista_bebidas:
        cant = lista_venta.count(bebida.id)
        if cant > max:
            max = cant
            max_nombre = bebida.nombre
    return max_nombre 



def main():
    cantidad_clientes = 0
    cant_alcoholicas = 0
    cant_no_alcoholicas = 0
    ventas_alcoholicas = []
    ventas_no_alcoholicas = []
    monto_total = 0
    promedio_compra = 0
    option = ''
    valid = False
    lista_bebidas = bebidas_iniciales()
    while option != '4':

            option = input('''
                Bienvenido.
                Escoja una opcion.
                1. Registrar una bebida.
                2. Hacer una compra.
                3. Mostrar estadisticas
                4. Salir
                -> ''')

            if option == '1':
                tipo = {'1':True, '2':False}
                key = input('''
                Es alcoholica:
                1. Si
                2. No
                -> ''')
                while not valid:
                    bebida = Bebida(
                    input('ID: '),
                    input('Nombre: '),
                    input('Precio: '),
                    tipo[key]
                    )
                    valid = True
                    for item in lista_bebidas:
                        if bebida.id == item.id:
                            print('\nPor favor intente con otro ID.\n')
                            valid = False
                            break
                valid = False
                lista_bebidas.append(bebida)     


            if option == '2':
                compra = []
                monto = 0
                cantidad = 0
                cliente = Cliente(
                    input('Nombre: '),
                    input('ID: '),
                    int(input('Edad: '))
                    )
                while True:
                    if cliente.edad >= 18:
                        mostrar_bebidas(lista_bebidas)
                    else:
                        mostrar_bebidas_no_alcoholicas(lista_bebidas)
                    while not valid:
                        seleccion = input('Introduzca el ID de la bebida: ')
                        for bebida in lista_bebidas:
                            if seleccion == bebida.id:
                                valid = True
                                monto += bebida.precio
                                compra.append(bebida)
                                if bebida.es_alcoholica:
                                    cant_alcoholicas += 1
                                    ventas_alcoholicas.append(bebida.id)
                                else:
                                    cant_no_alcoholicas += 1
                                    ventas_no_alcoholicas.append(bebida.id)
                                break
                        if not valid:
                            print('\nIntroduzca una opcion valida.')
                    valid = False
                    continuar = input('''
                    ¿Desea comprar otra bebida?
                    1. Si
                    2. No
                    -> ''')
                    if continuar == '2':
                        break

                descuento = obtener_descuento(cliente, monto)
                total = monto - descuento
                imprimir_factura(cliente, compra, monto, descuento, total)
                cantidad_clientes += 1
                monto_total += monto
            
            if option == '3':

                try:
                    promedio_compra = monto_total / cantidad_clientes
                except:
                    promedio_compra = 0

                max_alcoholica = obtener_mas_vendida(lista_bebidas, ventas_alcoholicas)
                max_no_alcoholica = obtener_mas_vendida(lista_bebidas, ventas_no_alcoholicas)

                print(f'''
            
            Cantidad de bebidas vendidas: 
            - Alcoholicas: {cant_alcoholicas}
            - No Alcoholicas: {cant_no_alcoholicas}

            Bebida mas vendida: 
            - Alcoholicas: {max_alcoholica}
            - No Alcoholicas: {max_no_alcoholica}

            Cantidad de clientes: {cantidad_clientes}

            Promedio de compra: {promedio_compra}
            ''')
                        

                    
main()