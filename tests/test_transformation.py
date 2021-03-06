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

from transformation import Transformation
import numpy as np

unitary = np.array([[0.0+0.0j, 0.0+1.0j], [0.0-1.0j, 0.0+0.0j]])

def test_init_from_unitary_returns_unitary():
    U = Transformation.from_unitary(unitary)
    assert np.allclose(U, unitary)