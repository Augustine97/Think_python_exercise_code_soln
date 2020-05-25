"""Exercise 6.8. The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd(a, b) = gcd(b,r). As a base case, we can use gcd(a, 0) = a. 
Write a function called gcd that takes parameters a and b and returns their greatest common divisor."""


def gcd(a,b):
    l=[]
    if a>b:
        t=a
    else:
        t=b
    for  i in range(1,t+1):
        if a%i==0 and b%i==0:
            l.append(i)
    print(max(l))
    
if __name__=='__main__':
    a=int(input())
    b=int(input())
    gcd(a,b)