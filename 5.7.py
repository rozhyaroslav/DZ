import json
firms = {}
average_profit = 0
sum_profit = 0
counter_firm = 0
with open('5.7.txt','r',encoding='utf-8') as f_obj:
    for line in f_obj:
        buffer = line.split(' ')
        profit = int(buffer[2])-int(buffer[3])
        if profit >= 0:
            sum_profit += profit
            counter_firm += 1
        new_dict = {buffer[0]: profit}
        firms.update(new_dict)
    average_profit = sum_profit/counter_firm
    aver_prof = {'average_profit': average_profit}
    result = [firms, aver_prof]
    print(result)
    with open('5.7.json','w',encoding='utf-8') as js_obj:
        json.dump(result,js_obj)
