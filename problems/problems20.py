
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def matrix_sum(matrix):# # func used for matrix
    print("Row Sums:")
    for i in range(len(matrix)):## yastu row eddhe anta 
        row_sum = 0## if we dont put this back row sum kuda sayrikolutadde
        for j in range(len(matrix[i])):#current row alli yastu element edhe anta thilkonokke
            row_sum += matrix[i][j] #i represents row and j represents coloum
        print(f"Row {i+1}: {row_sum}")

matrix_sum(matrix)

###2Q. FIND HIGHEST SUM IN A ROW
matrix2 = [
    [1, 2, 3],
    [10, 20, 30],
    [4, 5, 6]
]

def highest_row_sum(matrix):
    max_sum = 0
    row_number = 0
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix[i])):
            row_sum += matrix[i][j]
            if row_sum > max_sum:
                row_sum = max_sum
                row_sum = i + 1
    print("highest row" , "row_number")
    print("highest sum" , "max_sum")
    
highest_row_sum(matrix)
    

             
             
             
             
             
    
    