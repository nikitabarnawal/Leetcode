'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    minlen = len(strs[0])
    lcp = ''
    for i in range(len(strs)):
        minlen = min(minlen,len(strs[i]))
            
    i = 0
    while i < minlen:
        char = strs[0][i]
        for j in range(1,len(strs)):
            if char != strs[j][i]:
                return lcp
                    
        lcp = lcp + char
        i = i+1
    return lcp

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
