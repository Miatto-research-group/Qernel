#     Copyright (C) 2020 Miatto research group.

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from Tensor import *


#seeding for reproducibility
np.random.seed(42)

#Creating Kets
a = np.array([-0.5+0.32j, 0.1+0.89j, 0.4+0.23j])
b = np.array([-0.3+0.32j, 0.2+0.89j, 0.5+21j])

tens_a = Tensor(a)
tens_b = Tensor(b)
print('Tensor A: ',  tens_a)
print('Tensor B: ',  tens_b)

print("A+B ", tens_a + tens_b)
print("A-B ", tens_a - tens_b)
print("A*3 ", tens_a * 3)
print("3.0*A ", 3.0 * tens_a)
print("A/10 ", tens_a/10)

"""
h = ket_a ** 5
print('Ket A**5: ',  h)

print('A == A: ',  ket_a == ket_a)
print('A == B: ',  ket_a == ket_b)
print('A != B: ',  ket_a != ket_b)
print('A != A: ',  ket_a != ket_a)

print('A.array', ket_a.array)
print('A.shape', ket_a.shape)
print("A.normalise.is_pure ", ket_a.normalise().is_pure)
print("A.normalise().is_valid_QS ", ket_a.normalise().is_valid_QS)
print("A.is_valid_QS ", ket_a.is_valid_QS)
print("A.purity ", ket_a.purity)

tmp_dict = {ket_a : "Yay!"}
print('dict?', tmp_dict[ket_a])

print("A.normalise() ", ket_a.normalise())

print("A.complex_conjugate()", ket_a.complex_conjugate())

print("A.conjugate_transpose()", ket_a.conjugate_transpose())

print("A.inner_prod(B) ", ket_a.inner_prod(ket_b))









dm_a = DensityMatrix(a)
dm_b = DensityMatrix(b)

#Performing operations

#addition
print(ket_a + ket_b) #superposition
print(dm_a + dm_b) #convex sum

#substraction
print(ket_a - ket_b) #superposition
print(dm_a - dm_b) #convex sum

"""