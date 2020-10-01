#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 2
b = 2


# In[3]:


a + b


# In[5]:


print(a + b)
print( a - b)
print(a * b)


# In[7]:


print( 10 % 3)


# - Assignment Operators

# - The standard assignment operators are available. That is ,α ® = beta is a shorthand for α = α ® β where ® is any arithmetic operator we saw above.

# In[9]:


a = 12
b = 5
a += b
print(a, b)
a -= b
print(a, b)
a *= b
print(a, b)
a **= b
print(a, b)


# - Boolean 
# - The two constants True and False are defined.
# - The usual boolean operators are also available  : ==, !=, >, <, >=, <=

# In[11]:


a = 12
b = 13
print(a ==b - 1, a == b, a != b, a < b, a >= b)


# - Bitwise Operators
# - Bitwise operators acts on bits and performs bit by bit operation.

# In[ ]:


- Bitwise AND------X & Y
- Bitwise OR------X | Y
- Bitwise NOT------X ~ Y
- Bitwise XOR------X ^ Y
- Bitwise RIght Shift------X >>
- Bitwise Left Shift------X <<


# In[14]:


a = 60
print(bin(a))
b = 13
print(bin(b))


# In[22]:


a = 60   # 60 = 0011 1100
b = 13   # 13 = 0000 1101

c = a & b;   # 12 = 0000 1100
print("Value of c is ",c)

c = a | b;   # 61 = 0011 1101
print("Value of c is ",c)

c = a ^ b;   # 49 = 0011 0001
print("Value of c is ",c)
      
c = ~ a;     # 61 = 1100 0011
print("Value of c is ",c)
      
# The left operands value is moved right by the number of bits specified by the rigte operand.      
c = a >> 2;  # 15 = 0000 1111 and a will be moved two units at the left.
print("Value of c is ",c)

# The left operands value is moved left by the number of bits specified by the left operand.
c = a << 2;  # 240 = 1111 0000 and a will be moved two units at the right.
print("Value of c is ",c)


# - Relational Operators

# ###  Relational Operators: 
#     Relational operators compares the values. It either returns True or False according to the condition.
# 
# - Greater than: True if left operand is greater than the right---- x > y
# - Less than: True if left operand is less than the right---- x < y
# - Equal to: True if both operands are equal---- x == y
# - Not equal to - True if operands are not equal---- x != y
# - Greater than or equal to: True if left operand is greater than or equal to the right---- x >= y
# - Less than or equal to: True if left operand is less than or equal to the right---- x <= y
# 
# 

# In[35]:


# Examples of Relational Operators 
a = 25
b = 47
  
# a > b is False 
print(a > b) 
  
# a < b is True 
print(a < b) 
  
# a == b is False 
print(a == b) 
  
# a != b is True 
print(a != b) 
  
# a >= b is False 
print(a >= b) 
  
# a <= b is True 
print(a <= b)


# ### Special operators:
#     There are some special type of operators like-
# ###### Identity operators-
# is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.
# - is          True if the operands are identical 
# - is not      True if the operands are not identical
# 

# In[29]:


# Examples of Identity Operators
a1 = 3
b1 = 3
a2 = 'DataScience'
b2 = 'DataScience'
a3 = [1, 2, 3]
b3 = [1, 2, 3]
a4 = (1, 2, 3)
b4 = (1, 2, 3)
print(a1 is not b1)
print(a2 is b2)
# Output is False,Since Lists are mutable.
print(a3 is b3)
print(a4 is b4)


# In[27]:


a2[2] = "M"


# - Logical Operators

# ### Logical operators: 
#     Logical operators perform Logical AND, Logical OR and Logical NOT operations.
# 
# 
# - Logical AND: True if both the operands are true----  x and y
# - Logical OR: True if either of the operands is true---  x or y
# - Logical NOT: True if operand is false--- not x
# 
# 

# In[31]:


# Examples of Logical Operator 
a = True
b = False
  
# Print a and b is False 
print(a and b) 
  
# Print a or b is True 
print(a or b) 
  
# Print not a is False 
print(not a)


# In[33]:


import sys
print(sys.getsizeof(a3))
print(sys.getsizeof(b3))


# - Conditional Statement

# In[44]:


# Create a variable salary and Indentation is necessary after If and else
salary = 35000
if salary >= 25000: 
    print("eligible for loan")
else:
        print("Not eligible for loan")


# In[43]:


# Create a variable salary and Indentation is necessary after If and else
salary = 15000
if salary >= 25000: 
    print("eligible for loan")
else:
        print("Not eligible for loan")


# In[51]:


# Create a variable salary and without indentation eror is generated there.
salary = 35000
if salary >= 25000: 
print("eligible for loan")


# In[50]:


marks = 90
if marks >= 70:
    print("Eligible for next round")
else:
    print("Not eligible for next round")      


# In[ ]:




