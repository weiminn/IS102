# Name: Wei Minn
# Section: G5

# lab1b

# fill up the weight_category method to return either "underweight", "overweight" or "normal" 
# depending on the height (in cm) and weight (in kg)
def weight_category(weight, height):
  
  bmi = weight/((float(height)/100)**2)
  
  if (bmi < 18.5):
    return "underweight"
  elif (bmi > 25):
    return "overweight"
  else:
    return "normal"
