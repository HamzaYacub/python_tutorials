#------------------------------------------------------------ q1
#def cigar_party(cigars, is_weekend):
#  if (cigars >= 40 and cigars <= 60) and (not is_weekend):
#    return True
#  elif is_weekend:
#    if cigars >= 40:
#      return True
#    else:
#      return False
#  else:
#    return False
    
#------------------------------------------------------------ q2
#def date_fashion(you, date):
#  if (you <= 2) or (date <= 2):
#    result = 0
#  elif (you >= 8) or (date >= 8):
#    result = 2
#  else:
#    result = 1
  
#  return result

#----------------------------------------------------------- q3
#def squirrel_play(temp, is_summer):
#  if is_summer:
#    if (temp >= 60) and (temp <= 100):
#      return True
#    else:
#      return False
#  else:
#    if (temp >= 60) and (temp <=90):
#      return True
#    else:
#      return False

#-------------------------------------------------------- q4
#def caught_speeding(speed, is_birthday):
#  if is_birthday:
#    if speed >= 81 + 5:
#      ticket = 2
#    elif speed <= 60 + 5:
#      ticket = 0
#    else:
#      ticket = 1
#  else:
#    if speed >= 81:
#      ticket = 2
#    elif speed <= 60:
#      ticket = 0
#    else:
#      ticket = 1
  
#  return ticket

#---------------------------------------------------------- q5
#def sorta_sum(a, b):
  
#  sumOf = a + b
  
#  if sumOf >= 10 and sumOf <= 19:
#    sumOf = 20
    
#  return sumOf

#---------------------------------------------------------- q6
#def alarm_clock(day, vacation):
#  if vacation:
#    if day == 0 or day == 6:
#      alarm = "off"
#    else:
#      alarm = "10:00"
#  else:
#    if day == 0 or day == 6:
#      alarm = "10:00"
#    else:
#      alarm = "7:00"
  
#  return alarm

#--------------------------------------------------------- q7
#def love6(a, b):
#  if (a == 6 or b == 6) or (abs(a - b) == 6) or (a + b == 6):
#    return True
#  else:
#    return False

#--------------------------------------------------------- q8
#def in1to10(n, outside_mode):
#  if outside_mode:
#    if n <= 1 or n >= 10:
#      return True
#    else:
#      return False
#  else:
#    if n <= 10 and n >= 1:
#      return True
#    else:
#      return False

#--------------------------------------------------------- q9
#def near_ten(num):
#  remainder = num % 10
  
#  if remainder <= 2 or remainder >= 8:
#    return True
#  else:
#    return False