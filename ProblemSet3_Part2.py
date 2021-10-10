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
#%% Task 5

#read in loitering_events_20180723.csv
fileLoit = open(file = "loitering_events_20180723.csv", mode = 'r')

#create list of all lines in fileLoit
lineLoit = fileLoit.readlines()

#close loitering_events_20180723.csv
fileLoit.close()

#create list of header items in fileLoit
headersLoit = lineLoit[0]
headers = headersLoit.split(',')

#extract index values for header items

mmsi_indx = headers.index('transshipment_mmsi')
start_lat_indx = headers.index('starting_latitude')
start_long_indx = headers.index('starting_longitude')
end_lat_indx = headers.index('ending_latitude')

#create empty dictionary
loitDict = {}

#begin loop
for loitString in lineLoit:
    if loitString[0] in "t":
        continue

#split lines into list of data items   
    loitData = loitString.split(',')
        
#create objects individual data items    
    mmsi2 = loitData[mmsi_indx]
    start_lat = float(loitData[start_lat_indx])
    start_long = float(loitData[start_long_indx])
    end_lat = float(loitData[end_lat_indx])
    
     #select vessels crossing equator AND starting between 165 and 170 degrees
     #longitude
    if (165 < start_long < 170) and ((start_lat < 0 < end_lat) or\
        (start_lat < 0 < end_lat)):

        #populate loitDict with vessels crossing equator and starting between 
        #165 and 170 degrees longitude
        loitDict[mmsi2] = start_long  
        
        print("Vessel # " + mmsi2 + " flies the flag of " + vesselDict[mmsi2])     