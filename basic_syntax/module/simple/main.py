# encoding: utf-8

from basic_syntax.module.simple.utils.utils import get_sum
from basic_syntax.module.simple.utils.class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(encoder.encode('edcba'))

# 3
# edcba
# abcde
