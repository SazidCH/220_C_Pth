**Instructions to Follow (Failing to follow these will result mark deductions).**
1. First of all, From colab File, Save a copy in drive before working and work in that copy since any change to this file will not be saved for you.
2. You can not use any built-in function except len()

3. You can not use any other python collections except array (e.g: tuple, dictionaries etc.).

4. We will initialize a new array using numpy library. We have to mention the fixed size during initialization. There might be 4 approaches.

 i. arr = np.array([None] * 10) #Initializing an array length 10 with values None.

 ii. arr = np.array([0] * 10) #Initializing an array length 10 with values zero.

 iii. arr = np.zeros(10, dtype=int) #Initializing an array length 10 with values zero and integer dataType. By default, dtype is float.

 iv. arr = np.array([10, 20, 30, 40]) #Initializing an array length 4 with the values.

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

#You will see the status Accepted after completion if your code is correct.

If your function is wrong you will see wrong [correction percentage]

Do not change the driver code statements. You can only change the input values to test your code. 

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

