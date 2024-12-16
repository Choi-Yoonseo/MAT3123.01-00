class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        for words in words:
            s = words.lower()
            if(
                all(char in row1 for char in s)
                or all(char in row2 for char in s) 
                or all(char in row3 for char in s)
            ):

                ans.append(words)
        return ans