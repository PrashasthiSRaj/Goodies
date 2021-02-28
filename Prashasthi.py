print('Note: As there are only 10 goddies listed in the input fil given please enter the employee number upto 10\n')
a = input('Enter the number of Employee: ')
a = int(a)
file=open("Execution_input.txt",'r')
fout=open("Execution_output.txt","a")
line=[]
da=[]
lit=[]
str1=dict()
for data in file:
    data=data.replace('\n','')
    line.append(data)
    da=data.split(':')
    if da[1] !='':
        lit.append(int(da[1]))
        str1[lit[-1]]=da[0]
lit.sort()
temp=[]
diff=111111111
sum=0
for i in range(0,len(lit)-(a-1)):
    sum=lit[i+a-1]-lit[i]
    if diff > sum:
       diff=sum
       temp=[]
       for k in range(i,i+a):
           temp.append(lit[k])
print('Number of employees: '+ str(a))
print('\n')
fout.write('Number of employees: '+ str(a))
fout.write('\n')
print('Here the goodies that are selected for distribution are:')
for i in range(len(temp)):
    for k,v in str1.items():
        if temp[i]==k:
            print(v+": "+str(temp[i]))
            fout.write(v+": "+str(temp[i]))
            fout.write('\n')
output=temp[-1]-temp[0]

print('\n')
fout.write('\n')
print('And the difference between the chosen goodie with highest price and the lowest price is '+str(output))
fout.write('And the difference between the chosen goodie with highest price and the lowest price is '+str(output))  

fout.write
fout.close()


