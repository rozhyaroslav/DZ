i=0
informatic=0
physic=0
gym=0
# razdelen_spisok=str(str(vocabulary).split('(')).split(' ')
# print(razdelen_spisok)
with open ('5.6.txt','r',encoding='utf-8') as f_obj:
    while i<3:
        razdelen_spisok=list(f_obj.readline().split(' '))
        for el in list(razdelen_spisok):
            buffer=el.split('(')
            for el in buffer:
                if i==0:
                    try: informatic+=int(el)
                    except: continue
                if i==1:
                    try: physic+=int(el)
                    except: continue
                if i==2:
                    try: gym+=int(el)
                    except: continue
        i+=1
vocabulary={'Информатика':informatic, 'Физика':physic,'Физкультура':gym}
print(vocabulary)