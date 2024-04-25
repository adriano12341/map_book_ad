from models.data_source import users
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user['name']} {user['surname']}')


lista_uzytkownikow(users)
