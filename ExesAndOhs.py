def xo(s):
    count0 = 0
    count1 = 0
    for x in s:
        if x == 'o' or x == 'O':
            count0 += 1
        elif x == 'x' or x == 'X':
            count1 += 1

    if count0 == count1:
        return True
    elif count0 != count1:
        return False
    return False


        
        

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

print(xo('ooxx'))

