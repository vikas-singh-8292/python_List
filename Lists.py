bicycles = ["trek", 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[4])
message= "My first bicycles was "+bicycles[0].title()+"."
print(message)
# Example: 1
fridName = ["vikash","Arjun","Prakash","Awesome"]
print(fridName[0])
print(fridName[1])
print(fridName[2])
print(fridName[3])




# Changing, Adding, and Removing Element
 #Changing 
bicycles[0]="Vikash"
print(bicycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[1]='Splender'
print(motorcycles)



 #Making List using append()
motorcycles = []
motorcycles.append("Honda")
motorcycles.append("tata")
motorcycles.append("Hero")
print(motorcycles)



# Inserting Elements into a List using insert()

motorcycles.insert(0 ,'ducati')
print(motorcycles)




# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)



#Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_morocycle = motorcycles.pop()
print(motorcycles)
print(popped_morocycle)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title()+".")




#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
too_expensive = 'suzuki'
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# Avoiding Index Errors When Working with Lists


cars = ["Bmw","ferrari","Suzuki"]
print(cars[3])
print(cars[-1])
motor = []
print(motor[-1])
