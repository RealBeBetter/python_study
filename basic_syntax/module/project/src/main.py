# encoding: utf-8

from basic_syntax.module.project.proto.mat import Matrix
from basic_syntax.module.project.utils.mat_mul import mat_mul

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print(mat_mul(a, b).data)

# [[19, 22], [43, 50]]
