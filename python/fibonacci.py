import sys
import os
from typing import List

# fmt:off
#
# Let's assume the module was build by CMake commands in the project root
# on Linux-like system:
#
#   cmake -B ./build && cmake --build ./build
#
# in this case our new-created Python module `pyfibonacci` will be placed in
# the dir `./build/cpp/`.
#
# Adding this path to the module search path list (replace "../build/cpp" if
# you built or put the module to another path):
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.dirname(module_dir)
module_path = os.path.join(project_root_dir, 'build/cpp')
sys.path.append(module_path)

# Importing out module:
import pyfibonacci
# fmt:on


the_answer = pyfibonacci.the_answer
what = pyfibonacci.what


def calc(index: int) -> int:
    if index <= 1:
        return index

    return calc(index - 1) + calc(index - 2)


def calc_externally(index: int) -> int:
    return pyfibonacci.calc(index=index)


class SeriesCalculator:
    def __init__(self) -> None:
        self._indexes = []

    def put_index(self, index: int) -> None:
        self._indexes.append(index)

    def calc(self) -> List[int]:
        result = []
        for index in self._indexes:
            result.append(calc(index=index))
        return result


class ExternalSeriesCalculator:
    def __init__(self) -> None:
        self._calc = pyfibonacci.SeriesCalculator()

    def put_index(self, index: int) -> None:
        self._calc.put_index(index=index)

    def calc(self) -> List[int]:
        return self._calc.calc()
