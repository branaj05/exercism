def tick(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    result = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = sum(
                matrix[r][c]
                for r in range(i-1, i+2)
                for c in range(j-1, j+2)
                if (r, c) != (i, j) and 0 <= r < rows and 0 <= c < cols
            )
            if matrix[i][j] == 1:
                result[i][j] = 1 if neighbors in (2,3) else 0
            else:
                result[i][j] = 1 if neighbors == 3 else 0
    return result

# import numpy as np
# KERNEL = np.array([[1, 1, 1], 
#                    [1, 0, 1], 
#                    [1, 1, 1]])
# def tick_convolve(matrix):
#     """Fun but doesn't work in Exercims's test suite b/c numpy"""
#     if not matrix:
#         return []
#     matrix = np.array(matrix)
#     mat_bool = matrix.astype(bool)
#     def _convolve2d(img, kern):
#         kh, kw = kern.shape
#         pad_h, pad_w = kh//2, kw//2
#         padded = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode ='constant')

#         conv = np.zeros_like(img, dtype = float)
#         for i in range(img.shape[0]):
#             for j in range(img.shape[1]):
#                 conv[i, j] = np.sum(padded[i:i+kh, j:j+kw]*kern)
#         return conv

#     conv = _convolve2d(matrix, kern = KERNEL)
#     lives_on = (2 <= conv) & (conv <= 3) & mat_bool
#     resurrects = (conv == 3) & ~(mat_bool)
#     retval = lives_on | resurrects
#     return retval.astype(int).tolist()


if __name__ == "__main__": 
    matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
    expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    ret = tick(matrix)