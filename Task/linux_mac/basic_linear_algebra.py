def vector_size_check(*vector_variables):
    first_length = len(vector_variables[0])
    for v in vector_variables:
        if len(v) != first_length:
            return False
    return True

def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    plus_vector = [0] * len(vector_variables[0])
    for v in vector_variables:
        for index in range(len(v)):
            plus_vector[index] += v[index]
    return plus_vector

def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    minus_vector = list(vector_variables[0])
    for v in vector_variables[1:]:
        for index in range(len(v)):
            minus_vector[index] -= v[index]
    return minus_vector

def scalar_vector_product(alpha, vector_variable):
    return [alpha * i for i in vector_variable]

def matrix_size_check(*matrix_variables):
    rows = len(matrix_variables[0])
    for m in matrix_variables:
        if len(m) != rows:
            return False
        for row in m:
            if len(row) != len(matrix_variables[0][0]):
                return False
    return True

def is_matrix_equal(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        return False
    first_matrix = matrix_variables[0]
    for m in matrix_variables[1:]:
        for row1, row2 in zip(first_matrix, m):
            if row1 != row2:
                return False
    return True

def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError("Matrix sizes do not match")
    plus_matrix = [[0]*len(matrix_variables[0][0]) for _ in range(len(matrix_variables[0]))]
    for m in matrix_variables:
        for i in range(len(m)):
            for j in range(len(m[i])):
                plus_matrix[i][j] += m[i][j]
    return plus_matrix

def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError("Matrix sizes do not match")
    minus_matrix = [row[:] for row in matrix_variables[0]]
    for m in matrix_variables[1:]:
        for i in range(len(m)):
            for j in range(len(m[i])):
                minus_matrix[i][j] -= m[i][j]
    return minus_matrix

def matrix_transpose(matrix_variable):
    transpose_matrix = []
    for i in range(len(matrix_variable[0])):
        new_row = []
        for v in matrix_variable:
            new_row.append(v[i])
        transpose_matrix.append(new_row)
    return transpose_matrix

def scalar_matrix_product(alpha, matrix_variable):
    scalar_matrix = []
    for row in matrix_variable:
        new_row = []
        for item in row:
            new_row.append(alpha * item)
        scalar_matrix.append(new_row)
    return scalar_matrix

def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_b)

def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError("Matrix product is not available")

    result_matrix = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix
