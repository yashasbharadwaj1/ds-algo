#Reverse words in a given string
s="yashas.is.bad.boy"
res=s.split(".")
a=res[::-1] 
ans=".".join(a) 
print(ans) 
#output is boy.bad.is.yashas