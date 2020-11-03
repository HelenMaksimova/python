# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Вариант с while:
user_answer = input("Введите число: ")

counter = 0
result = 0

while counter < len(user_answer):
    if int(result) < int(user_answer[counter]):
        result = user_answer[counter]
    counter += 1

print(f"В числе {user_answer} самая большая цифра {result}")


# Вариант с for и max()

user_answer = input("Введите число: ")

answer_spell = []

for i in user_answer:
    answer_spell.append(int(i))

result = max(answer_spell)

print(f"В числе {user_answer} самая большая цифра {result}")


# Вариант с list comprehension и max()

user_answer = input("Введите число: ")
result = max([int(elem) for elem in user_answer])
print(f"В числе {user_answer} самая большая цифра {result}")


# Вариант с list, map и max:

user_answer = input("Введите число: ")
result = max(map(int, list(user_answer)))
print(f"В числе {user_answer} самая большая цифра {result}")
