spisok = list(input("Введите значения в список: "));
print(spisok);
result=list(spisok);
i=0;
if len(spisok)%2==0:
    while i<len(spisok):
        result[i]=spisok[i+1]
        result[i+1]=spisok[i]
        i+=2;
    print(result);
elif len(spisok)%2==1:
    while i<len(spisok)-1:
        result[i] = spisok[i + 1]
        result[i + 1] = spisok[i]
        i += 2;
    result[len(spisok)-1]=spisok[len(spisok)-1];
    print(result);