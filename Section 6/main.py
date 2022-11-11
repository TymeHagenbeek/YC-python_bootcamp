from random import shuffle

def add_nums(num1,num2):
    return num1+num2

def is_even(number):
    result = number % 2 == 0
    return result

def is_even_list(num_list):
    for i in num_list:
        if i % 2 == 0:
            return True
        else:
            pass
    return False

def return_even_list(num_list):

    even_numbers = []

    for i in num_list:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            pass
    return even_numbers

def employee_check(work_hours):
    current_max =0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    
    return (employee_of_month, current_max)


work_hours = [('Abby',100),('Billy',1000),('Cassie',800)]
name,hours = employee_check(work_hours)
#print(name, hours)


mylist=[1,2,3,5]
#print(return_even_list(mylist))

#print(is_even(10))
#print(add_nums(2,5))

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick number between 0 and 2: ")
    return int(guess)

def check(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print('wrong guess')
        print(mylist)

mylist = [' ','O',' ']
shuffle_list(mylist)
guess = player_guess()
check(mylist, guess)

def myfunc(*args):
    return sum(args)
print(myfunc(10,20,30))

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit choice of is {}'.format(kwargs['fruit']))

myfunc2(fruit='apple')


def myfunc(a):
    mylist = []
    for i in range(0,len(a)):
        if i%2 != 0:
            upper = a[i].upper()
            mylist.append(upper)
        elif i%2 == 0:
            lower = a[i].lower()
            mylist.append(lower)
    x = ''.join(mylist)
    return x
print(myfunc('tyme'))



