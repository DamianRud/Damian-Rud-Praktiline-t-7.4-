import os
import glob
from datetime import datetime
from analuusaator import*

#  Показываем текущую папку проекта
print("Projekti kaust:", os.getcwd()) # os.getcwd полный путь к текущей рабочей директории

# Смотрим какие расширения файлов есть в папке
koik_failid = glob.glob("*.*")  # ищем все файлы
laiendid = []

for fail in koik_failid:
    osad = fail.split(".")  # разбиваем имя файла по точке
    if len(osad) > 1:
        if osad[-1] not in laiendid:  # если расширение ещё не добавлено
            laiendid.append(osad[-1])

print("Leitud faililaiendid:", laiendid)  # выводим найденные расширения

# -------- МЕНЮ --------
while True:
    print("--- MENÜÜ ---")
    print("1 - Täielik analüüs")           # Полный анализ
    print("2 - Salvesta raport faili")      # Сохранить отчёт
    print("3 - Kustuta vanad raportid")     # Удалить старые отчёты
    print("4 - Otsi faile algustähe järgi") # Поиск файлов по первой букве
    print("0 - Välju")                      # Выход

    valik = input("Sisesta valik: ")       # пользователь вводит выбор

    #  ПОЛНЫЙ АНАЛИЗ
    if valik == "1":
        try:  # добавляем проверку на ошибки
            laiend = input("Sisesta faililaiend (nt .py või .txt): ")
            failid = leia_projektifailid(laiend)  # ищем файлы с этим расширением

            if len(failid) == 0:  # если файлов нет
                print("Faile ei leitud.")
            else:
                for fail in failid:
                    print("\nAnalüüsitav fail:", fail)  # показываем имя файла
                    analuusi_faili_sisu(fail)         # анализируем файл
        except Exception as e:
            print("Faili analüüsimisel tekkis viga:", e)

    # СОХРАНЕНИЕ ОТЧЁТА
    elif valik == "2":
        try:
            loo_raporti_kataloog()  # создаём папку, если её нет
            nimi = "raport.txt"     # простое имя файла
            tee = os.path.join("Analüüsi_Raportid", nimi)  # путь к файлу

            fail = open(tee, "w", encoding="utf-8")  # открываем файл на запись
            fail.write("Raport loodud: " + str(datetime.now()) + "\n")  # дата и время
            fail.write("See on näidisraport.\n")  # пример текста отчёта
            fail.close()  # закрываем файл

            print("Aruanne salvestatud:", tee)
        except Exception as e:
            print("Aruande salvestamisel tekkis viga:", e)

    # УДАЛЕНИЕ СТАРЫХ ОТЧЁТОВ
    elif valik == "3":
        try:
            if os.path.exists("Analüüsi_Raportid"):  # проверяем, есть ли папка
                raportid = glob.glob("Analüüsi_Raportid/*.txt")  # ищем все отчёты
                for r in raportid:
                    os.remove(r)  # удаляем файл
                print("Kõik aruanded on kustutatud")
            else:
                print("Aruannete kaustu pole")
        except Exception as e:
            print("Aruannete kustutamisel tekkis viga:", e)

    # ПОИСК ФАЙЛОВ ПО ПЕРВОЙ БУКВЕ
    elif valik == "4":
        try:
            taht = input("Sisesta esimene täht: ")
            leitud = leia_failid_algustähe(taht)  # ищем файлы
            if len(leitud) == 0:
                print("Faile ei leitud.")
            else:
                print("Leitud failid:", leitud)
        except Exception as e:
            print("Failide otsimisel tekkis viga:", e)

    # ВЫХОД
    elif valik == "0":
        print("Programm on lõppenud.")
        break  # выходим из цикла

    else:
        print("Vale valik, proovi uuesti.")


