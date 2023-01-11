#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


e = np.arange(1,11)
e


# In[6]:


a =np.array([[1,2,3],[10,20,30]])
b =np.array([[5,6,7],[40,50,60]])
a
b


# In[7]:


a


# In[8]:


c =np.hstack((a,b))


# In[9]:


c


# In[10]:


d = np.vstack((a,b))


# In[11]:


d


# In[12]:


f=np.arange(2,21,2)
f


# In[13]:


g= np.arange(13,131,13)


# In[14]:


g


# In[15]:


h=np.linspace(1.0,3.0,num=10)


# In[16]:


h


# In[17]:


i=np.array([[1,2,3],[5,6,7]])
i


# In[18]:


i.size


# In[19]:


i.shape


# In[20]:


i[:]


# In[21]:


i[1:2]


# In[22]:


i[0]


# In[23]:


i[1]


# In[24]:


i[:,2]


# In[28]:


a = np.random.randint(0,10,size=(3,3,))
print(a)



# In[27]:


print(a.max())


# In[29]:


a+=2


# In[30]:


a


# In[31]:


a.min()


# In[33]:


a.reshape(3,2)


# In[34]:


v=np.array([1,2,3,4])
v


# In[43]:


v.reshape((4,1))


# In[39]:


v.copy()


# In[42]:


v.reshape((4,1))


# In[ ]:




