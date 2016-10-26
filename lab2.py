#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
users = ['admin', 'guest', 'user1', 'user2', 'user3']

matrix = [[[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]],
         [[0,0,0], [1,0,0], [0,0,0], [1,0,0], [0,0,0]],
         [[1,1,1], [1,1,0], [0,0,0], [1,1,0], [1,0,0]],
         [[1,1,0], [1,1,1], [1,1,0], [1,0,0], [1,1,1]],
         [[1,0,0], [0,0,0], [1,1,1], [1,1,1], [1,0,0]]]

while True :
    name = input('Введите имя пользователя ')
    if name == 'quit' : break   
    if name in users :
        ind = users.index(name)
        print (name, ' перечень Ваших прав:')
        for i in range(5) :
            print ('Объект ', i, end='')
            if matrix [ind][i] == [1, 1, 1] : print (' Полный доступ', end='')
            elif matrix [ind][i] == [0, 0, 0] : print (' Полный запрет', end='')
            else :
                if matrix [ind][i][0] == 1 : print (' Чтение ', end='')
                if matrix [ind][i][1] == 1 : print ('Запись ', end='')
                if matrix [ind][i][2] == 1 : print ('Передача прав', end='')
            print ('')
        while True :    
            inp = input ('> ')
            if inp == 'quit' : break
            instr = inp.split(' ')
            func = instr [0]
            if ((len(instr) == 2) and (func != 'grant')  or ((len(instr) == 4) and (func == 'grant'))) :
                try :
                    arg = int(instr[1])
                    if (0 <= arg <= 4) :
                        if func == 'read' :
                            if matrix [ind][arg][0] == 1 : print ('Операция прошла успешно')
                            else : print ('У Вас нет прав для осуществления операции')
                        elif func == 'write' :
                            if matrix [ind][arg][1] == 1 : print ('Операция прошла успешно')
                            else : print ('У Вас нет прав для осуществления операции')
                        elif func == 'grant' :
                            priem = instr[2]
                            if instr[3] == 'read' : prav = 0
                            elif instr[3] == 'write' : prav = 1
                            elif instr[3] == 'grant' : prav = 2
                            else :
                                print ('Не верно указаны права')
                                continue
                            if matrix [ind][arg][2] == 1 :
                                if priem in users :
                                    ind2 = users.index(priem)                       
                                    if matrix [ind][arg][prav] == 1 :
                                        matrix [ind2][arg][prav] = 1
                                        print ('Операция прошла успешно')
                                    else : print ('Вы не можете передавать право, которого у Вас нет')
                                else : print ('Пользователь не найден')
                            else : print ('У Вас нет прав для осуществления операции')
                        else : print ('Нет такой операции')
                    else : print ('Нет такого объекта')
                except ValueError : print ('Неправильный параметр команды')
            else : print ('Не правильный формат команды')
    else : print ('Пользователь не найден')
