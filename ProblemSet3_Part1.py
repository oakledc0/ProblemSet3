#-----------------------------------------------------------------------------
#
# Author: Cal Oakley
# Date: Fall 2021
#
#-----------------------------------------------------------------------------
# %% /*-PS3: Code Block Task 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = "20322" 

print(mountain + ', formerly\nknown as "' + nickname + '",')
print("is " + elevation + ' above sea level.' )
# %% /*-PS3: Code Block Task 2--*/
# create 'dataFolder' object
dataFolder = "W:\859_data\\tri_state"
#create 'dataList' object
dataList = ["\\roads.shp", "\\road_types.dbf", "\\naip_imagery.tif"]
#create "userItem" object
userItem = "\\streams.shp"
#append dataList 
dataList.append(userItem)
#concatenate and print file path names
for x in dataList:
    print(dataFolder + x)
# %% /*-PS3: Code Block Task 3--*/
#create empty list "userNumbers"
userNumbers = []
#set number of inputs
for i in range(0,3):
    #add inputs to "userNumbers" as integers
    userNumbers.append(int(input(prompt= "Enter an integer: ")))
    #sort input integers
    userNumbers.sort()
print(userNumbers[2])
# %% /*-PS3: Code Block CHALLENGE QUESTION--*/
userNumbers = []

for i in range(0,3):
    userNumbers.append(int(input(prompt= "Enter an integer: ")))
    userNumbers.sort(reverse = True)
print(userNumbers)
