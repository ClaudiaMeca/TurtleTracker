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
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	    -46.309	6	0	-126	529	3	401 651134.7	0"

#Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specific items in the list
record_id = lineData[0]  #ARGOS tracking record ID
obs_date = lineData[2] #Observation date
ob_lc = lineData[4] #Observation Location Class
obs_lat = lineData[6] #ObservationLatitude
obs_lon = lineData[7] #Observation Longitude

#Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#%%Read data directly from ARGOS file

#Create a variable pointing to the data file
argos_data = './Data/Raw/Sara.txt'
#Create a file object from the file
argos_obj = open(argos_data, 'r')
#Read contents of file into a list
argos_list = argos_obj.readlines()
#close file
argos_obj.close()
#Pretend we read one line of data from the file
argos_str = argos_list[18]
#Split the string into a list of data items
argos_data = argos_str.split()
#Extract items in list into variables
record_id = argos_data[0]  #ARGOS tracking record ID
obs_date = argos_data[2] #Observation date
ob_lc = argos_data[4] #Observation Location Class
obs_lat = argos_data[6] #ObservationLatitude
obs_lon = argos_data[7] #Observation Longitude

#Print the location of Sara
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#%% Tips
#Reading text files

fileObj = open('Data/Raw/Sara.txt', 'r')
lineString2 = fileObj.readline(); print (lineString2)
lineList = fileObj.readlines(); print(lineList[-1])
fileObj.close()

# Writing to text files

newFile = open('newfile.txt', 'w')
newFile.write("Hello planet\nIt's me")
newFile.close()

# Appending to text files
open('newfile.txt', 'a').write("See what I did here")