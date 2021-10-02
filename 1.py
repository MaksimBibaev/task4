name=input("Введите имя студента:")
surname=input("Введите фамилию студента:")
date=int(input("Введите год рождения:"))
print(name,"_",surname,"_",date)
D=name
name=surname
surname=D
date+=60
print(name,"_",surname,"_",date)
