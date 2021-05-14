# 3 ways to import: 1.
# 1 - helpers_module import number_sum
# 2 - from helpers_module import *
# 3 - import helpers_module. Because it is not globally available, unlike the other two ways to import you need to add module file name before calling the function eg. helpers_module.numbers_sum()
from helpers_module import *

# Step1: create virtual environmnet
# >>python -m venv my-venv <Virtual_Env_folder_name>
# Step2: Activate it
# >>tutorial-env/bin/activate
# Step3: Install the required package:
# >> pip install colorama
# Step4: write the code
# Step5: Creating the "requirements.txt" - do at end
# >> pip freeze > requirements.txt

# import Colorama
from colorama import Fore, Back

# Calling
# 1
my_list = [45, 7, 65, 23, 78]
print(Fore.BLACK+Back.YELLOW + str(number_sum(my_list)))
print(Fore.RESET + Back.RESET)



# 2
empty_list = []
print(Fore.BLACK+Back.RED + number_sum(empty_list))
print(Fore.RESET + Back.RESET)



# 3
error_list = [34, 78, 45, 23, "d", "6"]
print(Fore.RED+Back.CYAN + number_sum(error_list))
print(Fore.RESET + Back.RESET)
