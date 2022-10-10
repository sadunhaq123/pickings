#file1 = open('3_october_kilometers.dat', 'r')
file1 = open('4_october_kilometers.dat', 'r')
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
list_of_offset = []
list_of_time = []
list_of_time_permanent = []
list_of_max_offset = []
c=0
reversed_list_of_time = []
list_of_body = []
interval = 1
for line in Lines:
    content = line.strip()
    split = content.split(' ')
    offset = split[2]
    time = split[3]
    list_of_offset.append(offset)
    list_of_time.append(time)
    list_of_time_permanent.append(time)
    if len(list_of_time)==636:
        reversed_list_of_time.append(list_of_time[::])
        list_of_time.clear()

        #if (c>1300):
    c = c + 1


for i in range(len(list_of_offset)):
    if i%636 == 0:
        list_of_max_offset.append(list_of_offset[i])

c=0.0000-0.250
incr = 0.0125
incr2 = 0.250
cholder = c
z=-1
new_c = True
for i in range(len(list_of_time_permanent)):
    if i %636 == 0:
        max_value = list_of_max_offset.pop(0)
        #print(max_value)
        max_value = float(max_value)

        max_value = f"{max_value:.3f}"
        #print(max_value)
        header = '     ' + str(max_value) + '       -1         0         0'
        list_of_body.append(header)
        #print(header)
        c=c+incr2
        new_c = True
        z=z+1
        col2_list = reversed_list_of_time.pop(0)
    else:
        if new_c is True:
            cholder = c
            new_c = False
        col1 = float(cholder)
        #print(col2_list)
        col2 = float(col2_list.pop(0))
        col3 = float(0.010)
        col4 = 1
        value = '     ' + str(f"{col1:.3f}") + '    '+ str(f"{col2:.3f}")+ '     '+ str(f"{col3:.3f}")+ '         1'
        #print(value)
        list_of_body.append(value)
        cholder=cholder+incr

footer = '    0    0         0        -1'
list_of_body.append(footer)

with open('4_october_rayinvr_1_corrected.dat', 'w+') as f:
    # write elements of list
    #break
    for items in list_of_body:
        #if counter > 1000:
        #    break
        f.write('%s\n' % items)
        #if counter_1> 288743:
        #    break

    print("File for rayinvr written successfully")

# close the file
f.close()
#print(list_of_body)