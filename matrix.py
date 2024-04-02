import numpy as np

def get_matrix_from_user(prompt):
    print(prompt)
    rows = int(input("请输入矩阵的行数："))
    cols = int(input("请输入矩阵的列数："))
    matrix = np.zeros((rows, cols))
    
    for r in range(rows):
        for c in range(cols):
            matrix[r, c] = float(input(f"请输入第{r+1}行，第{c+1}列的元素："))
    return matrix

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def calculate_inverse(matrix):
    return np.linalg.inv(matrix)

def matrix_multiplication(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

if __name__ == "__main__":
    operation = input("请选择操作：det(计算行列式)，inv(计算逆矩阵)，mul(矩阵乘法)：")
    
    if operation == 'det':
        matrix = get_matrix_from_user("请输入矩阵的值：")
        print(f"矩阵的行列式值为：{calculate_determinant(matrix)}")
    elif operation == 'inv':
        matrix = get_matrix_from_user("请输入矩阵的值：")
        if np.linalg.det(matrix) == 0:
            print("该矩阵不可逆。")
        else:
            print(f"矩阵的逆为：\n{calculate_inverse(matrix)}")
    elif operation == 'mul':
        matrix_a = get_matrix_from_user("请输入第一个矩阵的值：")
        matrix_b = get_matrix_from_user("请输入第二个矩阵的值：")
        if matrix_a.shape[1] != matrix_b.shape[0]:
            print("错误：第一个矩阵的列数必须与第二个矩阵的行数相等。")
        else:
            print(f"矩阵乘积为：\n{matrix_multiplication(matrix_a, matrix_b)}")
    else:
        print("无效的操作选项。")
