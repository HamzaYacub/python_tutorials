#---------------------------------------- q1
#def sleep_in(weekday, vacation):
  
#  if vacation:
#    return True
#  else:
#    if not weekday:
#      return True
#    else:
#      return False

#----------------------------------------- q2
#def monkey_trouble(a_smile, b_smile):
#  if (a_smile and b_smile) or (not a_smile and not b_smile):
#    return True
#  else:
#    return False

#------------------------------------------ q3
#def sum_double(a, b):
#  sumOf = a + b
  
# if a == b:
#    sumOf = sumOf * 2
    
#  return sumOf

#------------------------------------------ q4
#def diff21(n):
#  diff = abs(21 - n)
  
#  if n > 21:
#    diff = diff * 2
    
#  return diff

#------------------------------------------ q5
#def parrot_trouble(talking, hour):
#  if hour < 7 or hour > 20:
#    if talking:
#      return True
#    else:
#      return False
#  else:
#    return False

#------------------------------------------- q6
#def makes10(a, b):
#  if (a == 10) or (b == 10) or (a + b == 10):
#    return True
#  else:
#    return False

#------------------------------------------- q7
#def near_hundred(n):
#  if n > 149:
#    near = abs(200 - n)
#  else:
#    near = abs(100-n)
  
#  if near <= 10 and near >= 0:
#    return True
#  else:
#    return False

#-------------------------------------------- q8
#def pos_neg(a, b, negative):
#  if negative:
#    if (a < 0) and (b < 0):
#      return True
#    else:
#      return False
#  else:
#    if (a < 0) and (b > 0):
#      return True
#    elif (a > 0) and (b < 0):
#      return True
#    else:
#      return False

#--------------------------------------------- q9
#def not_string(str):
#  if str[:3] == "not":
#    return str
#  else:
#    return "not " + str

#--------------------------------------------- q10
#def missing_char(str, n):
#  frontOfString = str[:n]
#  backOfString = str[n+1:]
  
  
#  newStr = frontOfString + backOfString
#  return newStr

#-------------------------------------------- q11
#def front_back(str):
  
#  if len(str) < 2:
#    return str
#  else:  
#    first_char = str[0]
#    last_char = str[-1]
#    middle = str[1:-1]
    
#    return last_char + middle + first_char

#------------------------------------------ q12
#def front3(str):
#  newStr = str[:3]
  
#  return newStr + newStr + newStr