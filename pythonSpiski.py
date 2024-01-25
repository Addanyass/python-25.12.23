# my_number = 0             распределяет  строки с числами
# my_list = [1,3,4,"text",7,6,5] распределяет строки со словами

# print(my_number)
# print(my_list)   
#-----------------------------------------------
#спискии распределение
# my_number = 0             
# my_list = [1,3,4,"text",7,6,5, my_number]
# print(my_list[0])
# print(my_list[-1])
# print(my_list[0:3])
#--------------------------------------------------

# my_number = 0             
# my_list = [1,3,4,"text",7,6,5, my_number]

# gen_list = [i for i in range(10)]
# print(gen_list)
#------------------------------------------------------

# определенное число между -10 и до 10 отработает 10 раз и выведет рандомно 
# from random import randint
# gen_list = [randint(-10,10) for _ in range(10)]
# print(gen_list)
#--------------------------------------------------------
# так же но уже с 0 до 100 и len отвечает за вывод всего любого текста который есть во всю длину на строке
# from random import randint
# gen_list = [randint(-10,10) for _ in range(10)]
# print(gen_list)

# print(len(gen_list))
# gen_list[0] = 100
# print(gen_list)
#---------------------------------------------------------------
# from random import randint
# gen_list = [randint(-10,10) for _ in range(10)]
# print(gen_list)

# print(len(gen_list))
# gen_list[0] = 100
# print(gen_list)
# gen_list.insert(2, 100) добавляет число 100 (то что хочешь добавить), по индексу 2 (то куда хочешь добавить)
#------------------------------------------------------------------
# from random import randint
# gen_list = [randint(-10,10) for _ in range(10)]
# print(gen_list)

# print(len(gen_list))
# gen_list[0] = 100
# print(gen_list)
# gen_list.insert(2, 100)
# print(gen_list)
# print(max(gen_list))
# print(120 in gen_list) #определяет правда это или нет , у меня меньше 120
# print(gen_list.index(100)) #определяет действительно ли первый элемент 100 