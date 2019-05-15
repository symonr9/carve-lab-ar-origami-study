#############################################################################################################
# File Name: thesisData.R
# Author: Symon Ramos
# Date Created: 5/7/19
# Last Updated: 5/7/19
# Description: This file will take the exported csv file from the data collected in the mySQL database for 
# the pilot study data and display the data in the form of a graph. Statistical information will also be
# collected.
#############################################################################################################

#Read the data within the csv file exported from the mySQL database.
initial_inputdata = read.csv(file.choose(),header=TRUE)

#As of 5/7/19: 
#   c(1:137) covers all augmented cues data
#   c(138:209) covers all augmented manual data
#
#   c(1:82) covers all augmented cues data where augmentations were not emphasized
#   c(83:137) covers all augmented cues data where augmentations were emphasized


#Define and exclude specified variables

#Augmented Cues Data
inputdata <- initial_inputdata[c(1:137), c(1:23)]

#Use to only see learning task data
origamidata1 <- subset(inputdata, task_type == "First1" || task_type == "Second1" || task_type == "Third1" || task_type == "First2" || task_type == "Second2" || task_type == "Third2")
#method type (Normal, Augmented)
boxplot(origamidata1$total_time~origamidata1$method_type, main = "Task Time (Practice Trials) Pilot Design", col = blues9, horizontal = TRUE, xlab = "Task Time (sec)")



#Use to only see assessment task data
origamidata2 <- subset(inputdata, task_type == "Test1" || "Test2")
#method type (Normal, Augmented)
boxplot(origamidata2$total_time~origamidata2$method_type, main = "Task Time (Test Trials) Pilot Design", col = blues9, horizontal = TRUE, xlab = "Task Time (sec)")


#augmented manual data
inputdata2 <- initial_inputdata[c(138:209), c(1:23)]


#Use to only see learning task data
origamidata3 <- subset(inputdata2, task_type == "First1" || task_type == "Second1" || task_type == "Third1" || task_type == "First2" || task_type == "Second2" || task_type == "Third2")
#method type (Normal, Augmented)
boxplot(origamidata3$total_time~origamidata3$method_type, main = "Task Time (Practice Trials) Revised Design", col = blues9, horizontal = TRUE, xlab = "Task Time Elapsed (sec)")


#Use to only see assessment task data
origamidata4 <- subset(inputdata2, task_type == "Test1")
#method type (Normal, Augmented)
boxplot(origamidata4$total_time~origamidata4$method_type, main = "Task Time (Test Trials) Revised Design", col = blues9, horizontal = TRUE, xlab = "Task Time Elapsed (sec)")



#Display the column names in the console.
names(origamidata)

# Get summary statistics for total time using the summary() and sd() commands.
# Summary will give you the mean and the five number summary but will not give the standard deviation.
# To get a sample standard deviation use sd().
summary(origamidata$total_time)
sd(origamidata$total_time)
