imie_1: str = "Julia"
imie_2: str = "Chubert"
imie_3: str = "Adrian"
imie_4: str = "Bartłomiej"
online_1: str = "online"
online_2: str = "offline"
online_3: str = "online"
online_4: str = "online"

users: list[str] = [imie_1, imie_2, imie_3, imie_4]
online: list[str] = [online_1, online_2, online_3, online_4]

print("Lista znajomych to: ")
for index, user in enumerate(users):
    print(f"\tTwój znajomy {user} jest {online[index]}")
