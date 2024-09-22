def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    
    # Return bool response for palidrome
    return word == word[::-1]
    
#x = lab2Question1('')
#print(x)
#x = lab2Question1('beer')
#print(x)
#x = lab2Question1('iamai')
#print(x)

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    
    #This an intensive computation in recursive mode
    #f(n) = f(n-1)+f(n-2) if n>1
    #Declaration field

    #return 0 or 1 if the input number is less than 3
    # will stop the recursive call one this number is hit
    if number_val <= 2:
        return [0, 1][:number_val]
    
    #Recursive call entry with decreasing input value
    mList = lab2Question2(number_val - 1)
    
    #store the sum of the last two numbers
    mList.append(sum(mList[-2:]))
    
    #return the sum
    return mList
  

#test calls for verification
#x = lab2Question2(0)
#print(x)
#x = lab2Question2(-1)
#print(x)
#x = lab2Question2(7)
#print(x)

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    
    #Set the string to lower case to prevent the bypass of capital letters - ACSI value of letters and capital are different
    #ie C is 67 which is not equal to c which is 97
    #Solve by converting to lower case and checking the repititions
    string1 = str1.lower()
    string2 = str2.lower()
    index = string1.count(string2)
    
    #return the count
    return index
    
#x = lab2Question3("Coding is cool, but I was a code monkey","co")
# print(x)
#x = lab2Question3("Attitude is everything", "tt")
#print(x)
#x = lab2Question3("Superstitious and superfluous", "super")
#print(x)

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list

    #Check for unequal length between the strings
    if len(list1) != len(list2):
        #as with the requiremetns return an blank list
        return []
    
    #start with a blank list
    sum_List = []
    #go through every character of the first string
    for i in range(len(list1)):
        #sum the values of the strings at each character
        sum = list1[i] + list2[i]
        #produce a list of the sums
        sum_List.append(sum)

    # return new list sum   
    return sum_List

#x = lab2Question4([1,2,3,4],[1,2,3,4])
#print(x)
#x = lab2Question4([1, 2, 3, 4], [5, 6, 7])
#print(x)
#x = lab2Question4([1, 2, 8, 3], [4, 5, 6, 7])
#print(x)

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    
     
     #Declaration Field
    password = None
    ans = False
    #print('The password must be over 8 characters, have 1 upper case character, have at least 1 lower case character and contain 1 number')
    #print('Please enter a correctly format Passwordpassword')
    
    #Get the user's input from the keyboard
    password = input()
    
    #Continue until a valid password is found through a while loop
    while ans == False:
        #call another method to return whether the pasword is in the correct formatting
        ans = isValidPassword(password)
        #if false re-ask for the user;s password
        if ans == False:
            #print('The password must be over 8 characters, have 1 upper case character, have at least 1 lower case character and contain 1 number')
            #print('Please re-enter a correct password')
            password = input()
        
    #return the password if correct   
    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number

    #Declaration Field
    #Set boolean values to false as default
    is_upper = False
    is_lower = False
    is_digit = False
    
    #Check length of password for at least 8 characters
    ans = not bool(len(password) < 8)
    if ans == False:
        return ans
    
    #Check for an upper case letter in the input string from the user
    for l in password:
        #if found, set the boolean condition and break from checking the rest of the string
        if l.isupper() is True:
            is_upper = True
            break

    #Check for an lower case letter in the input string from the user
    for l in password: 
        #if found, set the boolean condition and break from checking the rest of the string       
        if l.islower() is True:
            is_lower = True
            break

     #Check for an lower case letter in the input string from the user
    for l in password:
        #if found, set the boolean condition and break from checking the rest of the string 
        if l.isdigit() is True:
            is_digit = True
            break
    #return the boolean condition of the three flags to the calling function
    return(is_upper and is_lower and is_digit)

         
#x = lab2Question5()
#print(x)

