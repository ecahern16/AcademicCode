

def lists_a(lst):
    # lists_a: Swap the first and last elements of a list
    if len(lst):
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


def lists_b(lst):
    n = 0
    if len(lst):
        length = len(lst)
        last = [ lst[length - 1] ]
        beginning = lst[:length - 1]
        return last + beginning
    else:
        return lst


def lists_c(lst):
    # lists_c: Replace all even elements by 0 (all elements divisible by 2)
    n = 0
    if len(lst):
        while n < len(lst):
            if lst[n] % 2 == 0 :
                lst[n] = 0
            n = n + 1
    return lst
        

def lists_d(lst):
    # lists_d: Replace each element except the first and last by the larger of its two neighbors
    n = 1
    if len(lst):
        newlst = []
        newlst.append(lst[0])
        while n < len(lst) - 1:
            if lst[n-1] > lst[n+1]:
                newlst.append(lst[n-1])
            else :
                newlst.append(lst[n+1])
            n = n + 1
            
        newlst.append(lst[-1])
    return newlst


def lists_e(lst):
    # lists_e: Remove the middle element if the list length is odd, or the middle two elements if the length is even.
    if len(lst):
        x = len(lst) // 2
        if len(lst) % 2 == 0:
            del lst[(x-1):x+1]
        else :
            del lst[x]
    return lst
            


def lists_f(lst):
    # lists_f: Move all even elements to the front, otherwise preserving the order of the elements
    n = 0
    if len(lst):
        newlst = []
        while n < len(lst):
            if lst[n] % 2 == 0:
                newlst.append(lst[n])
                del lst[n]
            else:
                n = n + 1 
    return newlst + lst


def lists_g(lst):
    # lists_g: Return the second-largest element in the list
    if len(lst):
       largest = max(lst[0],lst[1])
       secondlargest = min(lst[0],lst[1])
       x = len(lst)
       for n in range(2,x):
           if lst[n]>largest:
               secondlargest=largest
               largest=lst[n]
           elif lst[n]>secondlargest and largest != lst[n]:
               secondlargest=lst[n]
       return secondlargest


def lists_h(lst):
    # lists_h: Return 1 if the list is currently sorted in increasing order, else -1
    if len(lst):
        n = 0
        while n < len(lst)-1:
            if lst[n] > lst[n+1]:
                return -1
            else :
                n = n + 1
        return 1


def lists_i(lst):
    # lists_i: Return 1 if the list contains two adjacent duplicate elements, else -1
     if len(lst):
        n = 0
        while n < len(lst)-1:
            if lst[n] == lst[n+1]:
                return 1
            else :
                n = n + 1
        return -1


def lists_j(lst):
    # lists_j: Return 1 if the list contains duplicate elements(need not be adjacent), else -1
    if len(lst):
        lst.sort()
        return lists_i(lst)


