# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

nums_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('english_nums.txt', encoding='UTF-8') as eng_nums_f:
    with open('russian_nums.txt', 'w', encoding='UTF-8') as rus_nums_f:
        for elem in eng_nums_f.readlines():
            new_str = ' '.join([nums_dict[el] if el in nums_dict else el for el in elem.split()])
            print(new_str, file=rus_nums_f)
