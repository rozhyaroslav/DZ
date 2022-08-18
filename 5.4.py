i=1
result=[]
vocabulary={'One':'Один', 'Two':'Два','Three':'Три','Four':'Четыре'}
with open("5.4.1.txt", "r", encoding="utf-8") as f_obj:
    while i<5:
        buffer=list(f_obj.readline().split((' ')))
        buffer[0]=vocabulary.get(buffer[0])
        result+=(buffer)
        i+=1
    result = ' '.join(result)
    with open("5.4.2.txt", "w", encoding="utf-8") as f_obj_1:
        f_obj_1.write(result)


