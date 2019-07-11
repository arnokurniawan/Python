'''
Given a two list of ints create a third list 
such that should contain only odd numbers from the first list and even numbers from the second list
'''

def mergeList(listOne, listTwo):
  thirdList = []
  for num in listOne:
    if(num % 2 != 0):
      thirdList.append(num)
  for num in listTwo:
    if(num % 2 == 0):
      thirdList.append(num)
  return thirdList
    
print("Merged List is")
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print(mergeList(listOne, listTwo))