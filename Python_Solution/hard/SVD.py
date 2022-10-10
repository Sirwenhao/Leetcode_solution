# from numpy import array
# from scipy.linalg import svd
# A = array([[1,2],[3,4],[5,6]])
# U, S, V = svd(A)
# print(U)
# print(S)
# print(V)

# from numpy import array
# from numpy import diag
# from numpy import dot
# from numpy import zeros
# from scipy.linalg import svd
# # define a matrix
# A = array([[1,2],[3,4],[5,6]])
# print(A)
# # Singular-value decomposition
# U, S, V = svd(A)
# # create m x n Sigma matrix
# Sigma = zeros((A.shape[0], A.shape[1]))
# # print(Sigma)
# # populate Sigma with n x n diagonal matrix
# Sigma[:A.shape[1], :A.shape[1]] = diag(S)
# # print(Sigma)
# # reconstruct matrix
# B = U.dot(Sigma.dot(V))
# print(B)

# Reconstruct SVD