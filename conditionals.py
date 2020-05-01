mark = int(input("Enter in your mark:"))

if mark > 85:
    print("Distinction")
elif mark <= 85 and mark >= 65:
    print("Pass")
else:
    print("Fail")


#----------------------------------
# more improved version with input validation

#while mark:

#    if mark <= 100 and mark >= 85:
#        print("Distinction")
#        break
#    elif mark < 85 and mark >= 65:
#        print("Pass")
#        break
#    elif mark < 65 and mark >= 0:
#        print("Fail")
#        break
#    else:
#        mark = int(input("Your mark has to be between 0 - 100, please enter it again correctly: "))

