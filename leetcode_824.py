# daily challenge 


# i approached this by first determining an appropriate data structure, i though hashtable would be a good fit
# i then figured out a basic algorithm, in this case, getting the frequency of each letter in the string, and then comparing it to the ransom note.
# this passed all of the test cases, 45.18 faster runtime, 53.79% better mem usage. 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_table = {}
        
        # counting the frequency of chars in magazine string
        for i in magazine:
            if i not in magazine_table:
                magazine_table[i] = 1
            else:
                magazine_table[i] += 1
        
        # checking if ransom note can be constructed
        
        for j in ransomNote:
            if j in magazine_table:
                if magazine_table[j] == 1:
                    del magazine_table[j]
                else:
                    magazine_table[j] -= 1
            else:
                return False
        return True
