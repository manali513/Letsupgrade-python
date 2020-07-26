#!/usr/bin/env python
# coding: utf-8

# In[9]:


str1="India is my country"
substr1='is'
i=str1.find(substr1)
if i==-1:
    print("substr1 not found")
while i!=-1:
    print("substr1 at index no",(substr1,i))
    i=str1.find(substr1,i+len(substr1),len(str1))


# # # using lower() and upper()

# lower() function is used to make the string into small letters when the  iput is all in upper case

# In[7]:


str1="I WANT TO BE  SUCCESSFUL"
str1.lower()


# Upper() function is used to make the string into  upper case when the  iput is all in lower case

# In[8]:


str2="we are python programmers"
str2.upper()


# In[ ]:




