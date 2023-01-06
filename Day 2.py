#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[7]:


q =np.array([1,2,3,4])
print(q)


# In[9]:


type(q)


# In[10]:


q.size


# In[11]:


b=np.array([(1,2,3,4),(5,6,7,8)])


# In[12]:


print(b)


# In[14]:


b.ndim


# In[15]:


q.ndim


# In[16]:


np.zeros(3)


# In[17]:


np.zeros((2,3))


# In[18]:


q


# In[19]:


np.zeros((3,2,4))


# In[21]:


np.full((3,4),2)


# In[22]:


np.random.rand(3,5)


# In[23]:


np.save("new array",q)


# In[26]:


np.load("new array.npy")


# In[27]:


np.ones((3,4))


# In[57]:


b.size


# In[29]:


q


# In[30]:


q.view()


# In[31]:


q.view(dtype="float")


# In[48]:


a=np.array([1,2,3])
a


# In[37]:


np.copy(a)


# In[49]:


a.reshape((3,1))


# In[43]:


a.sort()


# In[44]:


a


# In[50]:


a.shape


# In[52]:


a.size


# In[53]:


a.dtype


# In[54]:


np.eye(4)


# In[55]:


np.eye(3)


# In[56]:


np.eye(1)


# In[58]:


a.sum()


# In[59]:


a.min()


# In[60]:


a.max(axis=0)


# In[61]:


a.max()


# In[62]:


a.mean()


# In[70]:


w=np.array([4,3,5,2,1])
w


# In[72]:


w.sort()
w


# In[77]:


z=np.delete(a,2)


# In[78]:


z


# In[ ]:




