patient_name = input("Enter patient's name: ")

while True:
  try:
    age = input("Enter patient's age: ")
    if age.isdigit(): #if the input is contains only digits
      age=int(age) #then it converts the string input into an integer
    else:   
       raise ValueError() #if it isn't a number return an error and execute the code after line 13
    if 0 <= age <= 120: #this checks that the age is within 0-120 to limit 10,000 year old vampires from checking in
        break #breaks free from the loop if all of the 
    raise ValueError() #if it isn't between those numbers return an error and execute code after line 13
  except ValueError:
    print("Please enter a valid age.")

question = input("Returning patient? (y/n): ")

while question != "y" and question != "n": #same as above but this determines that the input can only be y or n
    question = input("Please answer 'y' or 'n': ")
    

while True:
  try:
    ssn = input("Enter patient's Social Security number: ")
    if ssn.isdigit() and len(ssn) == 9: #determines that the input is only numbers and is a 9 digit string
      ssn=str(ssn) #if it meets these requirements then convert it into a string so it can be concatonated at the end
      break #then break free from the loop
    else:   #if it doesn't meet these requirements return an error and loop until it meets them
      raise ValueError()
  except ValueError:
    print("Please enter a valid Social Security number.")

#concatonate the variables with some preset strings for formatting
print("Name: " + patient_name) #These print statements could instead enter the information into a form.
print("Age: " , age)
print("SSN: " + ssn[0:3] + "-" + ssn[3:5] + "-" + ssn[5:10]) #concatonating the ssn we converted to a str earlier

if question == "n":
    print("This is a new patient.")

elif question == "y":
    print("This is a returning patient.")
