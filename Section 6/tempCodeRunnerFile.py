def summer_of_69(*args):
    totaal = 0
    for i in args:
        if i == 6:
            i += 1
            if i == 9:
                pass
        totaal = totaal + args[i]

print(summer_of_69([1, 3, 5]))