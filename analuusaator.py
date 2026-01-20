import glob  # модуль для поиска файлов по шаблону
import os    # модуль для работы с папками и файлами


#Открытие файла и просмотр доступных методов
f = open('rida.txt', 'r')  # открываем файл rida.txt на чтение
print(dir(f))               # выводим все методы и свойства объекта файла
f.close()                   # закрываем файл

#  Функция для поиска файлов по расширению
def leia_projektifailid(laiend, asukoht="."):
    # если пользователь не ввёл точку в расширении, добавляем её
    if not laiend.startswith("."):#startswith Проверяю начинается ли расширение с точки
        laiend = "." + laiend

    # спрашиваем у пользователя папку, где искать файлы
    asukoht = input("sisesta kataloogi asukoht (tühjaks jätmisel kasutatakse praegust asukohta):")
    if asukoht == "":          # если пользователь оставил пустое поле
        asukoht = "."          # используем текущую папку

    # создаём шаблон поиска папка + * + расширение
    muster = os.path.join(asukoht, "*" + laiend) # os.path.join правильного склеивания путей к файлам и папкам
    failid = glob.glob(muster)  # ищем все файлы по шаблону
    return failid               # возвращаем список найденных файлов

#  поиска файлов
failid1 = leia_projektifailid(".py")  # ищем все .py файлы
failid2 = leia_projektifailid(".txt", "Analüüsi_Raportid")  # ищем .txt в указанной папке
failid3 = leia_projektifailid("csv", "C:/kasutajad/Dekstop/Andmed")  # ищем .csv в указанной папке

# выводим найденные файлы
print("Leitud .py failid", failid1)
print("Leitud .txt failid Analüüsi_Raportid kaustas:", failid2)
print("Leitud .csv failid C:/kasutaja/Dekstop/Andmed kaustas:", failid3)

# Функция для создания папки отчётов
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):  # проверяем, существует ли папка
        os.mkdir(nimi)            # если нет, создаём папку
        return True               # возвращаем True, если создали
    return False                  # если папка уже была, возвращаем False

#  Функция для поиска файлов по первой букве
def leia_failid_algustähe(taht):
    # ищем все файлы, начинающиеся с буквы "taht"
    return glob.glob(taht + "*.*")

# Функция для анализа содержимого файла
def analuusi_faili_sisu(failitee):
    try:
        # открываем  файл для чтения
        fail = open(failitee, "r", encoding="utf-8")
        read = fail.readlines()   # читаем все строки в список
        fail.close()              # закрываем файл

        #  создаём счётчики
        ridade_arv = 0           # общее количество строк
        tyhjade_ridade_arv = 0   # количество пустых строк
        todo_fixme_arv = 0       # количество TODO и FIXME

        # проходим по каждой строке файла
        for rida in read:
            ridade_arv = ridade_arv + 1  # увеличиваем счётчик всех строк

            if rida.strip() == "":       #strip удаляет лишние символы в начале и в конце строки

                tyhjade_ridade_arv = tyhjade_ridade_arv + 1  # увеличиваем счётчик пустых

            # считаем количество TODO и FIXME в строке
            todo_fixme_arv = todo_fixme_arv + rida.count("TODO")
            todo_fixme_arv = todo_fixme_arv + rida.count("FIXME")

        # выводим результаты анализа
        print("Ridade arv:", ridade_arv)
        print("Tühjade ridade arv:", tyhjade_ridade_arv)
        print("TODO ja FIXME arv:", todo_fixme_arv)

    except FileNotFoundError:
        # если файл не найден, выводим сообщение
        print("Viga: fail ei leinud ", failitee)

    except Exception as e:
        # если возникла любая другая ошибка, выводим её
        print("Viga:", e)




