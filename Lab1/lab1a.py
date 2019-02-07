# Name: Wei Minn
# Section: G5

# lab1a

# fill up the admit method to return either True or False depending on the sex and age
def admit(sex,age):
  if(sex == 'M'):
    if (age < 23):
      return False
    else: return True
  elif(sex == 'F'):
    if (age < 18):
      return False
    else: return True
