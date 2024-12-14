#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# Matriks 2x3
A = np.array([[4, 5, 6], 
              [7, 8, 9]])

# Matriks 2x3
B = np.array([[1, 2, 3],
              [1, 2, 3]])

A_plus_B = A + B # atau A_plus_B = np.add(A, B)
A_min_B = A - B  # atau A_min_B = np.subtract(A, B)

print("\nA + B:\n", A_plus_B)
print("\nA - B:\n", A_min_B)


# In[7]:


# matriks 3x2 
A = np.array([[1, 2], 
              [3, 4],
              [5, 6]])

# matriks 2x3
B = np.array([[10, 12, 12],
              [13, 14, 15]])

# matriks 3x3
A_mul_B = A @ B # atau A_mul_B = np.matmul(A, B)

print("\nA * B:\n", A_mul_B)


# In[9]:


# matriks 3x2
A = np.array([[1, 2], 
              [3, 4],
              [5, 6]])

# matriks 2x3
A_trans = A.transpose()

print("\nA Transpose:\n", A_trans)


# In[11]:


A = np.array([[5, 0, 1],
              [3, 2, 2],
              [1, 4, 2]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


A_det = np.linalg.det(A)
B_det = np.linalg.det(B)

print("\nDeterminan Matriks A:", A_det)
print("\nDeterminan Matriks B:", B_det)


# In[13]:


# matriks 3x3 (invertable)
A = np.array([[5, 0, 1],
              [3, 2, 2],
              [1, 4, 2]])

# matriks 3x3 (singular)
B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# invers matriks A
A_inv = np.linalg.inv(A)
print("\nA Invers:\n", A_inv)

# invers matriks B
B_inv = np.linalg.inv(B)     # akan menghasilkan error
print("\nA Invers:\n", B_inv)


# In[15]:


print("\nA x A Invers:\n", A @ A_inv)

print("\nA Invers x A:\n", A_inv @ A)







