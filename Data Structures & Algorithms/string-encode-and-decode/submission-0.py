class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        new_char = 'T'
        new_str = 'M'
        char = ''
        for word in strs :
            for char in word :
                encoded_strs += str(ord(char) + 5) 
                encoded_strs += new_char
            encoded_strs += new_str
        
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        s = s.split("M")
        s.pop()
        string = ""
        strings = []
        for word in s :
            word = word.split("T")
            word.pop()
            for char in word :
                string += chr(int(char)-5)
            strings.append(string)
            string = ""
        
        return strings
        
    
        