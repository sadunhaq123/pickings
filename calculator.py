#n,l,m,h,c = 15,114,220,18,0
#n,l,m,h,c = 50,505,354,88,18
#n,l,m,h,c = 171,225,171,111,13
#n,l,m,h,c = 136,209,238,102,26
#n,l,m,h,c = 132,126,134,62,7
#n,l,m,h,c = 147,217,241,158,21
#n,l,m,h,c = 129,111,111,60,7
#n,l,m,h,c = 66,100,64,40,9
#n,l,m,h,c = 165,209,236,161,40
#n,l,m,h,c = 0,568,509,44,3
#n,l,m,h,c = 280,379,537,330,77
#n,l,m,h,c = 368,599,643,362,57
n,l,m,h,c = 78,55,80,45,6

all = n+l+m+h+c

na = round((n/all)*100,1)
la = round((l/all)*100,1)
ma = round((m/all)*100,1)
ha = round((h/all)*100,1)
ca = round((c/all)*100,1)
print(na, la, ma, ha, ca)
print(na+la+ma+ha+ca)