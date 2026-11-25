class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        words = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in words:
                words[key].append(word)

            else:
                words[key] = [word]
            
        return list(words.values())

