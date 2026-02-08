'''
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = []
        carry = 0
        if len(a) < len(b):
            a,b = b,a
        blist = [int(i) for i in list(b[::-1])]
        alist = [int(i) for i in list(a[::-1])]
        for i in range(len(b)):
            t = blist[i] + alist[i] + carry
            if t == 0 or t == 1:
                c.append(t)
                carry = 0
            elif t == 2:
                c.append(0)
                carry = 1
            else:
                c.append(1)
                carry = 1

        for j in range(len(b),len(a)):
            t = alist[j] + carry
            if t == 0 or t == 1:
                c.append(t)
                carry = 0
            else:
                c.append(0)
                carry = 1
        if carry == 1:
            c.append(1)
        cc = [str(i) for i in c[::-1]]
        return ''.join(cc)


        
