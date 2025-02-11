class Node:
    def __init__(self,number):
        self.number=number
        self.next=None
first_list=None
second_list=None
final_list=None

def insert(pointer, digit):   
    if pointer==None:
        pointer=Node(digit)
        pointer.next=None
    else:
        temp=pointer
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(digit)
    return pointer

def print_list(pointer):
    temp=pointer
    while temp!=None:
        print(temp.number,end=' ')
        temp=temp.next


l1=[2,4,3]
l2=[5,6,4]
# storing items to the first list
for x in l1:
    first_list=insert(first_list,x)

# storing items to the second list
for x in l2:
    second_list=insert(second_list,x)


print_list(first_list)
print()
print_list(second_list)

# get the numbers
def get_actual_number(pointer):
    number=0
    def internal_fun(pointer):
        nonlocal number
        if pointer.next==None:
            number=pointer.number
        else:
            internal_fun(pointer.next)
            number=number*10+pointer.number
        return number
    return internal_fun(pointer)


first_number=get_actual_number(first_list)
second_number=get_actual_number(second_list)
# print()
# print(first_number,second_number,sep=' ')
# print()

# addition 
final=first_number+second_number

# convert to list
l3=[int(x) for x in str(final)][::-1]
# print(l3)

# push to link list
for x in l3:
    final_list=insert(final_list,x)

# print linked list
print()
print('----------')
print_list(final_list)

#    3 4 2
#  + 4 6 5
# ------------
#    8 0 7 