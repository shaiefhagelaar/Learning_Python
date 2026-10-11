
#basic's
print("Hello " + (name := input('Enter your name: ')) + "!, characters: " + str(len(name)))

#switching contents variables
glass1 = "milk"
glass2 = "juice"

glass1, glass2 = glass2, glass1

#taking user input, store into variables and combine the two into a name

print ("Welcome to the Band Name Generator")

location_lived = input("Where are you form?")

pet_name = input("What is the name of your pet?")

print("Your Band name is: " + location_lived + " " + pet_name)
