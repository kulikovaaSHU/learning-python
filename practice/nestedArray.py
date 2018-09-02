col_num=4
row_num=4
count = 0
array1 = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        array1[row][col] = count
        count += 1
        print(array1[row][col])
