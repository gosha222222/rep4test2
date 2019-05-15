import random

def attack(u1, u2):
    u1["damage"] = random.randint(15, 35)
    u2["damage"] = random.randint(15, 35)
    armor(u1, u2)
    u1["health"] = u1["health"] - u2["damage"]
    u2["health"] = u2["health"] - u1["damage"]
    print(f'У игрока {u1["name"]} осталось {round(u1["health"], 2)} жизней')
    print(f'У игрока {u2["name"]} осталось {round(u2["health"], 2)} жизней\n')

def armor(u1, u2):
    u1["damage"] = u1["damage"] / u2["armor"]
    u2["damage"] = u2["damage"] / u1["armor"]
    return u1, u2

def write_to(player_dict):

    with open(f'{player_dict["name"]}.txt', 'w', encoding='utf-8') as file:
        for key, value in player_dict.items():
            if key == "armor":
                file.write(str(value))
            else:
                file.write(str(value) + '; ')

dmg1 = 10
dmg2 = 20

name1 = input("Игрок 1, введите имя своего персонажа\n")
name2 = input("Игрок 2, введите имя своего персонажа\n")

u1 = {"name":name1, "health":100, "damage":dmg1, "armor":1.2}
u2 = {"name":name2, "health":100, "damage":dmg2, "armor":1.2}

write_to(u1)
write_to(u2)
i = 0
while u1["health"] > 0 and u2["health"] > 0:
    i += 1
    attack(u1, u2)
