# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

with open('firms.txt', encoding='UTF-8') as firms_f:
    firms_list = [elem.rstrip('\n').split() for elem in firms_f.readlines()]

firms_dict = {}
av_profit_dict = {}

for elem in firms_list:
    firm_name, type_own, revenues, costs = elem
    profit = float(revenues) - float(costs)
    firms_dict[firm_name] = profit

av_profit_list = [firms_dict[elem] for elem in firms_dict if firms_dict[elem] >= 0]
av_profit_dict['average_profit'] = \
    round(sum(av_profit_list) / len(av_profit_list), 2) if len(av_profit_list) > 0 else None

result_list = [firms_dict, av_profit_dict]

with open('firms_profit.json', 'w', encoding='UTF-8') as firms_js:
    json.dump(result_list, firms_js)
