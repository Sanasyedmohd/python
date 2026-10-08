list1 = list(map(int, input("Enter first list:").split()))
list2 = list(map(int, input("Enter second list:").split()))

if len(list1) == len(list2):
  print("(a) lists are of the same length")
else:
  print("(a) lists are not of the same length")
  
if sum(list1) == sum(list2):
  print("(b) lists have the same sum")
else:
   print("(b) lists do not have the same sum")
   
if set(list1).intersection(set(list2)):
   print("(c) Both lists contain common value(s)")
else:
  print("(c) No common value")
