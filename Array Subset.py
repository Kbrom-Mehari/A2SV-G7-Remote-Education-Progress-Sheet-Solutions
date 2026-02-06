class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        frequency_a = {}
        for i in a:
            frequency_a[i] = frequency_a.get(i,0) + 1
        for j in b:
            if not j in frequency_a or frequency_a[j] < 1:
                return False
            else:
                frequency_a[j] = frequency_a.get(j) - 1
        return True
