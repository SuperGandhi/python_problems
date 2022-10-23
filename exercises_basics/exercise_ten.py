class Prueba(object):

    def main(cls, args):

        kilometros = 0
        litros = 0
        kilometrosTotales = 0
        litrosTotales = 0
        promedio = 0

        while kilometros != -1:
            print ("Introduzca numero de kilometros en su viaje si desea\n" + "cancelar escriba -1")
            kilometros = ''
            kilometrosTotales += kilometros
            print("Introduzca numero de litros en su viaje")
            litros = ''
            litrosTotales += litros
            promedio = kilometros / litros
            print ("Los kilometros por litro de este viaje son:" + promedio)
        promedio = litrosTotales / kilometrosTotales
        print ("El promedio kilometros por litro es:" + promedio)


    if __name__ == '__main__':
        main()