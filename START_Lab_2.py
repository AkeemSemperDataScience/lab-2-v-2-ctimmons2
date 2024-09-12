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

    #base case
    first = 0
    second = 1

    #create initial list
    mList=[first, second]
    
    number_val -= 2

    while number_val>0:
        
        temp = second
        second = first + second
        first = temp
        mList.append(second)
        number_val -= 1

    return mList

#x = lab2Question2(0)
#print(x)
#x = lab2Question2(1)
#print(x)
#x = lab2Question2(10)
#print(x)

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    
    index = str1.count(str2)
    if index == 0:
        print('String not found.')
    else:
        print('Found at index', index)
    return index
    
#x = lab2Question3('coding is cool','co')
#print(x)
#x = lab2Question3('coding is cool','beer')
#print(x)

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    sum_List = []
    for i in list1:
        sum = list1[i-1] + list2[i-1]
        sum_List.append(sum)
        print(sum_List)
    return sum_List

#x = lab2Question4([1,2,3,4],[1,2,3,4])
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
    password = input()
    
    while ans == False:
        ans = isValidPassword(password)
        if ans == False:
            #print('The password must be over 8 characters, have 1 upper case character, have at least 1 lower case character and contain 1 number')
            #print('Please re-enter a correct password')
            password = input()
        
        
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
    
    #Check length of password
    ans = not bool(len(password) < 8)
    if ans == False:
        return ans
    
    #Check for an upper case letter
    for l in password:
        if l.isupper() is True:
            is_upper = True
            break
    
    for l in password:        
        if l.islower() is True:
            is_lower = True
            break

    for l in password:
        if l.isdigit() is True:
            is_digit = True
            break
    return(is_upper and is_lower and is_digit)

     
        
#x = lab2Question5()
#print(x)

