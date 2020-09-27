# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:01:55 2020

@author: clauv
"""
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
# {obs_date}

#record_id = lineData[0, 4]  #ARGOS tracking record ID
#obs_date = obs_dateTime.split()[10, 17] #Observation date
#ob_lc = lineData[18, 21] #Observation Location Class
#obs_lat = lineData[23, 24] #ObservationLatitude
#obs_lon = lineData[25, 30] #Observation Longitude