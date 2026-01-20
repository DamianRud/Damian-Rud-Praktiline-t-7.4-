#i = 0
#while i <7:
#   print(i)
#    i += 1







#number = 10
#while number > 0:
#    print(number)
#    number -= 1





#n = int(input("Enter a number N: "))

#summa = 0
#i = 0
#while i <n:
#    summa += i
#    i += 1
#    print(summa)











#i = 2
#while i <= 10:
#    print(i)
#    i += 2






#i=1
#while i <=5:
#print("3 *",i,"=",3*i)
#    i+=i







#number = 5
#while number > 0:
#    print(number)
#    number -=1
#print("Start")






#summa = 0
#i = 2
#while i <=10:
#    summa=summa+ i
#    i = i + 2
#print(summa)






#secret = 7
#guess = 0

#while guess != secret:
#    guess = int(input("Enter a number: "))
#    print("Wrong Answer")
#    if guess==secret:
#            print("Correct Answer")



#password = "12345"
#user=input("Введи пароль")
#while user !=password:
#    print("не правильно")
#   user= input("Попробуйте снова")
#print("Доступ разрешен")













#balance= 1000
#choice=0

#while choice!=4:
#    print("1.Проверить баланс")
#    print("2.Внести денги")
#    print("3.Снять наличные")
#    print("4.Выйти")

#    choice=input("Выберите действие")

#if choice==1:
#    print("Ваш баланс",balance)
#elif choice==2:
#    money=int(input("Сколько денег хотите положить"))
#    balance = balance + money
#    print("успешно")
#elif choice==3:
#    money=int(input("Сколько хотите снять"))
#    if money<=balance:
#        balance = balance-money
#        print("успешно")
#    else:
#        print("Недостаточна средств")
#elif choice==4:
#    print("Досвидания")
#else:
#    print("Не верный выбор")


#   print("Спасибо за использование")























print("========================================================")
print("         TERE TULEMAST SURMA AREENILE!")
print("========================================================")

# Fighters
names = ["SPARTAKUS", "KRIKS", "FLAMMA", "COMMODUS"]
hp_values = [100, 120, 90, 110]
stamina_values = [60, 40, 70, 50]

# Player choice
print("Vali oma võitleja:")
print("1 - SPARTAKUS")
print("2 - KRIKS")
print("3 - FLAMMA")
print("4 - COMMODUS")
player = int(input("Sinu valik (1-4): ")) - 1
print("Sa valisid:", names[player])

# Enemy choice
print("\nVali vastane:")
if player != 0: print("1 - SPARTAKUS")
if player != 1: print("2 - KRIKS")
if player != 2: print("3 - FLAMMA")
if player != 3: print("4 - COMMODUS")
enemy = int(input("Vastase valik (1-4): ")) - 1
print("Vastane on:", names[enemy])
print("========================================================")

# Game status
player_hp = hp_values[player]
enemy_hp = hp_values[enemy]
player_st = stamina_values[player]
enemy_st = stamina_values[enemy]

round_num = 1

# Main loop
while player_hp > 0 and enemy_hp > 0:
    print("\n[Voor", round_num, "]")
    print("Sina:", player_hp, "elu,", player_st, "vastupidavus")
    print("Vastane:", enemy_hp, "elu,", enemy_st, "vastupidavus")

    print("\nVali tegevus:")
    print("1 - Rünnak (-15 vastupidavust)")
    print("2 - Kaitse (-10 vastupidavust)")
    print("3 - Puhkus (+20 vastupidavust)")
    action = int(input("Sinu käik: "))

    # Player action
    player_damage = 0
    if action == 1 and player_st >= 15:
        player_damage = 10 + (round_num % 10)
        player_st = player_st - 15
        print("Sa ründad ja teed", player_damage, "kahju!")
    elif action == 2 and player_st >= 10:
        player_st = player_st - 10
        print("Sa kaitsed end!")
    elif action == 3:
        player_st = player_st + 20
        if player_st > stamina_values[player]:
            player_st = stamina_values[player]
        print("Sa puhkad ja taastad jõudu!")
    else:
        print("Sa oled liiga väsinud!")

    # Enemy action (simple pattern)
    if round_num % 3 == 0:
        enemy_action = 3
    elif round_num % 2 == 0:
        enemy_action = 1
    else:
        enemy_action = 2

    enemy_damage = 0
    if enemy_action == 1 and enemy_st >= 15:
        enemy_damage = 8 + (round_num % 7)
        enemy_st = enemy_st - 15
        print(names[enemy], "rünnak! Ta teeb", enemy_damage, "kahju!")
    elif enemy_action == 2 and enemy_st >= 10:
        enemy_st = enemy_st - 10
        print(names[enemy], "kaitseb end.")
    elif enemy_action == 3:
        enemy_st = enemy_st + 20
        if enemy_st > stamina_values[enemy]:
            enemy_st = stamina_values[enemy]
        print(names[enemy], "puhkab ja taastab jõudu.")
    else:
        print(names[enemy], "on liiga väsinud.")

    # Apply damage
    enemy_hp = enemy_hp - player_damage
    player_hp = player_hp - enemy_damage

    if enemy_hp < 0:
        enemy_hp = 0
    if player_hp < 0:
        player_hp = 0

    print("--------------------------------------------------------")
    print("Vooru lõpp:", names[player], "elud", player_hp, "|", names[enemy], "elud", enemy_hp)
    print("--------------------------------------------------------")

    round_num = round_num + 1

# End of game
print("\n========================================================")
if player_hp <= 0 and enemy_hp <= 0:
    print("Mõlemad kukuvad liivale! See on viik!")
elif enemy_hp <= 0:
    print(names[player], "võidab! Rahvas rõkkab rõõmust!")
else:
    print(names[enemy], "võidab! Publik karjub vere järele!")
print("========================================================")





