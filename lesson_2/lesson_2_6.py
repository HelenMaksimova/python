# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# реализуем заполнение исходного списка goods со словарями через цикл while:

goods = []

goods_dict = {}  # промежуточный словарь для заполнения списка goods

confirm = True  # переменная для выполнения цикла или выхода из цикла

while confirm:
    # заполняем промежуточный словарь:
    try:
        goods_dict['название'] = input('\nВведите название товара: ')
        goods_dict['цена'] = float(input('Введите цену товара: '))
        goods_dict['количество'] = float(input('Введите количество товара: '))
        goods_dict['ед. измерения'] = input('Введите единицу измерения товара: ')
    except ValueError:
        print('Цена и количество должны быть числами!')
        continue
    # добавляем в список копию промежуточного словаря:
    goods.append(goods_dict.copy())
    user_confirm = input('\nВвести следующий товар? (да / любой символ): ')
    confirm = True if user_confirm == 'да' else False  # проверка условия выхода из цикла

# реализуем словарь с аналитикой:

# собираем в список ключи из элементов списка goods:
list_keys = sum([list(elem.keys()) for elem in goods], [])
list_keys = list(set(list_keys))  # убираем повторяющиеся значения

result_dict = {}  # итоговый словарь с аналитикой

# заполняем словарь с аналитикой по полученным ранее ключам:
for key in list_keys:
    result_list = [elem.get(key) for elem in goods]
    result_dict[key] = list(set(result_list.copy()))

# преобразуем список goods в нумерованный (например, начиная с 1) и выводим на экран структуру данных "Товары":
goods = list(enumerate(goods, 1))
print('\nИсходная структура данных "Товары":')

for elem in goods:
    print(elem)

# выводим на экран словарь с аналитикой:
print('\nСловарь с аналитикой:')

for key, elem in result_dict.items():
    print(f'{key}: {elem}')