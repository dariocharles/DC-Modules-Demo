# 3 ways to import: 1.
# 1 - helpers_module import number_sum
# 2 - from helpers_module import *
# 3 - import helpers_module. Because it is not globally available, unlike the other two ways to import you need to add module file name before calling the function eg. helpers_module.numbers_sum()

from helpers_module import *

# Calling
# 1
my_list = [4, 56, 2, 7]
print(number_sum(my_list)) 
# 2
empty_list = []
print(number_sum(empty_list)) 
# 3
error_list = [34, 78, 45, 23, "d", "6"]
print(number_sum(error_list)) 





