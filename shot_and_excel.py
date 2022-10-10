import pandas as pd

list_of_fifth_index = []
list_of_fifth_values = []
list_of_fifth_rayinvr = []

file1 = open('4_october_rayinvr_1_corrected.dat', 'r')
Lines = file1.readlines()

# Load the xlsx file
excel_data = pd.read_excel('Shot_Z_input.xlsx', usecols=[0,2])
# Read the values of the file in the dataframe
df = pd.DataFrame(excel_data)
# Print the content
#print("The content of the file is:\n", df)
c=1
for i in range(len(df)):
    #print(i, type(i))
    #print(df.loc[i, 'A'], df.loc[i, 'C'])
    if c%5 == 0:
        #pass
        x = int(df.loc[i, 'A'])
        yy =float(df.loc[i, 'C'])
        y = f"{yy:.4f}"
        #print("IN LOOP", x, y)
        list_of_fifth_index.append(int(x))
        list_of_fifth_values.append(y)
    c +=1

#print(list_of_fifth_index)
line_number=1
c636 = 636
for line in Lines:
    content = line.strip()
    split = content.split(' ')
    #print(split)
    zz = float(split[0])
    z = f"{zz:.3f}"
    if line_number == 1:
        list_of_fifth_rayinvr.append(z)
    elif line_number == c636 + 1:
        list_of_fifth_rayinvr.append(z)
        c636 += 636
    line_number += 1

#print(list_of_fifth_rayinvr)
df2 =pd.DataFrame()
print(len(list_of_fifth_index), len(list_of_fifth_values), len(list_of_fifth_rayinvr))

df2[0] = list_of_fifth_index[:]
df2[1] = list_of_fifth_values[:]
df2[2] = list_of_fifth_rayinvr[:471]

df2.to_excel('shots_z_rectified.xlsx', index = False, header=None)