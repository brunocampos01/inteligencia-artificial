'''
width search

Explore all of the neighbors nodes at the present depth '''

three_d_array = [[[i for k in range(4)] for j in range(4)] for i in range(4)]

sum = three_d_array[1][2][3] + three_d_array[2][3][1] + three_d_array[0][0][0]

print(sum)