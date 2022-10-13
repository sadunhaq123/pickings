#file1 = open('3_october_kilometers.dat', 'r')
file1 = open('3rd column values', 'r')
Lines = file1.readlines()

file2 = open('r_backup.in(sample)', 'r')
Lines2 = file2.readlines()
list_of_names = []
original_body = []
modified_body = []
original_line_number = 1
l3 =[]
for line in Lines:
    content = line.strip()
    #str1 = squeeze(" ", content)
    #print(str)
    split = content.split("\t")
    #print(split)
    third = split[2]
    #print(third)
    l3.append(third)

with open('x_shots_3rd.dat', 'w+') as f:
    # write elements of list
    #break
    for items in l3:
        #if counter > 1000:
        #    break
        f.write('%s, ' % items)
        #if counter_1> 288743:
        #    break

    print("File for xshots written successfully")

# close the file
f.close()