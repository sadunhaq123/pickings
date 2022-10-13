#file1 = open('3_october_kilometers.dat', 'r')
file1 = open('tx.in (original values).in(originalvalues)', 'r')
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
l0=[]
l1=[]
l2=[]
l3=[]
l=[]
first_space = True
list_of_body = []

def squeeze(char,s):
    while char*2 in s:
        s=s.replace(char*2,char)
    return s

for line in Lines:
    content = line.strip()
    str1 = squeeze(" ", content)
    #print(str)
    split = str1.split(" ")
    #print(split)

    col1_original = float(split[0])
    col1 = int(float(split[0]))
    col2 = float(split[1])
    col3 = float(split[2])
    col4 = split[3]
    n = len(str((col1)))
    #print(n)
    #print(col1)
    if c%636 + 1 == 1 and n==1:
        value = '     ' + str(col1_original) + '        -1         0         0'
    elif n==1:
        value = '     ' + str(f"{col1_original:.3f}") + '     ' + str(f"{col2:.3f}") + '     ' + str(f"{col3:.3f}") + '         ' + col4
    elif c%636 + 1 == 1 and n==2:
        value = '    ' + str(col1_original) + '        -1         0         0'
    elif n==2:
        value = '    ' + str(f"{col1_original:.3f}") + '     ' + str(f"{col2:.3f}") + '     ' + str(f"{col3:.3f}") + '         ' + col4
    elif c%636 + 1 == 1 and n==3:
        value = '   ' + str(col1_original) + '        -1         0         0'
    elif n==3:
        value = '   ' + str(f"{col1_original:.3f}") + '     ' + str(f"{col2:.3f}") + '     ' + str(f"{col3:.3f}") + '         ' + col4

    #print(value)
    list_of_body.append(value)
    c +=1


with open('4_october_rayinvr_fixed_spaces.dat', 'w+') as f:
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

