# merge two sorted list
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def insert_node(value,pointer):
    if pointer==None:
        pointer=Node(value)
    else:
        temp=pointer
        while temp.next!=None:
             temp=temp.next
        temp.next=Node(value)
    return pointer

def show_nodes(pointer):
    if pointer==None:
        return None
    else:
        temp=pointer
        while temp!=None:
            print(temp.val,end=' ')
            temp=temp.next

def do_something(n,second_pointer):
    temp=second_pointer
    prev=second_pointer
    while temp.val<=n.val and temp:
        prev=temp
        temp=temp.next   # 1 3 4 7    1 
    
    if temp==second_pointer:
        return Node(n.val,temp)
    else:
        new=Node(n.val,prev.next)
        prev.next=new
        return second_pointer

    
        

def merge_sorted_list(first,second):
    temp1=first
    temp2=second
    if temp1==None:
        return second
    elif temp2==None:
        return first
    else:
        while temp1!=None:
            final=do_something(temp1,second)
            temp1=temp1.next
        return final

            
# first list
l1=[1]
l2=[1,3,4,7]
first=None
second=None
for x in l1:
    first=insert_node(x,first)
for x in l2:
    second=insert_node(x,second)

show_nodes(first)
print()
show_nodes(second)
print()
temp3=merge_sorted_list(first,second)
show_nodes(temp3)