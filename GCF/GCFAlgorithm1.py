
def gcd(a,b):

    fa = []

    for i in range(1,a+1):
        if (a%i) == 0:
            fa.append(i)   

    fb = []

    for j in range(1,b+1):
        if (b%j) == 0:
            fb.append(j)

    cf = []

    for f in fa:
        if f in fn:
            cf.append(f)

    return(cf[-1])

print "Enter Two Numbers to find their GCF:\n" 

num1 = int(raw_input("Number 1: "))
num2 = int(raw_input("Number 2: "))

print "\n"
print "GCF of " + str(num1) + " and " + str(num2) + " is " + str(gcd(num1,num2)) + "."

