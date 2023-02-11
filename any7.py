def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    
    #iterating over the argument array and if any of them has a 7 the returns true if not returns false
    for num in nums:
        print(num) 
        if num == 7:
            return True
    return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

