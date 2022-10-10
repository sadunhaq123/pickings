#file1 = open('picking-last-work-fixed_inconsistency.dat', 'r')
#file1 = open('29-sept_fixed_inconsistency.dat.txt', 'r')
file1 = open('4_october_columns_added.dat', 'r')
Lines = file1.readlines()
list_of_names = []
original_body = []
modified_body = []
original_line_number = 1

count = 0
line_number=0
count_636=0
offset_list = []
list_of_names = []

for line in Lines:
    content = line.strip()
    split = content.split(' ')
    meter = split[2]
    kilometer = float(meter) / 1000
    value = split[0] + ' ' + split[1] + ' ' + str(f"{kilometer:.4f}") + ' ' + split[3]
    list_of_names.append(value)
    #print(value)
    #break
    #print(content)
    #if()
#print(original_line_number)


with open('4_october_kilometers.dat', 'w+') as f:
    # write elements of list
    #break
    for items in list_of_names:
        #if counter > 1000:
        #    break
        f.write('%s\n' % items)
        #if counter_1> 288743:
        #    break

    print("File for kms written successfully")

# close the file
f.close()










