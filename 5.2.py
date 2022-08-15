i=0
with open("5.2.txt", "r") as f_obj:
    for line in f_obj:
        slova=list(line.split(' '))
        i+=1
        print(f'В {i}-й строке {len(slova)} слов')
    print(f'Всего в файле {i} строк')