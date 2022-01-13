class Solution: 
    
    def __init__(self):
        self.i = 0

    def decodeString(self, s: str) -> str:
        
        ans = ""

        while self.i < len(s) and s[self.i] != "]":
            
            if not s[self.i].isdigit():
                ans += s[self.i]
                self.i += 1
            else:
                const = 0

                while self.i < len(s) and s[self.i].isdigit():
                    const = const * 10 + int(s[self.i])
                    self.i += 1

                self.i += 1
                the_decoded_string = self.decodeString(s)
                self.i += 1

                ans += the_decoded_string * const

        return ans
