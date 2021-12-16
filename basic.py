
f = input("Enter the coefficients for each power: ").split(" ")

a = int(input("Enter a lower bound: "))
b = int(input("Enter an upper bound: "))

n = int(input("Enter the amount of squares to approximate: "))

approx = 0
curr = a
intX = (b-a)/n

# summations
for i in range(n):

    temp = 0

    # find f(xi)
    for j in range(len(f)):
        temp += int(f[j])*pow(curr,len(f)-j-1)

    approx += temp*intX

    curr += intX

print("The approx sum with %d squares is: %s"%(n,str(approx)))