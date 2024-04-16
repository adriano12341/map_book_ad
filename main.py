users: list=[

    {"name": "Julia", "surname": "Gotowiec", "posts":1500,},
    {"name": "Chubert", "surname": "Sybilski", "posts":1534,},
    {"name": "Adrian", "surname": "Dobrzański", "posts": 3,}

]

print("Informacje o twoich znajomych: ")
for user in users:
    print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]}')