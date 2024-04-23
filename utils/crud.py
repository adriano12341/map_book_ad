def add_user(lista:list)->None:
    imie=input("Podaj imię: ")
    nazwisko=input("Podaj nazwisko: ")
    liczba_postow=int(input("Podaj liczbę postów użytkownika: "))
    nazwa_miejscowosci=input("Podaj nazwę miejscowosci: ")
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, 'location': nazwa_miejscowosci }
    lista.append(new_user)
def read_friends(users: list)->None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} posty.')

def search_user(users: list)->dict:
    user_name=input("Podaj imię: ")
    for user in users:
        if user["name"] == user_name:
            print(user)
            return user

def remove_user(users: list):
    user_name=input("Podaj imię: ")
    for user in users:
        if user["name"] == user_name:
            users.remove(user)