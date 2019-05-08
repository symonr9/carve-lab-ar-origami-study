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



#Define and exclude specified variables

#Augmented Cues Data
inputdata <- initial_inputdata[c(1:137), c(1:23)]

#Use to only see learning task data
origamidata1 <- subset(inputdata, task_type == "First1" || task_type == "Second1" || task_type == "Third1" || task_type == "First2" || task_type == "Second2" || task_type == "Third2")
#method type (Normal, Augmented)
boxplot(origamidata1$total_time~origamidata1$method_type, main = "Time Elapsed (Learning Tasks) w/ Cues", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")


#Use to only see assessment task data
origamidata2 <- subset(inputdata, task_type == "Test1" || "Test2")
#method type (Normal, Augmented)
boxplot(origamidata2$total_time~origamidata2$method_type, main = "Time Elapsed (Test Tasks) w/ Cues", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")


#augmented manual data
inputdata2 <- initial_inputdata[c(138:209), c(1:23)]


#Use to only see learning task data
origamidata3 <- subset(inputdata2, task_type == "First1" || task_type == "Second1" || task_type == "Third1" || task_type == "First2" || task_type == "Second2" || task_type == "Third2")
#method type (Normal, Augmented)
boxplot(origamidata3$total_time~origamidata3$method_type, main = "Time Elapsed (Learning Tasks) w/ A. Manual", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")


#Use to only see assessment task data
origamidata4 <- subset(inputdata2, task_type == "Test1")
#method type (Normal, Augmented)
boxplot(origamidata4$total_time~origamidata4$method_type, main = "Time Elapsed (Test Tasks) w / A. Manual", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")




#Display the column names in the console.
names(origamidata)

# Get summary statistics for total time using the summary() and sd() commands.
# Summary will give you the mean and the five number summary but will not give the standard deviation.
# To get a sample standard deviation use sd().
#summary(origamidata$total_time)
#sd(origamidata$total_time)

# Generate boxplot(s) that compares the overall time elapsed to certain columns.

#origami type (Boat, Swan)
#boxplot(origamidata$total_time~origamidata$origami_type, main = "Comparison of Overall Time Elapsed based on Origami Type", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")
#task type (First1, Second1, Third1, Test1, First2, Second2, Third2, Test2)
#boxplot(origamidata$total_time~origamidata$task_type, main = "Comparison of Overall Time Elapsed based on Task Type", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")


# Calculate range from 0 to max value of cars and trucks
#g_range <- range(0, origamidata$total_time)

#plot(origamidata, type="o", col="blue", ylim=g_range, 
#     axes=FALSE, ann=FALSE)

# Make x axis using Mon-Fri labels
#axis(1, at=1:5, lab=c("Mon","Tue","Wed","Thu","Fri"))

# Make y axis with horizontal labels that display ticks at 
# every 4 marks. 4*0:g_range[2] is equivalent to c(0,4,8,12).
#axis(2, las=1, at=4*0:g_range[2])

# Create box around plot
#box()
