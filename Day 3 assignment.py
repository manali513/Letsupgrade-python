#!/usr/bin/env python
# coding: utf-8

# # sum of natural numbers using while loop

# In[1]:


n= int(input("enter the value" ))
sum1=0
i=1
while(i<=n):
    sum1=sum1+i
    i=i+1
print("sum of natural no is" ,sum1)


# # sum of natural numbers with if statement

# In[2]:


n=int(input("enter the value"))
if  n>0:
    n=(n*(n+1)/2)
    print("the natual no is",n )
else :
    print("enter the natural number")
    
    


# # To check whether integer is prime number

# In[ ]:


n= int(input("enter the value" ))
for i in range(2,n):
        if (n%i) == 0:
            print(no is not prime)
else:
    print("no is prime")


# In[ ]:





# In[ ]:




