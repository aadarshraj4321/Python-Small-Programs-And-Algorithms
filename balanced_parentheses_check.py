def parenthesis(s):
    
    if len(s)%2 !=0:
        return false

    opening = set("([{")
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])

    stack = []
    
    for paren in s:
        if paren in opening:
            stack.append(paren)
            print("Stack Appending")
            print(stack)
            print("---------------")
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()
            print("Stack Pop")
            print(last_open)
            print("-------")  
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


print(parenthesis("[{()}]"))
