def bon(w):
    w = str(w)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1,len(w)):
        if w[i] == w[i - 1] :
            num = int(alpha.find(w[i])) + 1
    return num*4

secretCode = input("Enter secret code : ")
print(bon(secretCode))
