'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

'''

def romanToInt(s):
    mp = {}
    mp['I'] = 1
    mp['V'] = 5
    mp['X'] = 10
    mp['L'] = 50
    mp['C'] = 100
    mp['D'] = 500
    mp['M'] = 1000
    n = len(s)
    check = mp[s[0]]
    sum = 0
    sum1 = 0
    for i in range(len(s)-1):
        if mp[s[i]] <= check and mp[s[i]] >= mp[s[i+1]]:
            sum += mp[s[i]]
        elif mp[s[i]] > check:
            sum1 = mp[s[i]]-check
            sum += sum1
            
                
        check = mp[s[i]]
            
    if check < mp[s[n-1]]:
        sum1 = mp[s[n-1]] - check
        sum += sum1
    else:
        sum += mp[s[n-1]]
        
    return abs(sum)
    

print(romanToInt('XIV'))
