st = 'Print only the words that start with an s in this sentence'
x = st.split()
for i in x:
    if i[0] == 's':
        print(i)

for i in range(0, 10 ,2):
    print(i)

mylist = []
for i in range(50):
    if i % 3 == 0:
        mylist.append(i)
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'
x = st.split()
for i in x:
    if len(i) % 2 == 0:
        print(i)

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

mylist2 = []
st = 'Create a list of the first letters of every word in this list'
x = st.split()
for i in x:
    mylist2.append(i[0])
print(mylist2)