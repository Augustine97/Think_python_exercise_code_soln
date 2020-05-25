"""Exercise 6.7. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case. """

def is_power(a,b):
    if a%b==0 and a/b%b==0:
        print('True')
    else:
        print('False')
    
if __name__=='__main__':
    a=int(input())
    b=int(input())
    is_power(a,b)

        
    