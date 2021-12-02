#Python linked list data structure

def mergeLists(head1, head2):
    #check null lists
    if not head1:
        return head2
    if not head2:
        return head1

    # select head
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    # keep original head, work from current
    c = head.next
    
    while head1 or head2:
        if not head1:
            c.next = head2
            break
        if not head2:
            c.next = head1
            break
        if head1.data <= head2.data:
            c.next = head1
            head1 = head1.next
        else:
            c.next = head2
            head2 = head2.next  
        c = c.next  
    return head