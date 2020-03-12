
def gcf(a,b):

    if a < b: # Assume a >= b
        (a,b) = (b,a)

    if (a%b) == 0:
        return(b)
    else:
        return(gcd(b,a%b)) # a % b < b, always!

print "Enter Two Numbers to find their GCF:\n" 

num1 = int(raw_input("Number 1: "))
num2 = int(raw_input("Number 2: "))

print "\n"
print "GCF of " + str(num1) + " and " + str(num2) + " is " + str(gcd(num1,num2)) + "."

