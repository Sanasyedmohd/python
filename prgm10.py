numbers=list(map(int,input("Enter numbers:").split()))
for i in range(len(numbers)):
  if numbers[i] > 100:
     numbers[i]="over"
print(numbers)
