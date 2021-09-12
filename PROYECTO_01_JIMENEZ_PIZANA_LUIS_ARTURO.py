from os import system
from lifestore_file import *

# Lista con los datos de acceso de usuarios
# user_nickname, user_password, user_level, user_name
users = [["admin", "admin", 1, "Luis"], ["cliente", "cliente", 2, "Juan"]]


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-INIT -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#funcion que inicia el programa
def init_app():
    current_user = login()
    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-LOGIN-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#Inicio de sesion
def login():

    isLogin = False

    user_input = input("Escribe el nombre del usuario: ")
    pass_input = input("Escribe el usuario: ")

    for user in users:
        if (user[0] == user_input and user[1] == pass_input):
            print("Inicio de sesión correcto \n")
            isLogin = True
            return user

    while (isLogin == False):
        print("Los datos de inicio de sesión son incorrectos \n")
        user_input = input("Escribe el nombre del usuario: ")
        pass_input = input("Escribe el usuario: ")

        for user in users:
            if (user[0] == user_input and user[1] == pass_input):
                print("Inicio de sesión correcto \n")
                isLogin = True
                return user


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra el menu segun el user_level que tenga el usuario( admini o cliente )
def show_main_menu(current_user):
    if (current_user[2] == 1):
        show_main_manu_for_admin(current_user)

    elif (current_user[2] == 2):
        show_main_menu_for_client(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
## Muestra el menu para los administradores
def show_main_manu_for_admin(current_user):

    system("clear")

    print("BIENVENIDO ", current_user[3], "\n")
    print("Elige una opción ")
    print("""
    1._ Mostrar los 10 productos con más vendidos
    2._ Mostrar los 10 productos con menos vendidos
    3._ Mostrar los 10 productos con más busquedas
    4._ Mostrar los 10 productos con menos busquedas
    5._ Mostrar los 5 productos por categoría con más ventas
    6._ Mostrar los 5 productos por categoría con menos ventas
    7._ Mostrar los 5 productos por categoría con más busquedas
    8._ Mostrar los 5 productos por categoría con menos busquedas
    9._ Mostrar los 10 productos con mejor puntuación
    10._ Mostrar los 10 productos con peor puntuación
    11._ Mostrar el reporte de ventas
        """)

    opc = ""

    while opc != "salir" :

        opc = input(
            "Elige una opción o escribe \"salir\" para terminar la ejecución: "
        )

        if opc == "1":
            show_products_with_more_sales(current_user)
            break
        elif opc == "2":
            show_products_with_less_sales(current_user)
            break
        elif opc == "3":
            show_products_with_more_searches(current_user)
            break
        elif opc == "4":
            show_products_with_less_searches(current_user)
            break
        elif opc == "5":
            show_products_with_more_sales_by_category(current_user)
            break
        elif opc == "6":
            show_products_with_less_sales_by_category(current_user)
            break
        elif opc == "7":
            show_products_with_more_searches_by_category(current_user)
            break
        elif opc == "8":
            show_products_with_less_searches_by_category(current_user)
            break
        elif opc == "9":
            show_products_with_better_score(current_user)
            break
        elif opc == "10":
            show_products_with_worse_score(current_user)
            break
        elif opc == "11":
            show_sale_report(current_user)
            break
        elif opc == "salir" :
            print("Ejecución terminada")
            break
        else:
            print("ELige una opción correcta")


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
## muestrael menu para los clientes
def show_main_menu_for_client(current_user):
    system("clear")

    print("BIENVENIDO ", current_user[3], "\n")
    print("Elige una opción ")
    print("""
    1._ Mostrar los 10 productos con más vendidos
    2._ Mostrar los 10 productos con menos vendidos
    3._ Mostrar los 10 productos con más busquedas
    4._ Mostrar los 10 productos con menos busquedas
    5._ Mostrar los 5 productos por categoría con más ventas
    6._ Mostrar los 5 productos por categoría con menos ventas
    7._ Mostrar los 5 productos por categoría con más busquedas
    8._ Mostrar los 5 productos por categoría con menos busquedas
    9._ Mostrar los 10 productos con mejor puntuación
    10._ Mostrar los 10 productos con peor puntuación
        """)

    opc = ""

    while opc != "salir" :

        opc = input(
            "Elige una opción o escribe \"salir\" para terminar la ejecución: "
        )

        if opc == "1":
            show_products_with_more_sales(current_user)
            break
        elif opc == "2":
            show_products_with_less_sales(current_user)
            break
        elif opc == "3":
            show_products_with_more_searches(current_user)
            break
        elif opc == "4":
            show_products_with_less_searches(current_user)
            break
        elif opc == "5":
            show_products_with_more_sales_by_category(current_user)
            break
        elif opc == "6":
            show_products_with_less_sales_by_category(current_user)
            break
        elif opc == "7":
            show_products_with_more_searches_by_category(current_user)
            break
        elif opc == "8":
            show_products_with_less_searches_by_category(current_user)
            break
        elif opc == "9":
            show_products_with_better_score(current_user)
            break
        elif opc == "10":
            show_products_with_worse_score(current_user)
            break
        elif opc == "salir" :
            print("Ejecución terminada")
            break
        else:
            print("ELige una opción correcta")


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra los 10 articulos con mayores ventas
def show_products_with_more_sales(current_user):

    system("clear")

    list_sales_by_id_product = []

    print("LISTA DE LOS 10 PRODUCTOS MÁS VENDIDOS \n")

    list_sales_by_id_product = count_total_sales_by_id_product()

    #Ordena las ventas totales de mayor a menor
    #(Metodo Burbuja)
    for x in range(0, len(list_sales_by_id_product)):
        for i in range(x, len(list_sales_by_id_product)):
            if list_sales_by_id_product[x][1] < list_sales_by_id_product[i][1]:
                aux = list_sales_by_id_product[x]
                list_sales_by_id_product[x] = list_sales_by_id_product[i]
                list_sales_by_id_product[i] = aux

    # Muestra los 10 articulos con mayores ventas
    for x in range(0, 10):
        for product in lifestore_products:
            if list_sales_by_id_product[x][0] == product[0]:
                print(
                    str(x + 1) + "._ VENTAS (" +
                    str(list_sales_by_id_product[x][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Muestra los 10 articulos con menores ventas
def show_products_with_less_sales(current_user):

    system("clear")

    list_sales_by_id_product = []

    print("LISTA DE LOS 10 PRODUCTOS MENOS VENDIDOS \n")

    list_sales_by_id_product = count_total_sales_by_id_product()

    #Ordena las ventas totales de menor a mayor
    #(Metodo Burbuja)
    for x in range(0, len(list_sales_by_id_product)):
        for i in range(x, len(list_sales_by_id_product)):
            if list_sales_by_id_product[x][1] > list_sales_by_id_product[i][1]:
                aux = list_sales_by_id_product[x]
                list_sales_by_id_product[x] = list_sales_by_id_product[i]
                list_sales_by_id_product[i] = aux

    # Muestra los 10 articulos con menores ventas
    for x in range(0, 10):
        for product in lifestore_products:
            if list_sales_by_id_product[x][0] == product[0]:
                print(
                    str(x + 1) + "._ VENTAS (" +
                    str(list_sales_by_id_product[x][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Muestra los 10 articulos con mas busquedas
def show_products_with_more_searches(current_user):

    system("clear")

    list_searches_by_id_product = []

    print("LISTA DE LOS 10 PRODUCTOS MÁS BUSCADOS \n")

    list_searches_by_id_product = count_total_searches_by_id_product()

    # Ordena las busquedas totales de mayor a menor #######
    #(Metodo Burbuja)
    for x in range(0, len(list_searches_by_id_product)):
        for i in range(x, len(list_searches_by_id_product)):
            if list_searches_by_id_product[x][1] < list_searches_by_id_product[
                    i][1]:
                aux = list_searches_by_id_product[x]
                list_searches_by_id_product[x] = list_searches_by_id_product[i]
                list_searches_by_id_product[i] = aux

    #Muestra los 10 articulos con mas busquedas
    for x in range(0, 10):
        for product in lifestore_products:
            if list_searches_by_id_product[x][0] == product[0]:
                print(
                    str(x + 1) + "._ BUSQUEDAS (" +
                    str(list_searches_by_id_product[x][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Muestra los 10 productos con menos busquedas
def show_products_with_less_searches(current_user):

    system("clear")

    list_searches_by_id_product = []

    print("LISTA DE LOS 10 PRODUCTOS MENOS BUSCADOS \n")

    list_searches_by_id_product = count_total_searches_by_id_product()

    # Ordena las busquedas totales de menoor a mayor
    #(Metodo Burbuja)
    for x in range(0, len(list_searches_by_id_product)):
        for i in range(x, len(list_searches_by_id_product)):
            if list_searches_by_id_product[x][1] > list_searches_by_id_product[
                    i][1]:
                aux = list_searches_by_id_product[x]
                list_searches_by_id_product[x] = list_searches_by_id_product[i]
                list_searches_by_id_product[i] = aux

    # Muestra los 10 articulos on menos busquedas
    for x in range(0, 10):
        for product in lifestore_products:
            if list_searches_by_id_product[x][0] == product[0]:
                print(
                    str(x + 1) + "._ BUSQUEDAS (" +
                    str(list_searches_by_id_product[x][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                break 

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra 5 productos mas vendidos por categoria
def show_products_with_more_sales_by_category(current_user):
    system("clear")

    list_sales_by_id_product = []
    list_sales_by_category = []
    categories = []

    print("LISTA DE LOS 5 PRODUCTOS POR CATEGORÍA MAS VENDIDOS \n")

    list_sales_by_id_product = count_total_sales_by_id_product()

    categories = get_categories()

    list_sales_by_category = group_total_sales_by_category(
        categories, list_sales_by_id_product)

    #Ordena las ventas totales de mayor a menor
    #(Metodo Burbuja)
    for j in range(0, len(list_sales_by_category)):
        for x in range(1, len(list_sales_by_category[j])):
            for i in range(x, len(list_sales_by_category[j])):
                if list_sales_by_category[j][x][1] < list_sales_by_category[j][
                        i][1]:
                    aux = list_sales_by_category[j][x]
                    list_sales_by_category[j][x] = list_sales_by_category[j][i]
                    list_sales_by_category[j][i] = aux

    #imprime por los cinco productos mas vedidos por categoria
    for j in range(0, len(list_sales_by_category)):
        print("\n CATEGORIA: ", list_sales_by_category[j][0])
        if len(list_sales_by_category[j]) < 5:
            for i in range(1, len(list_sales_by_category[j])):
                for product in lifestore_products:
                    if list_sales_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ VENTAS (" +
                            str(list_sales_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break
        else:
            for i in range(1, 6):
                for product in lifestore_products:
                    if list_sales_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ VENTAS (" +
                            str(list_sales_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra los 5 productos por categoria menos vendidos
def show_products_with_less_sales_by_category(current_user):
    system("clear")

    list_sales_by_id_product = []
    list_sales_by_category = []
    categories = []

    print("LISTA DE LOS 5 PRODUCTOS POR CATEGORÍA MENOS VENDIDOS \n")

    list_sales_by_id_product = count_total_sales_by_id_product()

    categories = get_categories()

    list_sales_by_category = group_total_sales_by_category(
        categories, list_sales_by_id_product)

    # Ordena las ventas totales de menor a mayor
    #(Metodo Burbuja)
    for j in range(0, len(list_sales_by_category)):
        for x in range(1, len(list_sales_by_category[j])):
            for i in range(x, len(list_sales_by_category[j])):
                if list_sales_by_category[j][x][1] > list_sales_by_category[j][
                        i][1]:
                    aux = list_sales_by_category[j][x]
                    list_sales_by_category[j][x] = list_sales_by_category[j][i]
                    list_sales_by_category[j][i] = aux

    # imprime los cinco productos menos vedidos por categoria
    for j in range(0, len(list_sales_by_category)):
        print("\n CATEGORIA: ", list_sales_by_category[j][0])
        if len(list_sales_by_category[j]) < 5:
            for i in range(1, len(list_sales_by_category[j])):
                for product in lifestore_products:
                    if list_sales_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ VENTAS (" +
                            str(list_sales_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break
        else:
            for i in range(1, 6):
                for product in lifestore_products:
                    if list_sales_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ VENTAS (" +
                            str(list_sales_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra  los 5 productos por categoria mas buscados
def show_products_with_more_searches_by_category(current_user):
    system("clear")

    list_searches_by_id_product = []
    list_searches_by_category = []
    categories = []

    print("LISTA DE LOS 5 PRODUCTOS POR CATEGORÍA MAS BUSCADOS \n")

    list_searches_by_id_product = count_total_searches_by_id_product()

    categories = get_categories()

    list_searches_by_category = group_total_searches_by_category(
        categories, list_searches_by_id_product)

    #Ordena las busquedas totales de mayor a menor
    #(Metodo Burbuja)
    for j in range(0, len(list_searches_by_category)):
        for x in range(1, len(list_searches_by_category[j])):
            for i in range(x, len(list_searches_by_category[j])):
                if list_searches_by_category[j][x][
                        1] < list_searches_by_category[j][i][1]:
                    aux = list_searches_by_category[j][x]
                    list_searches_by_category[j][
                        x] = list_searches_by_category[j][i]
                    list_searches_by_category[j][i] = aux

    # imprime los cinco productos mas vedidos por categoria
    for j in range(0, len(list_searches_by_category)):
        print("\n CATEGORIA: ", list_searches_by_category[j][0])
        if len(list_searches_by_category[j]) < 5:
            for i in range(1, len(list_searches_by_category[j])):
                for product in lifestore_products:
                    if list_searches_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ BUSQUEDAS (" +
                            str(list_searches_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break
        else:
            for i in range(1, 6):
                for product in lifestore_products:
                    if list_searches_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ BUSQUEDAS (" +
                            str(list_searches_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#muestra los 5 productos por categoria con menos busquedas
def show_products_with_less_searches_by_category(current_user):
    system("clear")

    list_searches_by_id_product = []
    list_searches_by_category = []
    categories = []

    print("LISTA DE LOS 5 PRODUCTOS POR CATEGORÍA MENOS BUSCADOS \n")

    list_searches_by_id_product = count_total_searches_by_id_product()

    categories = get_categories()

    list_searches_by_category = group_total_searches_by_category(
        categories, list_searches_by_id_product)

    # Ordena las busquedas totales de menor a mayor
    #(Metodo Burbuja)
    for j in range(0, len(list_searches_by_category)):
        for x in range(1, len(list_searches_by_category[j])):
            for i in range(x, len(list_searches_by_category[j])):
                if list_searches_by_category[j][x][
                        1] > list_searches_by_category[j][i][1]:
                    aux = list_searches_by_category[j][x]
                    list_searches_by_category[j][
                        x] = list_searches_by_category[j][i]
                    list_searches_by_category[j][i] = aux

    # imprime por los cinco productos menos buscados por categoria
    for j in range(0, len(list_searches_by_category)):
        print("\n CATEGORIA: ", list_searches_by_category[j][0])
        if len(list_searches_by_category[j]) < 5:
            for i in range(1, len(list_searches_by_category[j])):
                for product in lifestore_products:
                    if list_searches_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ BUSQUEDAS (" +
                            str(list_searches_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break
        else:
            for i in range(1, 6):
                for product in lifestore_products:
                    if list_searches_by_category[j][i][0] == product[0]:
                        print(
                            str(i) + "._ BUSQUEDAS(" +
                            str(list_searches_by_category[j][i][1]) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
                        break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#contar el total de ventas por producto
def count_total_sales_by_id_product():

    # recorre lifestore_products y cuenta los
    # registros de ventas que se encuentran en la lifestores_sales
    # por cada id de productos y lo guarda en list_sales_by_id_product
    list_sales_by_id_product = []

    for product in lifestore_products:
        count = 0
        for sale in lifestore_sales:
            #valida si hay un registro de venta con ese id de producto y los contabiliza
            if sale[1] == product[0]:
                #valida que no sea una devolucion
                if sale[4] == 0:
                    count += 1
        list_sales_by_id_product.append([product[0], count])

    return list_sales_by_id_product


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#contar el total de busquedas por producto
def count_total_searches_by_id_product():

    # recorre lifestore_products y cuenta los
    # registros de busquedas que se encuentran en la lifestores_searches
    # por cada id de productos y lo guarda en list_sales_by_id_product
    list_searches_by_id_product = []

    for product in lifestore_products:
        count = 0
        for search in lifestore_searches:
            #valida si hay un registro de venta con ese id de producto y los contabiliza
            if search[1] == product[0]:
                count += 1
        list_searches_by_id_product.append([product[0], count])

    return list_searches_by_id_product


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#Agrupar el total de ventas por categoria
def group_total_sales_by_category(categories, list_sales_by_id_product):

    list_sales_by_category = []

    #agrupamos por categoria las ventas
    aux = 0
    for category in categories:
        list_sales_by_category.append([category])
        for total_sale in list_sales_by_id_product:
            for product in lifestore_products:
                if product[0] == total_sale[0] and product[3] == category:
                    list_sales_by_category[aux].append(total_sale)
        aux += 1

    return list_sales_by_category


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Agrupar el total de busquedas por categoria
def group_total_searches_by_category(categories, list_searches_by_id_product):

    list_searches_by_category = []

    #agrupamos por categoria las busquedas
    aux = 0
    for category in categories:
        list_searches_by_category.append([category])
        for total_search in list_searches_by_id_product:
            for product in lifestore_products:
                if product[0] == total_search[0] and product[3] == category:
                    list_searches_by_category[aux].append(total_search)
        aux += 1

    return list_searches_by_category


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#creamos lista por con las categorias que tienen los productos
def get_categories():
    categories = []

    for product in lifestore_products:
        if product[3] not in categories:
            categories.append(product[3])
    return categories


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-PARTE 2 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

def show_products_with_better_score(current_user) :
    system("clear")

    print("LISTA DE LOS 10 PRODUCTOS CON LAS MEJORES PUNTUACIONES \n")

    list_products_with_average_score = calc_average_score_by_product()

    #Ordena de mayor a menor score
    for x in range(0 , len(list_products_with_average_score)) : 
        for i in range( x , len(list_products_with_average_score)) :
            if list_products_with_average_score[x][1] < list_products_with_average_score[i][1] :
              aux = list_products_with_average_score[x]
              list_products_with_average_score[x] = list_products_with_average_score[i]
              list_products_with_average_score[i] = aux


    #Muestra los primeros 10 productos con el mejor score
    for i in range(0 , 10) :
      for product in lifestore_products :
        if product[0] == list_products_with_average_score[i][0] :
           print(str(i + 1) + "._ PROMEDIO SCORE(" + str(list_products_with_average_score[i][1]) + ") VENTAS("+ str(list_products_with_average_score[i][2] ) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
           break

    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
def show_products_with_worse_score (current_user) :

    system("clear")
    print("LISTA DE LOS 10 PRODUCTOS CON LAS PEORES PUNTUACIONES \n")

    list_products_with_average_score = calc_average_score_by_product()

    #Ordena de menor a mayor score
    for x in range(0 , len(list_products_with_average_score)) : 
        for i in range( x , len(list_products_with_average_score)) :
            if list_products_with_average_score[x][1] > list_products_with_average_score[i][1] :
              aux = list_products_with_average_score[x]
              list_products_with_average_score[x] = list_products_with_average_score[i]
              list_products_with_average_score[i] = aux

    #Muestra los primeros 10 productos con el peor score
    for i in range(0 , 10) :
      for product in lifestore_products :
        if product[0] == list_products_with_average_score[i][0] :
           print(str(i + 1) + "._ PROMEDIO SCORE(" + str(list_products_with_average_score[i][1]) + ") VENTAS("+ str( list_products_with_average_score[i][2] ) + ") -- stock (" + str(product[4]) + ") -- " + product[1])
           break
           
    opc = input("\n Regresar al menú principal, ingresa 1: ")

    while opc != "1":
        opc = input("\n Regresar al menú principal, ingresa 1: ")

    show_main_menu(current_user)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
def calc_average_score_by_product() :   

    list_products_with_average_score = []

    #Calcula el promedio de las puntuaciones de las ventas
    for product in lifestore_products : 
      count_sale = 0  
      total_score = 0
      for sale in lifestore_sales :
          if product[0] == sale[1] :
              total_score += sale[2]
              count_sale += 1 
      if total_score > 0 :
          list_products_with_average_score.append([product[0], total_score / count_sale, count_sale])
      else :
          list_products_with_average_score.append([product[0], 0, 0])


    return list_products_with_average_score

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+PARTE 3+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
def show_sale_report(current_user) :
        system("clear")
        
        months = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        months_names = [ "Enero", "Febrero", "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre", "Octubre" , "Noviembre" , "Diciembre"]
        lifestore_sales_ordened = []

        #agrupa las ventas por mes
        aux = 0
        for month in months :
            lifestore_sales_ordened.append([month])
            for sale in lifestore_sales :
            #valida que la venta sea en el mismo mes y que no sea 1 en refund
                if month == int(sale[3][3 : 5]) and int(sale[4]) == 0 : 
                   lifestore_sales_ordened[aux].append(sale)
            aux += 1

        
        #[month, total, sells]
        total_sales_by_month = []

        #calcula el total de ventas por mes
        for month_sales in lifestore_sales_ordened :
           total = 0
           count_sells = 0 
           for x in range(1 , len(month_sales)) :
               count_sells += 1 
               for product in lifestore_products :
                  if product[0] == month_sales[x][1] :
                      total +=  product[2]
           total_sales_by_month.append([month_sales[0] , total , count_sells])

        
        #####ORDENAR DE MENOR A MAYOR LAS VENTAS

        for x in range(0 ,len(total_sales_by_month)) :
           for i in range(x , len(total_sales_by_month)) :
                if total_sales_by_month[x][1] < total_sales_by_month[i][1] :
                    aux =  total_sales_by_month[x];
                    total_sales_by_month[x]  = total_sales_by_month[i]
                    total_sales_by_month[i]  = aux
          

          
        print("REPORTE DE VENTAS \n")

        print("VENTAS POR MES")
        
        total_sells = 0
        selled = 0 
         
        for month_sale in total_sales_by_month :
            print("\n" + months_names[month_sale[0] - 1] )
            print("Total de ventas: ", month_sale[2])
            print("Total de dinero : $ ", month_sale[1])
            total_sells += month_sale[2]
            selled += month_sale[1]

        print("\nVENTA ANUAL")
        print("Total de ventas anuales: ", total_sells)
        print("Total de dinero: $ ", selled)

        opc = input("\n Regresar al menú principal, ingresa 1: ")

        while opc != "1":
           opc = input("\n Regresar al menú principal, ingresa 1: ")

        show_main_menu(current_user)




