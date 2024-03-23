#Task 2: Comprehensions (lists and sets).

#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
#§ Create a normal and comprehensive list that will display the codes.
'''§ Create a normal and comprehensive list that will add the codes together for auditing purpose.
§ Create a normal and comprehensive list that will display only codes that are tracked by odd
numbers.
§ Create a set to display the list of codes.'''

codes = [14, 15, 16, 17, 18, 19, 20]

display= []

for i in codes:
  display.append(i)

  print(display)

add_list = []
sum = 0

for s in codes:
  sun = sum + s
  add_list.append(sum)

  print(add_list)

sum_a = 0
 
add_list = [sum_a := sum_a + comp  for comp in codes]

print("\n" ,add_list)

#§ Create a normal and comprehensive list that will display only codes that are tracked by odd numbers.

normal_c = []

for odd_no in normal_c:

  if odd_no%2 != 0:
    normal_c.append(odd_no)

    print("normal a list that will display only codes that are tracked by odd numbers",normal_c)
    
    odd_noc =[com for com in codes if com%2 != 0]

    print("comprehensive list that will display only codes that are tracked by odd numbers.",odd_noc)

    setlist = set(codes)

    print("set to display the list of codes",setlist)