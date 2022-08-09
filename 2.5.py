my_list=input("Введите значения через пробел: ");
my_list=my_list.split(' ');
my_list=sorted(my_list, reverse=True);
new_list=[];
print(my_list);
is_update=False;
new_rate=int(input("Введите новую оценку: "));
i=0;
while i<len(my_list):
    if int(my_list[i]) < new_rate and is_update==False:
        new_list.append(new_rate);
# Добавляемая переменная типа int поможет проверить, добавляется ли новая переменная после дублирующихся
        is_update=True;
    new_list.append(my_list[i]);
    i+=1;
print(new_list);
