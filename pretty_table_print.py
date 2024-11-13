def print_table(table):
    longest_list_len = max(map(len,[list for list in table]))
    line = ''
    for i in range(longest_list_len):
        line = ''
        valid_elements = []
        for list in table :
            longest_element = max(map(len,list))
            try:
                valid_elements.append(list[i].rjust(longest_element))
            except IndexError :
                continue
        for element in valid_elements:
            line += element + '\t' 
        print(line)
            

tableData = [['apple', 'oranges', 'cherries', 'banana','pinapple','strawberry'],
['Alice', 'Bob', 'Carol'],
['dogs', 'cats', 'moose', 'goose','lion'],
['Ayanokoji']]

print_table(tableData)

tableData = [['apple', 'oranges', 'cherries', 'banana','pinapple','strawberry'],
['Alice', 'Bob', 'Carol'],
['dogs', 'cats', 'moose', 'goose','lion']]

print_table(tableData)

"""
output:
     apple     Alice      dogs
   oranges       Bob      cats
  cherries     Carol     moose
    banana     goose
  pinapple      lion
strawberry

"""


