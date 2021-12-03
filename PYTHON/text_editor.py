# Simple Text editor with undo implemented with a stack

# key takeaways: before each operation, add existing string to undo stack
#               store inputs in list, pass to function for increased speed
#                a function is suffecient for this problem, class would be better for expansion

''' 
Sample Input
STDIN   Function
-----   --------
8       Q = 8
1 abc   ops[0] = '1 abc'
3 3     ops[1] = '3 3'
2 3     ...
1 xy
3 2
4 
4 
3 1
'''

def simple_text_editor(ops_list):
    s = ""
    actions = []
    
    for op in ops_list:
        op = op.split()
        
        # action 4: undo
        if len(op) == 1:
            s = actions.pop()
            continue
        
        # action 1: append
        if op[0] == '1':
            actions.append(s)
            s += op[1]
        # action 2: delete
        elif op[0] == '2':
            actions.append(s)
            s = s[:int(op[1]) * -1]
        # action 3: print
        elif op[0] == '3':
            print(s[int(op[1])-1])
        # invalid action
        else:
            raise ValueError("Invalid action number")


if __name__ == '__main__':
    # get input
    num_ops = input()
    ops_list = []
    for row in range(int(num_ops)):
        ops_list.append(input())

    # run function
    simple_text_editor(ops_list)
    

