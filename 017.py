"""If all the numbers from 1 to 1000
    (one thousand) inclusive were written
    out in words, how many letters would be used?
"""

import math


oneThroughNine = "onetwothreefourfivesixseveneightnine"
tenThroughNineteen = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
twentyThroughNinety = "twentythirtyfourtyfiftysixtyseventyeightyninety"




def main():
    """docstring for main"""
    
##1-99 will contain 36 + 70 + 74 8= 854 letters
# If we break it down we have the numbers 1-9 occurring 100 times each. => 36*100 = 3600
# 1-99 occurring 9 times => 9*854 = 7686
# “hundred” occurring 9 times with 7 letters. => 7*9 = 63
# “hundred and” occurring 9*99 times with 10 letters => 9*99*10 = 8910

    print(854 + 3600 + 7686 + 63 + 8910 + len("onethousand"))
    
    
            
if __name__ == "__main__":
    main()
