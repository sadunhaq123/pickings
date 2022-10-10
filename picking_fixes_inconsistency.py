#file1 = open('picking-last-work-fixed_rectified.dat', 'r')
#file1 = open('29_spet_4_more.dat', 'r')
#file1 = open('3_october_picking_4_more.dat', 'r')
file1 = open('4_october_picking_4_more.dat', 'r')
Lines = file1.readlines()
list_of_names = []
original_body = []
modified_body = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
original_line_number = 0

count = 0
line_number=0
count_636=0
l10 = []
g10 = {}
line=0
less={}
great = {}
deal = []
c=0
for line in Lines:
    content = line.strip()
    original_body.append(content)
    modified_body.append(content)
    
    
    values = content.split(' ')
    n = float(values[4])
    
    deal.append(n)
    
    if (line_number%636<10):
        l10.append(n)
        
        if (len(l10)>1 and line_number%636 !=0):
            if(abs(l10[line_number] - l10[line_number-1]) > 0.03):
                index = c*636 + line_number
                less[index]=n
     
    if (line_number%636>626):
        g10[line_number]=n
        
        if (len(g10)>1 and line_number%636 !=627):
            relative_line_number = abs(line_number -636)
            if(abs(g10[line_number] - g10[line_number-1]) > 0.03):
                index = c*636 + line_number
                great[index]= g10[line_number-1]
        
    
    line_number +=1
    if(line_number==636):
        l10.clear()
        
        x=int(original_line_number/636)
        c=c+1
        line_number = 0
    
    original_line_number +=1
    #print(line_number)
    #if()


#print(less)
print(great)

for i in range(len(original_body)):
    if i in less.keys():
        div = int(i/636)
        mod = i%636
        num =636*div
        hold = less[i]
        
        
        for j in range(mod, -1, -1):
            new_index = num+j
            hold = hold - 0.005
            deal[new_index] = hold
            #print(new_index, deal[new_index])
            
    if i in great.keys():
        div = int(i/636)
        mod = i%636
        num =636*div
        hold = great[i]
        
        
        for j in range(num+mod, num+636, 1):
            print(j)
            new_index = num+j
            hold = hold + 0.005
            deal[j] = hold
            #print(new_index, deal[new_index])
            
        #break
            

for i in range(len(original_body)):
    content = original_body[i]
    first_split= content.split(' ')
    new_n = deal[i]
    new_string = first_split[0] + ' ' + first_split[1] + ' ' + first_split[2] + ' ' +  first_split[3]  + ' ' + str(f"{new_n:.4f}") + ' ' + first_split[5]
    list_of_names.append(new_string)
    



    
counter_1 = 0
with open('4_october_fixed_inconsistency.dat', 'w+') as f:
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
    
    
    
    
    
    
    
    



