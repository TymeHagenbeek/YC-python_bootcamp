#Exercise 1: Simple Arithmetic
print(1+3)
print(10-5)
print(2*2)
print(3**3)
print(10%3)

#Exercise 2: Quick print check
myString = "Hello-World"
print(myString)


#Exercise 3: String indexing
print(myString[2:5])

print(myString[::2])

print(myString[::-1])

print('Hello World'[8:9])
print('Hello World'[8])
print('Hello World'[0])

#exercise 4: String Slicing
print('tinker'[1:4])
#--

name = 'Sam'
lastName = name[1:]
print(lastName)

newName = 'P' + lastName
print(newName)


letter = 'z'
print(letter*10)

x = 'Hello World'
print(x.upper())
print(x.split())
print(x.split('o'))

mijnNaam = "Tyme"
print('Mijn naam is {}'.format(mijnNaam))
print(f'Mijn naam is {mijnNaam}')

print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result = 100/777
print(result)
print('The result was {r:1.5}'.format(r=result))

#Exercise 5: Print formatting
print('Python {}'.format('rules!'))
#--

list1 = [1,2,3]
list2 = [4,5,6]

print(list1[1:])

newlist = list1 + list2
print(newlist)

newlist[0] = 'EEN'
print(newlist)

newlist.append('Zes')
print(newlist)

print(newlist.pop())
print(newlist)

numlist = [9,8,5,7,2,3]
numlist.sort()
print(numlist)
numlist.reverse()
print(numlist)

#Exersize 6: Lists
newList = [1, 'two', 3.14159]
#--

my_dict = {'naam': 'Tyme', 'achternaam': 'Hagenbeek'}
print(my_dict['naam'])

my_dict2 = {'k1': '1', 'k2': [0,1,2,3], 'k3': {'insideKey': 'Hoi'}}
print(my_dict2)
print(my_dict2['k3']['insideKey'].upper())
print(my_dict2.keys())
print(my_dict2.items())

#Exercise 7: Dictonaries
#{"k1": 1, "K2": 2, "K3": 3}
mydict = {"k1": 1, "K2": 2, "K3": 3}
#--


t = ('a','a','b')
print(t.count('a'))


mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)

myList = [1,1,1,1,2]
print(set(myList))

myfile = open("test.txt",'r')
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
print(myfile.readlines())
myfile.close()

with open('test.txt', mode='a') as myfile:
    #contents = myfile.read()
    myfile.write('\nHEEY')

with open('test2.txt', mode ='w') as f:
    f.write('I created this file')

#Exercise 8: File I/O
x = open('test.txt', mode='w')
x.write('Hello World')
x.close()

