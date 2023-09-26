#List and Lopps

for number in range(5):
    print(number)

for number in [1, 2, 3, 4, 5]:
    print(number)

supplies = ["something", "pens", "pencils", "sharpers", "rubbers"]
for index in range(len(supplies)):
    print("index" + str(index) + "in supplies is: " + supplies[index])

list = ["songs", "pashto", "parsi", "english"]
for songs in range(len(list)):
    print("the song you requested " + str(songs) + " are as below: " + list[songs])

home = ["qudrath", "ezath", "Muhib"]
for people in range(len(home)):
    print("People live in ro0m " + str(people) + " name " + home[people])

#The in and not in Operators

print("pencil" in ["something", "pens", "pencils", "sharpers", "rubbers"])

#>>> False

some_list = ["annabele", "expandable4", "wrath Of man", "avengers"]

print("spiderman" in some_list)

#>>> False

print( "pencil" not in  ["something", "pens", "pencils", "sharpers", "rubbers"])

#>>> True

print( "spiderman" not in some_list)

#>>> False

#myfreinds = ["bulbul", "duldul", "julbul", "binladin"]
#print(input(" Enter Your Freind Name..."))
#Name = input()
#if Name not in myfreinds:
#    print( Name + "is my Freind too.")
#else:
#    print("That's such a great guy " + Name)


#myfreinds = ["bulbul", "duldul", "julbul", "binladin"]
#print("Please enter you freinds name:")
#Name = input()
#if Name not in myfreinds:
#    print("Thats such a freat guy " +Name)
#else:
#    print(Name+  " is my freinds too...Great")

# Using enumerate Function
# it will produce two values 1st index and 2nd the value

machine = ["laptops", "computers", "cpus", "calculaters", "monitors"]
for index, item in enumerate(machine):
    print("index " + str(index) + " in home is: " + item)

#The enumerate() function is useful if you need both the item and the
#item’s index in the loop’s block



def convvert_add(list):
    integers = []
    for string in list:
        integers.append(int(string))
    return sum(integers)

print(convvert_add(["1", "3", "5"]))



def covert_add(string):
    string2 = []
    for values in string:
        string2.append(int(values))
    return sum(string2)
print(covert_add(["4","4"]))

    



























































