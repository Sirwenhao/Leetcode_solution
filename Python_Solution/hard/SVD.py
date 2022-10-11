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

# # Reconstruct SVD
# from numpy import array
# from numpy import diag
# from numpy import dot
# from scipy.linalg import svd
# # define a matrix
# A = array([[1,2,3],[4,5,6],[7,8,9]])
# print(A)
# # Singular-value decomposition
# U, S, V = svd(A)
# # create n x n Sigma matrix
# Sigma = diag(S)
# # reconstruct matrix
# B = U.dot(Sigma.dot(V))
# print(B)

# # Pseudoinverse
# from numpy import array
# from numpy.linalg import pinv
# # define a matrix
# A = array([[0.1, 0.2],
#             [0.3, 0.4],
#             [0.5, 0.6],
#             [0.7, 0.8]])
# print(A)
# # calculate pseudoinverse
# B = pinv(A)
# print(B)

# # Pseudoinverse via SVD
# from numpy import array
# from numpy.linalg import svd
# from numpy import zeros
# from numpy import diag
# # define matrix
# A = array([[0.1, 0.2],
#             [0.3, 0.4],
#             [0.5, 0.6],
#             [0.7, 0.8]])
# print(A)
# # calculate svd
# U, S, VT = svd(A)
# # reciprocals of s
# d = 1.0 / S
# # create m x n D matrix
# D = zeros(A.shape)
# # populate D with n x n diagonal matrix
# D[:A.shape[1], :A.shape[1]] = diag(d)
# # calculate pseudoinverse
# B = VT.T.dot(D.T).dot(U.T)
# print(B)

# from numpy import array
# from numpy import diag
# from numpy import zeros
# from scipy.linalg import svd
# # define a matrix
# A = array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#             [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
# print(A)
# # Singular-value decomposition
# U, S, V = svd(A)
# # create m x n Singma matrix
# Sigma = zeros((A.shape[0], A.shape[1]))
# # populate Sigma with n x n diagonal matrix
# Sigma[:A.shape[0], :A.shape[0]] = diag(S)
# # select
# n_elements = 2
# Sigma = Sigma[:, :n_elements]
# V = V[:n_elements]
# # reconstruct
# B = U.dot(Sigma.dot(V))
# print(B)
# # transform
# T = U.dot(Sigma)
# print(T)
# T = A.dot(V.T)
# print(T)

from numpy import array
from sklearn.decomposition import TruncatedSVD
# define array
A = array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
print(A)
# svd
svd = TruncatedSVD(n_components=2)
svd.fit(A)
result = svd.transform(A)
print(result)