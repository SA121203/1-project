# генераторы списков
# list = []
# for i in range (0, 100, 2):
    # list.append(i)

# print(list)

# list2 = [х for х in range(100)]
# print(list2)

# list = []
# for  i in range(1, 1000):
    # if i % 3 == 0:
        # list.append(i)

# print(list)

# list = [х for х in range(1, 100) if х % 3 == 0]
# print(list)

# list = []
# for i in range (-100, 50):
    # if i % 3 == 0 and i % 5 == 0:
        # pow (i, 3)
        # number = abs(i**3)
        # list.append(number)

# print(list)

#lists = [abs(pow(х, 3)) for х in range(-100, 50) if х % 3 == 0 and ]
#print(lists)

#def filter_list(range1, range2):
    #lists = [abs(pow(х, 3)) for х in range1, range2, ]


#kyal = {
    #'home': '2этаж',
    #'car': "BMW х7"
#}
#saykal = {
    #'home': '3этаж',
    #'car': "Toyota 470"
#}
#eldar = {
    #'hom': '6этаж',
    #'car': "Mers 222"
#}
#python_boot = [eldar, saykal, kyal]
#car = [х.get('car') for х in python_boot]
#print(car)

#python_boot = [eldar, saykal, kyal]
#home = list()
#for i in python_boot:
    #home.append(i.get('home'))

#print(home)

#from datetime import datetime

#def func1():
    #start = datetime.now()
    #lists = []
    #for i in range(1, 10000):
        #lists.append(i)
    #end = datetime.now() - start
    #print('Время для цикла for', end)
    #return lists

#def func2():
    #start = datetime.now()
    #lists = [х for х in range(1, 10000)]
    #end = datetime.now() - start
    #print('Время list comprehention', end)
    #return lists

#func1 ()
