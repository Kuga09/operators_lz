input_data = open('input.txt','r') 
a = input_data.read()
a=a.split()
b=int(a[0])
q=int(a[1])
n=int(a[2])
s=(b*(q**n-1))/(q-1)
output_data = open('output.txt','w')
output_data.write(str(s))
input_data.close()
output_data.close()