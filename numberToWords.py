class Solution:
    def numberToWords(self, num: int) -> str:
        self.str_ = str(num)
        self.len_num = len(self.str_)
        self.ans = ""
        self.number = {"0":"","1":" One","2":" Two","3":" Three",
                       "4":" Four","5":" Five","6":" Six",
                       "7":" Seven","8":" Eight","9":" Nine"}
        self.digit = {
            10: " Billion",
            7:" Million",
            4:" Thousand",
            1 :""  }
        self.oneTenth =  {"0":" Ten","1":" Eleven","2":" Twelve","3":" Thirteen",
                       "4":" Fourteen","5":" Fifteen","6":" Sixteen",
                       "7":" Seventeen","8":" Eighteen","9":" Nineteen"}
        self.tenth = {"2":" Twenty","3":" Thirty",
                       "4":" Forty","5":" Fifty","6":" Sixty",
                       "7":" Seventy","8":" Eighty","9":" Ninety"}
        self.solve(0)
        
        return self.ans[1:] if self.ans[1:] != "" else "Zero"
        
    def solve(self, idx):
        end = self.len_num - idx
        
        if end == 0:
            return 
        if end in {10,7,4,1}:
            self.ans += self.number[self.str_[idx]] 
            if len(self.ans) > 7 and not self.ans[-7] in {"B","M"}:
                self.ans += self.digit[end]
            elif len(self.ans)<= 7:
                self.ans += self.digit[end]

                
        elif end in {9,6,3} and self.str_[idx] != "0":
            self.ans += self.number[self.str_[idx]] + " Hundred"
        elif end in {8,5,2} and self.str_[idx] == "1":
            self.ans += self.oneTenth[self.str_[idx+1]]  
            if len(self.ans) > 7 and not self.ans[-7] in {"B","M"}:
                self.ans += self.digit[end-1]
            elif len(self.ans)<= 7:
                self.ans += self.digit[end-1]

            idx += 1
        elif end in {8,5,2} and self.str_[idx] != "1" and self.str_[idx] != "0":
            self.ans += self.tenth[self.str_[idx]]
        self.solve(idx+1)
        
        
        
        
        
        
        
        
