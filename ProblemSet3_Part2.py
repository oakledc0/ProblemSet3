#-----------------------------------------------------------------------------
#
# Author: Cal Oakley
# Date: Fall 2021
#
#-----------------------------------------------------------------------------
#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)
#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)
#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for lineString in lineList:
    if lineString[0] in ("m"):
        continue
#Split the data into values
    lineData = lineString.split(',')
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]
#Extract the fleet value
    fleet = lineData[fleet_idx]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
#%% Task 4.4
#create "vesselID" object
vesselID = "258799000"
#lookup fleet value for MMSI "258799000"
vesselDict[vesselID]
#print "Vessel # 258799000 flies the flag of Norway"
print("Vessel # " + vesselID + " flies the flag of " + vesselDict[vesselID])    