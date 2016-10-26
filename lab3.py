#!/usr/bin/env python3
# -*- coding: utf-8 -*-

users = ['admin', 'user1', 'user2', 'user3']
userLevel = [[3,3], [0,0], [1,1], [2,2]]
objects = [0,1,2,3]
A = ['NONCONFIDENTIAL', 'CONFIDENTIAL', 'SECRET', 'TOP_SECRET']

print ('OBJECTS:')
for i in range(4) : print('Object ', i, ' : ', A[objects[i]])
print ('SUBJECTS:')
for i in range(4) : print(users[i], ' : ', A[userLevel[i][0]])
while True :
    name = input('Введите имя пользователя: ')
    if name == 'quit' : break   
    if name in users :
        ind = users.index(name)
        while True :    
            inp = input('> ')
            if inp == 'quit' : break
            instr = inp.split(' ')
            if (len(instr) == 2) :
                func = instr[0]
                arg = instr[1]
                try :
                    if ((func == 'read') and (0 <= int(arg) <= 3)) :
                        if userLevel[ind][0] >= objects [int(arg)] : print ('Операция прошла успешно')
                        else : print ('У Вас нет доступа')
                    elif ((func == 'write') and (0 <= int(arg) <= 3)) :
                        if userLevel[ind][0] <= objects [int(arg)] : print ('Операция прошла успешно')
                        else : print ('У Вас нет доступа')
                    elif ((func == 'change') and (arg in A)) :
                        level = A.index(arg)
                        if userLevel[ind][1] >= level :
                            userLevel[ind][0] = level
                            print ('Операция прошла успешно')
                            print (users[ind], ' : ', A[userLevel[ind][0]])
                        else : print ('Вы не можете повысить уровень доступа')
                    else : print ('Неправильный параметр команды или нет команды')
                except ValueError : print ('Неправильный параметр команды')
            else : print ('Неправильный формат команды')
    else : print ('Пользователь не найден')
