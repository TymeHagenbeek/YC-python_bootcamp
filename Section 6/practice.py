#Warmup
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    if a%2 == 1 or b%2 == 1:
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,5))

#Animal Crackers
def animal_crackers(a):
    x = a.split()
    letter_1 = x[0][0]
    letter_2 = x[1][0]
    if letter_1 == letter_2:
        return True
    else:
        return False

print(animal_crackers('tyme tim'))

#Makes 20
def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False

print(makes_twenty(10,21))

#Level 1
#MacDonald
def old_macdonald(name):
    list1 = []
    list1[:0] = name
    list1[0] = list1[0].upper()
    list1[3] = list1[3].upper()
    list1 = ''.join(list1)
    return list1

print(old_macdonald('macdonald'))

#Master Yoda
def master_yoda(a):
    a= a.split()
    a.reverse()
    a = ' '.join(a)
    return a

print(master_yoda('I am ready'))

#Almost there
def almost_there(n):
    if n >= 90 and n <= 110 or n >= 190 and n <= 210:
        return True
    else:
        return False

print(almost_there(90))

#has 33
def has_33(a):
    for i in range(0,len(a)-1):
        if a[i] == a[i+1]:
            return True
    return False

print(has_33([3, 1, 3, 1]))

#Paper doll
def paper_doll(text):
    list1 = []
    list2 = []
    list1[:0] = text
    for i in list1:
        list2.append(i*3)
    list2 = ''.join(list2)
    return list2

print(paper_doll('Mississippi'))

#Blackjack
def blackjack(x,y,z):
    totaal = x + y + z    
    if totaal <= 21:
        return totaal
    elif totaal > 21 and x==11 or y==11 or z==11:
        totaal = totaal - 11
        return totaal
    else:
        return 'BUST'

print(blackjack(9,9,11))

#summer of 69
def summer_of_69(*args):
    totaal = 0
    

print(summer_of_69([1, 3, 5]))


