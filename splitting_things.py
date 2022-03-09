

numbers = "9,223,372,036,854,775,807"

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
values_list = values.split()

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

print('Old List')
print(values_list)
'''
new_list = []
for num in values_list:
    new_num = int(num)
    new_list.append(new_num)
x = 0
for num in new_list:
    x += num
print('New List')
print(new_list)
print('The sum is: {}'.format(x))
'''

for i in range(len(values_list)):
    values_list[i] = int(values_list[i])
print('New List')
print(values_list)