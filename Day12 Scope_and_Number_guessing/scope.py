## Scope
enemies = 1
def increase_enemies():
    enemies
    print(f"enemies inside the function = {enemies}")
    return enemies +1

enemies = increase_enemies()
print(f"enemies outside the function = {enemies}")


# Local Scope

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()

# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strenght = 2
#         print(player_health)


## BlockScope
# game_level = 3
# enemies = ["Skeleton","Zombie","Alien"]
# if game_level < 5:
    
#     new_enemy = enemies[0]

# print(new_enemy)
        

