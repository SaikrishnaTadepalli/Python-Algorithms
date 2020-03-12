
def gcd(a,b):

    i = min(a,b)

    while i>0:
        if (a%i) == 0 and (b%i) == 0:
            return(i)
        else:
            i = i -1

print "Enter Two Numbers to find their GCF:\n" 

num1 = int(raw_input("Number 1: "))
num2 = int(raw_input("Number 2: "))

print "\n"
print "GCF of " + str(num1) + " and " + str(num2) + " is " + str(gcd(num1,num2)) + "."