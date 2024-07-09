
#===========// 1 //===================================
immutable_var = 1, 2, 'string'
print(immutable_var)
print(type(immutable_var))#Проверяем тип

#immutable_var[0] = 3 // тип списка tuple неизменяем
#print(immutable_var)
#Возможно обращение только к элементам внутри списка:
immutable_var = [1, 2], 'True'
print(immutable_var)
immutable_var[0][1] = 3
print(immutable_var)


#===========// 2 //===================================
mutable_list = [1,2, 'string']
print(mutable_list)
mutable_list[2] = True
print(mutable_list)
mutable_list[0:2] = 3, False
print(mutable_list)
