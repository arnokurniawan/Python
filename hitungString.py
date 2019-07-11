'''
Diberikan string input , hitung  masing-masing jumlah huruf , angka, dan simbol
input di masukkan manual

'''


def findDigitsCharsSymbols(inputString):
  words = inputString.split()
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    if char.islower() or char.isupper():
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = input("Masukkan Karakter :  ")
#inputString = "P@#yn26at^&i5ve"
print("Print total counts of chars, digits,and symbols")
print(findDigitsCharsSymbols(inputString))