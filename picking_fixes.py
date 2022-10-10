#file1 = open('picking-last-work.dat', 'r')
#file1 = open('29_sept.dat', 'r')
#file1 = open('3_october_picking.dat', 'r')
file1 = open('4_oct_picking.dat', 'r')
Lines = file1.readlines()
list_of_names = []
original_body = []
modified_body = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
original_line_number = 1

count = 0
line_number=0
count_636=0


for line in Lines:
    content = line.strip()
    original_body.append(content)
    modified_body.append(content)
    original_line_number +=1
    #if()




# Strips the newline character
nn= len(original_body)
zz=0
line=0
while(line!=nn):
#for line in range(len(original_body)):

    content = original_body[line]
    #print(content)
    c=1

    original = content
    values = content.split(' ')
    n = int(float(values[3]))
    #print("N:", n)
    if (count ==0):
        holder = n
        first_content = original
        #print("F:", first_content)
        count_636 += 1

    elif (count>=1):
        new_holder = n
        if(holder == new_holder):
            count_636 +=1

    list_of_names.append(original)
    count += 1
    line=line+1
    #print("C636:", count_636)
    #print("C:", count)

    if (count==636):
        diff = count-count_636
        #print("DIFF:", diff)
        increment = 0.005
        old_content = first_content
        first_split = old_content.split(' ')
        first_n = round(float(first_split[4]),2)
        #first_n = f"{first_n:.2f}"
        perm = round(float(holder),2)
        new_n = first_n
        x=int(line_number/636)
        c=x*636
        no_of_inserts=0
        while(diff!=0):
            #print("Going in DIFF")
            new_n = new_n + increment
            new_n = round(new_n, 4)
            #new_n = f"{new_n:.2f}"
            new_string = first_split[0] + ' ' + first_split[1] + ' ' + first_split[2] + ' ' +  str(f"{perm:.2f}")  + ' ' + str(f"{new_n:.4f}") + ' ' + first_split[5]
            list_of_names.insert(c, new_string)
            diff = diff-1
            no_of_inserts += 1
            list_of_names.pop()
        #print("C636:", count_636)
        #print("C:", count)
        count=0
        count_636=0
        line = line - no_of_inserts
        #print("LINE:", line)
    line_number = line_number + 1




    #print(values)
    #print(values[0])
    #if (line_number == 640*3):
    #    break




for x in range(len(list_of_names)):
    break
    print(list_of_names[x])
    if (x>60):
        break

ll=1
keep = {}
for x in range(len(list_of_names)):
    #break
    #if (x>60):
    #    break
    ccc = list_of_names[x].split(' ')
    vv = int(float(ccc[3]))
    #print(ccc)
    #print(vv)
    if vv not in keep.keys():
        keep[vv] = 0
    else:
        keep[vv] +=1



counter_1 = 0
with open('4_october_picking_4_more.dat', 'w+') as f:
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