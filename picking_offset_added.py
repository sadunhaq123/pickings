#file1 = open('picking-last-work-fixed_inconsistency.dat', 'r')
#file1 = open('29-sept_fixed_inconsistency.dat.txt', 'r')
#file1 = open('3_october_fixed_inconsistency.dat', 'r')
file1 = open('4_october_fixed_inconsistency.dat', 'r')
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
    original_body.append(content)
    modified_body.append(content)
    original_line_number +=1
    #print(content)
    #if()
#print(original_line_number)

x=0
c=0
m=635
k=1
first = True
n=0
for ll in range(len(original_body)):
    if (ll%636==0 and ll==0):
        increment = 0
        m = 635
        x = x + 1

    if (ll >=0 and ll <636):
        content = original_body[ll]
        # print(content)
        parts = content.split(' ')
        value = 5 * x
        interval = parts[4]
        increment = increment + 1
        offset = 264 + (12.5 * m)
        offset_list.append(offset)
        m = m - 1
        # x=x+1
        new_string = str(f"{value:.2f}") + ' ' + str(increment) + ' ' + str(f"{offset:.2f}") + ' ' + interval
        #print(new_string)
        list_of_names.append(new_string)
        k = 0
        # c = c + 1

    if (ll>=636):
        #print("HE")
        if (ll % 636 == 0):
            #print("HEHE")
            increment = 0
            m = 635
            x = x + 1
            n= n + 1
        content = original_body[ll]
        # print(content)
        parts = content.split(' ')
        value = 5 * x
        interval = parts[4]
        increment = increment + 1
        y= ll%636
        offset = float(offset_list[y]) + 250*n
        m = m - 1
        # x=x+1
        new_string = str(f"{value:.2f}") + ' ' + str(increment) + ' ' + str(f"{offset:.2f}") + ' ' + interval
        #print(new_string)
        list_of_names.append(new_string)
        #break
counter_1 = 0
with open('4_october_columns_added.dat', 'w+') as f:
    # write elements of list
    #break
    for items in list_of_names:
        #if counter > 1000:
        #    break
        f.write('%s\n' % items)
        counter_1 = counter_1 + 1
        #if counter_1> 288743:
        #    break

    print("File for picking written successfully")

# close the file
f.close()










