from Empleado import Empleado, Ingeniero, Arquitecto, Obrero

def imprimir_factura(self, descuento, recarga, total):
    Empleado.mostrar_empleado(self)
    print(f'''
    Monto: {self.monto}
    Descuento: {descuento}
    Recarga: {recarga}
    TOTAL: {total}
    ''')

def main():
    option = ''
    monto_total = 0
    cantidad_ingenieros = 0
    cantidad_arquitectos = 0
    cantidad_obreros = 0
    pago_ingenieros = 0
    pago_arquitectos = 0
    pago_obreros = 0
    mayor_ingenieros = [0, '']
    mayor_arquitectos = [0, '']
    mayor_obreros = [0, '']

    while option != '3':

        option = input('''
            Bienvenido.
            Escoja una opcion.
            1. Registrar un empleado.
            2. Ver las estadisticas del final del dia.
            3. Salir
            -> ''')

        if option == '1':
            cargo = input('''
            Escoja el cargo del empleado.
            1. Ingeniero.
            2. Arquitecto.
            3. Obrero.
            -> ''')
            if cargo == '1':
                tipo = {'1': 'Civil', '2':'Electricista'}
                key = input('''
            Civil o Electricista.
            1. Civil.
            2. Electricista.
            -> ''')
                ingeniero = Ingeniero(
                    input('Nombre: '),
                    input('ID: '),
                    input('Mes: '),
                    int(input('Horas: ')),
                    'Ingeniero',
                    tipo[key]
                )
                descuento = Ingeniero.obtener_descuento(ingeniero)
                recarga = Ingeniero.obtener_recarga(ingeniero)
                total = ingeniero.monto - descuento + recarga
                monto_total += total
                pago_ingenieros += total
                cantidad_ingenieros += 1
                imprimir_factura(ingeniero, descuento, recarga, total)
                if total > mayor_ingenieros[0]:
                    mayor_ingenieros[0] = total
                    mayor_ingenieros[1] = ingeniero.id
                    
    

            elif cargo == '2':
                tipo = {'1': 'Exterior', '2':'Interior'}
                key = input('''
            Exterior o Interior.
            1. Exterior.
            2. Interior.
            -> ''')
                arquitecto = Arquitecto(
                    input('Nombre: '),
                    input('ID: '),
                    input('Mes: '),
                    int(input('Horas: ')),
                    'Arquitecto',
                    tipo[key]
                )
                descuento = Arquitecto.obtener_descuento(arquitecto)
                recarga = Arquitecto.obtener_recarga(arquitecto)
                total = arquitecto.monto - descuento + recarga
                monto_total += total
                pago_arquitectos += total
                cantidad_arquitectos += 1
                imprimir_factura(arquitecto, descuento, recarga, total)
                if total > mayor_arquitectos[0]:
                    mayor_arquitectos[0] = total
                    mayor_arquitectos[1] = arquitecto.id

            elif cargo == '3':
                tipo = {'1': 'Capataz', '2':'Novato'}
                key = input('''
            Capataz o Novato.
            1. Capataz.
            2. Novato.
            -> ''')
                obrero = Obrero(
                    input('Nombre: '),
                    input('ID: '),
                    input('Mes: '),
                    int(input('Horas: ')),
                    'Obrero',
                    tipo[key]
                )
                descuento = Obrero.obtener_descuento(obrero)
                recarga = Obrero.obtener_recarga(obrero)
                total = obrero.monto - descuento + recarga
                monto_total += total
                pago_obreros += total
                cantidad_obreros += 1
                imprimir_factura(obrero, descuento, recarga, total)
                if total > mayor_obreros[0]:
                    mayor_obreros[0] = total
                    mayor_obreros[1] = obrero.id

        elif option == '2':

            try:
                promedio_ingenieros = pago_ingenieros/cantidad_arquitectos
            except:
                promedio_ingenieros = 0

            try:    
                promedio_arquitectos = pago_arquitectos/cantidad_arquitectos
            except:
                promedio_arquitectos = 0

            try:
                promedio_obreros = pago_obreros/cantidad_obreros
            except:
                promedio_obreros = 0

            print(f'''
            Monto total facturado: {monto_total}

            Cantidad de: 
            - Ingenieros: {cantidad_ingenieros}
            - Arquitectos: {cantidad_arquitectos}
            - Obreros: {cantidad_obreros}

            Promedio de pago:
            - Ingenieros: {promedio_ingenieros}
            - Arquitectos: {promedio_arquitectos}
            - Obreros: {promedio_obreros}

            Empleado mayor pagado:
            - Ingeniero: {mayor_ingenieros[1]}
            - Arquitecto: {mayor_arquitectos[1]}
            - Obrero: {mayor_obreros[1]}
            ''')

                

                
main()