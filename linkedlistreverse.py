#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        


# In[97]:


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)


# In[98]:


a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e


# In[73]:


def reverse(num):
    l=[]
    num=a
    l.append(num)
    while num.nextnode:
        
        print(num.value)
        num=num.nextnode
        l.append(num)
    
    l[0].nextnode=None
       
    for i in range(len(l)-1,0,-1):
        try:
            l[i].nextnode=l[i-1]
        except:
            pass
    


# In[71]:


l=[]
num=a
l.append(num)
while num.nextnode:
    
    print(num.value)
    num=num.nextnode
    l.append(num)


# In[72]:


l[2].value


# In[52]:


for i in range(len(l)-1,0,-1):
    print(i)
    print (l[i])


# In[82]:


reverse(a)


# In[83]:


b.nextnode.value


# In[87]:


a.nextnode.value


# In[84]:


c.nextnode.value


# In[ ]:





# In[88]:


def reverse1(num):
    current =num
    previous=None
    next1=None
    while current:
        next1=current.nextnode
        current.nextnode=previous
        previous=current
        current=next1
        


# In[91]:


reverse1(a)


# In[93]:


e.nextnode.value


# In[94]:


d.nextnode.value


# In[95]:


b.nextnode.value


# In[96]:


def nthfrmlastnode(a,n):
    lftpt=a
    m=lftpt
    for i in range(n):
        m=m.nextnode
    rtpt=m
    while rtpt:
        rtpt=rtpt.nextnode
        lftpt=lftpt.nextnode
    return lftpt
        
        
        
    


# In[102]:


nthfrmlastnode(a,1).value


# In[ ]:




