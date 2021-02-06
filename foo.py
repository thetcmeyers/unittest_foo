def cube(x):
    try:
        if x < 0:
            return
        b = x*x*x
        return round(b,3)
    except TypeError:
        return



def average(A):
    if len(A) == 0:
        return
    total = 0
    for e in A:
        total = total + e
    return total / len(A)

def name(f,l):
    try:
        r = f + " " + l
        return r
    except TypeError:
        return


##print(cube(3))

##print(average([1,2,3,7,8,9]))

##print(name("Tarren","Meyers"))
