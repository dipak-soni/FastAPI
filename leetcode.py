class Node:
    def __init__(self,number):
        self.number=number
        self.next=None
first_list=None
second_list=None

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

        