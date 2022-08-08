time=int(input("Введите время в секундах: "));
hours=int(time/3600);
minutes=int(time%3600/60);
seconds=time%3600%60;
print("Ваше переведенное время в формате ЧЧ:MM:CC: ", hours, ":", minutes,":",seconds);
