#!/usr/bin/env python
# coding: utf-8

# # Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, and make a new dictionary in which keys become values and values become keys, as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,
# "http": 80}

# In[2]:


port1={21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
new_dict = dict([(value, key) for key, value in port1.items()])
print(new_dict)
         


# # 2.	Take a list of tuple as shown below.
# [(1,2), (3,4), (5,6),(4,5)]
# Make a new list which contains sum of number of tuples.[(1,2), (3,4), (5,6),(4,5)]
# 

# In[3]:


list1=[(1,2),(2,3),(3,4),(4,5)]
a=[sum(i) for i in list1]
print(a)


# # [(1,2,3), [1,2], ['a','hit','less']]
# The List contains tuple and lists. Make the elements of inner lists and tuples to outer list
# 
# 

# In[5]:


list1=[(1,2,3),[1,2],["a","hit","less"]]
result = [item for i in list1 for item in i] 
print(result)


# In[ ]:





# In[ ]:




