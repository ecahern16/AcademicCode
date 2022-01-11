
def exponent(a, n):
    #Base case
    if n == 1:
        return a
    #Recursive statement
    return a*(exponent(a, n-1))

def permutations(v):
    if len(v) == 0:
        return []
    
    if len(v) == 1:
        return [v]
    
    current = []
    for i in range(len(v)):
        item = v[i]
        newList = v[:i] + v[i+1:]
        
        for e in permutations(newList):
            current.append([item] + e)
            
    return current 
    
    

def palindrome(v):
    if len(v) == 1 or len(v) == 0: 
        return True
    if v[0] != v[-1]: 
        return False
    return palindrome(v[1:-1])

