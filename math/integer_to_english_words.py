# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/


# Initial solution - reverse order
class Solution1:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tenToNineteen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion"]
        result=[]
        power = 0

        while num:
            chunk = num % 1000
            if chunk>0 and power>0:
                result.append(suffixes[power])
            
            onesDigit = (chunk % 100)%10
            tensDigit = (chunk % 100)//10
            hundredsDigit = chunk//100

            # Handle ones digit for 1-9 or 20-99
            if onesDigit>0 and tensDigit!=1:
                result.append(singles[onesDigit])
            
            # Handle ones and tens digit for 11-19
            if tensDigit == 1:
                result.append(tenToNineteen[onesDigit])
            # Handle tens digit for 20-99
            elif tensDigit>1:
                result.append(tens[tensDigit])

            # Handle hundreds digit for 100-999
            if hundredsDigit>0:
                result.extend(["Hundred", singles[hundredsDigit]])

            power+=1
            num = num//1000
        return " ".join(reversed(result))

# Slightly cleaner solution - Solve each chunk from left to right
class Solution2:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tenToNineteen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        suffixes = ["", "Thousand", "Million", "Billion"]
        result=[]
        power = 0

        def convert(n):
            onesDigit = (n % 100)%10
            tensDigit = (n % 100)//10
            hundredsDigit = n//100
            
            if n < 10:
                return singles[n]
            elif n<20:
                return tenToNineteen[n-10]
            elif n<100:
                return tens[tensDigit] + (" " + singles[onesDigit] if onesDigit else "")
            else:
                return singles[hundredsDigit] + " Hundred" + (" " + convert(n % 100) if n % 100 != 0 else "")

        while num:
            chunk = num % 1000
            if chunk>0:
                chunk_words = convert(chunk) 
                if power>0:
                    chunk_words += " " + suffixes[power]
                result.append(chunk_words)
            
            power+=1
            num = num//1000
        
        return " ".join(reversed(result))