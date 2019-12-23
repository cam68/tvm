import timeit
import tvm
nop = tvm._api_internal._nop

setup = """
import tvm
nop = tvm._api_internal._nop
"""
timer = timeit.Timer(setup=setup,
                     stmt='nop((None,..., slice(0, 100, 2)))')
timer.timeit(1)
num_repeat = 1000
print("tvm.tuple_slice_ellipsis_combo:", timer.timeit(num_repeat) / num_repeat)


setup = """
import numpy as np
"""

timer = timeit.Timer(setup=setup,
                     stmt='np.empty((1,2,1))')
timer.timeit(1)
print("numpy.emmpty:", timer.timeit(num_repeat) / num_repeat)


setup = """
import tvm
nop = tvm._api_internal._nop
"""
timer = timeit.Timer(setup=setup,
                     stmt='nop("mystr")')
timer.timeit(1)
num_repeat = 1000
print("tvm.str_arg:", timer.timeit(num_repeat) / num_repeat)
