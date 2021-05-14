# Modules: Allow you to store reusable blocks of code in separate files. And are referenced using the import statement. Packages are a collections of modules






# def number_total(number_list):
#     # using for loop with initial of total
#     # number_list => a list that contains numeric values
#     # declare a new variable with name "total"
#     # has to have an initial value of 0
#     total = 0
#     # we need to use a loop to go through all the elements in this array "number_list"
#     # in JS: for(var i=0; i<=number_list.length; i++) { our code goes here }
#     for number in number_list:
#         # In JS: total += number_list[i]
#         # assume number_list = [45.6, 12.78, 10.89, 23.42]
#         # adding 45.6 to my container "total"
#         # total=total+number # total = 0 + 45.6
#         # Or the short way:
#         total += number  # the same as we wrote before: total=total+number
#     return total    # at the end of this function: return the final total









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
        string =  'An error has occurred, this function only takes number data types'
        return string


