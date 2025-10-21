#!/usr/bin/env python
# coding: utf-8

# # Conditionals and evaluations
# 
# To work with logic in Python, you must first understand `if`, `else`, and `elif`. There are other conditional statements in Python however. This notebook will introduce you to the basic conditionals that will allow you to do the most amount of logic work.
# 
# Evaluations go hand in hand with conditional statements because it is how Python decides to go into the next instruction or skip it.

# ## `if` conditions and evaluations

# In[1]:


# all conditionals evaluate the result of the condition (expression)
condition = True 
if condition:
    print("The condition was met")


# In[2]:


# if the condition changes to false, then it get skipped
condition = False
if condition:
    print("Was the condition met?")


# In[3]:


# some data structures are truthy: false when empty, but true when they contain items
groceries = []
if groceries:
    print("we have some groceries!")

invites = ["John", "George"]
if invites:
    print("we have some invites!")


# In[4]:


# other types like integers (0, and any positive integer) are truthy
properties = 0
if properties:
    print("We have properties!")

parents = 2
if parents:
    print("we have parents!")


# In[5]:


# operators are supported 
if properties == 0:
     print("no properties!")

if parents > 1:
    print("there is more than 1 parent")


# ## `else` conditions
# When an `if` condition is not met, you can use an `else` condition (in that order!). Rule of thumb: don't try to compound several `if` and `else` conditions and keep them to a minimum, it otherwise makes code harder to read!

# In[6]:


if properties:
    print("We have properties")
else:
    print("We don't have any properties")


# ## `elif` conditions
# This is useful when we want to add an `else` statement that needs to be mapped to a condition as well

# In[7]:


if properties:
    print("We have properties")
# evaluate if parents is valid
elif parents:
    print("We don't have any properties, but we have parents")


# ## Negative conditions
# 
# By default, Python evaluates statements that are `True`. To represent a negative statement, you must add a `not` keyword. Watch out for statement that use `not` as it can make it harder to read!

# In[12]:


name = None

if not name:
    print("Didn't get a name!")


# In[13]:


# same is possible with elif conditions
last_name = None

if not name:
    print("No name!")
elif not last_name:
    print("No last name either!")


# ## Compounding conditions with `and`
# 
# When multiple conditions must be met you can use `and` as well.

# In[14]:


has_kids = True
married = True

if has_kids and married:
    print("This person is married and has kids")


# In[11]:


# not can be used as well but can get harder to read

likes_books = False
is_logged_in = False

if not likes_books and not is_logged_in:
    print("User not logged in!")


# In[ ]:





# In[ ]:




