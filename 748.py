class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        word_map = {}
        for ch in licensePlate:

            if ch.isalpha() and ch.lower() not in word_map:  
                word_map[ch.lower()] = 1
            elif ch.isalpha():
                word_map[ch.lower()] += 1

        word_len = 100000
        output_word = ""
        result = []
        for word in words:
            flag = True
            
            for key , val in word_map.items():
                if (key not in word) or ( word.count(key) < val):
                    flag = False
                    break
            if flag and len(word) < word_len:
                word_len = len(word)
                output_word = word
                
        
        return output_word


        

        