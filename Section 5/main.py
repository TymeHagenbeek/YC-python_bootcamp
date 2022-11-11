if 3 > 2:
    print('its true!')

hungry = True

if hungry:
    print('feed me')
else:
    print('im not hungry')

loc = "bank"

if loc == "Auto shop":
    print('cars are cool')
elif loc == "bank":
    print("money is cool")
else:
    print("idk")


mylist = [1,2,3,4,5,6,7,8,9]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(num)

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

mystring = "Hello World"
for letter in mystring:
    print(letter)

mylist2 = ([1,2],[3,4],[5,6],[7,8])
for i in mylist2:
    for x in i:
        print(x)

for a,b in mylist2:
    print(a)

d = {'k1':1, 'k2': 2, 'k3': 3}
for key, value in d:
    print(value)

x = 0
while x < 5:
    print(x)
    if x == 2:
        break
    x=x + 1

mystring = 'tyme'
for letter in mystring:
    if letter == "y":
        continue
    print((letter))


for num in range(0,10,2):
    print(num)

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

word = 'ebcde'
for item in enumerate(word):
    print(item)



