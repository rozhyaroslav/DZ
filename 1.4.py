n = input("Введите положительное число: ");
spisok = [n];
i=0;
maximum=0;
while i < len(n):
    if int(n[i])>maximum:
        maximum=int(n[i]);
    i=i+1;
print(maximum);