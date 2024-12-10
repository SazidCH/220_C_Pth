#CORRECT VER

#Task 03: Decryption Process

def decrypt_matrix(matrix):
  #To Do
    numb_rows = len(matrix)
    numb_cols = len(matrix[0])
    column_sums = [0] * numb_cols

    for i in range(numb_cols):
        for j in range(numb_rows):
            column_sums[i] += matrix[j][i]

    result_size = numb_cols - 1
    result = [0] * result_size

    for k in range(result_size):
        result[k] = column_sums[k + 1] - column_sums[k]
    print(matrix)
    print('decrypted linear array:')

    return result

  #END

matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]
