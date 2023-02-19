# Обработка ошибок

#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["hfsaa"]

#IndexError
# fruit_list = ["Apple", "Banana", "Kiwi"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# try:
#     # блок кода, который может иметь ошибку
# except:
#     # блок кода, который должен отработать,
#     # если ошибка нашлась
# else:
#     # если ошибок не было, то делай блок else
# finally:
#     # сделается в любом случае

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sajga"])
# except FileNotFoundError:
#     print("Здесь ошибка")
#     file = open("a_file.txt", "w")
#     file.write("парпаапа")
# except KeyError as error_msg:
#     print(f"Такого ключа {error_msg} не существует")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("Файл закрылся")
#     raise TypeError("Это ошибку создал я")
# raise Поднимать ошибку

######### ПРАКТИЧЕСКИЕ ПРИМЕРЫ #####

#BMI

# height = float(input("Рост: "))
# weight = int(input("Вес: "))
#
# if height > 3:
#     raise ValueError("Рост человека не может быть больше 3 метров")
#
# bmi = weight / height ** 2
# print(bmi)

####### ПРИМЕР 2 НА ОБРАБОТКУ ИСКЛЮЧЕНИЙ

fruits = ["Apple", "Orange", "Kiwi"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("pie")
#     else:
#         print(fruit + "pie")
#
# make_pie(1)

####### ЕЩЕ ОДИН ПРИМЕР НА ОБРАБОТКУ ИСКЛЮЧЕНИЙ (ОШИБОК)

vk_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 53, "Comments": 5, "Shares": 2},
    {"Likes": 10, "Comments": 5, "Shares": 1},
    {"Likes": 21, "Comments": 2},
    {"Comments": 5, "Shares": 10},
    {"Comments": 7, "Shares": 12},
]

total_likes = 0

for post in vk_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        pass

print(total_likes)