#display numbers from a list using a loop
num1 = [1,2,3,4]
for i in num1:
  print(i) 

# total number of digits in a pattern
number = 3476376
counter = 0
while number != 0:
  number = number//10
  counter = counter + 1
print("Total digits are: ", counter) 
