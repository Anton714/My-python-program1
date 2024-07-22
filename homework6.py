my_dict={'Dima':1999,'Iren':2005,'Nik':1988}
print('Мой список:',my_dict)
print('Год рождения: ',my_dict.get('Iren'))
print(my_dict.get('Anton','Такого имени нет в списке.'))
my_dict.update({'Sasha':1987,'Lilu':2004,})
print('Удаленное значение:',my_dict.pop('Dima'))
print('Измененный список:',my_dict)
print(' ')

my_set={'Beef',123,234,'Rom',123,'Beef'}
print('My set:',my_set)
my_set.update({True,'Dell'})
my_set.discard(234)
print('My modified set:',my_set)