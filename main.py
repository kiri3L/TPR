from Table import Table

"""
    С помощью ф-ии rite_criterions_to_file('input.txt')
    создай файл с input.txt
    в нем должны быть данные для перовй таблицы:
    имя критерия
    вес
    шкала
    код
    стремление 
    
    когда вводишь шкалы, нажми ENTER чтобы прекратить ввод
    
    обрати внимание: если стремление положительное, то самое лучшее значение имеет самый большой кол
                     если стремление отрицательное, то самое лучшее значение имеет самый маленький код!
                     
    формат файла
    
    название:вес:шкала1/шкала2/ ... /шкалаN:код1/код2/ ... /кодN:граница1/граница2/ ... /границаN-1:стремление
    
    Граница -- то место, где происходит переход межуд шкалами
    
    границ на 1 меньше чем шкал(кодов)
        
    Записывать критерии лучше по одному, чтобы не сбиться
    
    после того как все запишешь, закоментируй эту функцию и раскомкнтируй все остаьное    
"""

#write_criterions_to_file('input.txt')


"""
    основная лаба 
"""
# t = Table()
# t.read('input2.txt', 'input.txt')
# t.apply_rules()
# t.print_table()
# t.electre(1)
# flag = True
# try:
#     while float:
#         i = input('\n\nВведите С: ')
#         if i == "":
#             print('\n\nВсего доброго!')
#             break
#         t.electre(float(i))
# except:
#     print('\n\nВсего доброго!')


