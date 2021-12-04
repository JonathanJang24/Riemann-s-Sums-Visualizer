f = input("Enter the coefficients for each power: ").split(" ")

a = int(input("Enter a lower bound: "))
b = int(input("Enter an upper bound: "))

for k in range(1,10):
    intX = (b-a)/k
    curr = a
    approx = 0
    # summations
    for i in range(k):

        temp = 0

        # find f(xi)
        for j in range(len(f)):
            temp += int(f[j])*pow(curr,len(f)-j-1)

        approx += temp*intX

        curr += intX

    print("The approx sum with %d squares is: %s"%(k,str(approx)))