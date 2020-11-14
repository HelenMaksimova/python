# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('poem.txt', encoding='UTF-8') as poem_f:
    poem_list = poem_f.readlines()
    str_count = len(poem_list)
    name = poem_f.name

print(*poem_list, sep='')

print(f'\nВсего в файле "{name}" строк: {str_count}')

for idx, elem in enumerate(poem_list, 1):
    print(f'В {idx}-й строке слов: {len(elem.split())}')
