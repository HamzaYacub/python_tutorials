#------------------------------------------------ q1
#def hello_name(name):
#  return "Hello " + name + "!"

#------------------------------------------------ q2
#def make_abba(a, b):
#  return a + b + b + a

#------------------------------------------------ q3
#def make_tags(tag, word):
#  frontTag = "<" + tag + ">"
#  backTag = "</" + tag + ">"
  
#  return frontTag + word + backTag

#------------------------------------------------- q4
#def make_out_word(out, word):
#  halfway = len(out) / 2
  
#  frontOut = out[:halfway]
#  backOut = out[halfway:]
  
#  return frontOut + word + backOut

#------------------------------------------------- q5
#def extra_end(str):
#  newStr = str[-2:]
  
#  return newStr + newStr + newStr

#------------------------------------------------- q6
#def first_two(str):
#  if len(str) < 2:
#    return str
#  else:
#    return str[:2]

#-------------------------------------------------- q7
#def first_half(str):
#  length = len(str) / 2
  
#  newStr = str[:length]
  
#  return newStr

#--------------------------------------------------- q8
#def without_end(str):
#  return str[1:-1]

#--------------------------------------------------- q9
#def combo_string(a, b):
#  if len(a) < len(b):
#    return a + b + a
#  else:
#    return b + a + b

#--------------------------------------------------- q10
#def non_start(a, b):
#  return a[1:] + b[1:]

#--------------------------------------------------- q11
#def left2(str):
#  if len(str) < 2:
#    return str
#  else:
#    frontStr = str[:2]
#    backStr = str[2:]
    
#    return backStr + frontStr
