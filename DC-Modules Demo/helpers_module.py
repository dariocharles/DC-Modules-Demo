# Modules: Allow you to store reusable blocks of code in separate files. And are referenced using the import statement. Packages are a collections of modules

# Function to find the sum
def number_sum(list):
    # try/except - the try sees if there are an errors and if there are then the except handles the error
    try:
       # declaring variable "sum"
        sum = 0
        # if/else statement to see if the list has any elements
        if not list:
            string = "The list doesn't have any elements!"
            return string
        else:
            # using a for loop to iterate through all the elements in the "list"
            for number in list:
                sum += number
            return sum
    except Exception:
        string = 'An error has occurred, this function only takes number data types'
        return string
