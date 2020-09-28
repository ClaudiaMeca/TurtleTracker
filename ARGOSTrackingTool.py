#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Claudia Meca (cm498@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#%% Parsing one line of tracking data
#Copy and paste a line of data as the lineString variable value
#lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	    -46.309	6	0	-126	529	3	401 651134.7	0"

#Use the split command to parse the items in lineString into a list object
#lineData = lineString.split()

# Assign variables to specific items in the list
#record_id = lineData[0]  #ARGOS tracking record ID
#obs_date = lineData[2] #Observation date
#ob_lc = lineData[4] #Observation Location Class
#obs_lat = lineData[6] #ObservationLatitude
#obs_lon = lineData[7] #Observation Longitude

#Print information to the use
#print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#%% Ask the user for a date, specifying the format
user_date = input("Enter a date to search for Sara (M/D/YYYY):")

###Read data directly from ARGOS file
#Create a variable pointing to the data file
argos_file = './Data/Raw/Sara.txt'
#Create a file object from the file
argos_obj = open(argos_file, 'r')
#Read contents of file into a list
argos_list = argos_obj.readlines()
#close file
argos_obj.close()

# create dictionaries
date_dict = {}
coord_dict = {}

# Using a for loop to read all the data lines
for argos_str in argos_list:
    if argos_str[0] in ("#", "u"): continue

    argos_data = argos_str.split() #Split the string into a list of data items

    record_id = argos_data[0]  ##Extract items in list into variables, ARGOS tracking record ID
    obs_date = argos_data[2] #Observation date
    obs_lc = argos_data[4] #Observation Location Class
    obs_lat = argos_data[6] #ObservationLatitude
    obs_lon = argos_data[7] #Observation Longitude

    if obs_lc in ("1", "2", "3"):
        #print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}") #Print the location of Sara
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat, obs_lon) # add items to dictionaries

# create empty list to hold matching keys
matching_keys = []

# loop through all key, value pairs in the date_dictionary
for date_item in date_dict.items():
    #get the key and date of the dictionary item
    the_key, the_date = date_item
    #see if the date (the value) matches the user date
    if the_date == user_date:
        #If so, add the key to the list
        matching_keys.append(the_key)
        
# Reveal locations for each key in matching keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
    
# Check that at least one key was returned; tell the user if not.
if len(matching_keys) == 0:
    print("No observations were recorded for {}".format(user_date))
#%% using a while loop to read all the data lines (less memory required)
#argos_file = './Data/Raw/Sara.txt'
#argos_obj = open(argos_file, 'r')
#argos_str2 = argos_obj.readline()

#while argos_str2:
#    if argos_str2[0] in ("#", "u"): continue
    
#    argos_data2 = argos_str2.split() #Split the string into a list of data items
    
#    record_id = argos_data2[0]  ##Extract items in list into variables, ARGOS tracking record ID
#    obs_date = argos_data2[2] #Observation date
#    ob_lc = argos_data2[4] #Observation Location Class
#    obs_lat = argos_data2[6] #ObservationLatitude
#    obs_lon = argos_data2[7] #Observation Longitude
    
#    print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}") #Print the location of Sara
    
#    argos_str2 = argos_obj.readline() # move to next line    

#argos_obj.close() # close file
#%% Tips
#Reading text files

#fileObj = open('Data/Raw/Sara.txt', 'r')
#lineString2 = fileObj.readline(); print (lineString2)
#lineList = fileObj.readlines(); print(lineList[-1])
#fileObj.close()

# Writing to text files

#newFile = open('newfile.txt', 'w')
#newFile.write("Hello planet\nIt's me")
#newFile.close()

# Appending to text files
#open('newfile.txt', 'a').write("See what I did here")