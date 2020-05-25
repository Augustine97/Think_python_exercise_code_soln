"""Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc"""


def is_sorted(l):
    if sorted(l)==l:
        print('True')
    else:
        print('False')
        
 

if __name__=="__main__":
    l=[]
    for  i in range(int(input())):
        l.append(int(input()))
    is_sorted(l)
        