import random
import time

# piedra papel o tijera
opciones = ("piedra", "papel", "tijera")
rounds = 1
comp_wins, user_wins, fin = 0, 0, False


def user_options():
    opcion = input("escoge piedra, papel o tijera ").lower()
    if not opcion in opciones:
        print("la opcion no es valida")
    return opcion


def comp_options():
    comp = random.choice(opciones)
    # genera opcion random de la tupla
    return comp


def iniciar_game(opcion, comp):
    if opcion in opciones:
        print("user = " + opcion)
        print("comp = " + comp)


def check_rules(opcion, comp):
    global user_wins, comp_wins
    if opcion == comp:
        print("empate")
    elif (
        (opcion == "tijera" and comp == "papel")
        or (opcion == "piedra" and comp == "tijera")
        or (opcion == "papel" and comp == "piedra")
    ):
        print("ganas")
        user_wins += 1
    else:
        print("pierdes")
        comp_wins += 1


def check_winner():
    global fin
    if comp_wins == 2:
        print("gana comp")
        fin = True
    elif user_wins == 2:
        print("gana user")
        fin = True


while fin == False:
    print("*" * 10)
    print("Round", rounds)
    print("*" * 10)
    print(comp_wins, user_wins)

    opcion, comp = user_options(), comp_options()

    iniciar_game(opcion, comp)
    check_rules(opcion, comp)
    check_winner()
    rounds += 1
    time.sleep(1)
