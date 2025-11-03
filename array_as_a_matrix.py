mat1=[[1,2],[3,4]]
mat2=[[5,6],[7,8]]
result=[[0,0],[0,0]]
transpose=[[0,0],[0,0]]
#Multiplication
def mat_product(mat1,mat2):
    for i in range(2):
        for j in range(2):
            result[i][j]=(mat1[i][0]*mat2[0][j]+mat1[i][1]*mat2[1][j])
    print("Multiplication:")
    for k in result:
        print(k)
mat_product(mat1,mat2)

#Addition 
def mat_add(mat1,mat2):
    for i in range(2):
        for j in range(2):
            result[i][j]=mat1[i][j]+mat2[i][j]
    print("addition:")
    for k in result:
        print(k)
mat_add(mat1,mat2)

#Transpose
def mat_transpose(mat1):
    for i in range(2):
        for j in range(2):
            transpose[i][j]=mat1[j][i]
    print("Transpose:")
    for k in transpose:
            print(k)

mat_transpose(mat1)
