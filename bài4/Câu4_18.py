def fibonacci_nho_hon_n(n):
 ds=[]
 a, b= 0, 1
 while a<n:
   ds.append(a)
   a,b=b,a+b
 return ds
n=int(input ("enter positive integer n: "))
ds_so = fibonacci_nho_hon_n(n)
print("fibonacci numbers smaller than", n, "is", ds_so)
