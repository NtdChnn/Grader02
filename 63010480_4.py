def hbd(age):
    i = 2
    while True:
        age_ = 0
        a__ = age
        j = 0
        while True:
            age_ += (a__ % i) * (10 ** j)
            a__ = int(a__ / i)
            j += 1
            if a__ == 0:
                break
        if age_ == 20 or age_ == 21:
            break
        i += 1

    return f'saimai is just {age_}, in base {i}!'

year = input("Enter year : ")
print(hbd(int(year)))
