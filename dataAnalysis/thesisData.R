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
origamidata = read.csv(file.choose(),header=TRUE)

#Display the column names in the console.
names(origamidata)

# Get summary statistics for total time using the summary() and sd() commands.
# Summary will give you the mean and the five number summary but will not give the standard deviation.
# To get a sample standard deviation use sd().
summary(origamidata$total_time)
sd(origamidata$total_time)

# Generate boxplot(s) that compares the overall time elapsed to certain columns.

#origami type (Boat, Swan)
boxplot(origamidata$total_time~origamidata$origami_type, main = "Comparison of Overall Time Elapsed based on Origami Type", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")
#task type (First1, Second1, Third1, Test1, First2, Second2, Third2, Test2)
boxplot(origamidata$total_time~origamidata$task_type, main = "Comparison of Overall Time Elapsed based on Task Type", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")
#method type (Normal, Augmented)
boxplot(origamidata$total_time~origamidata$method_type, main = "Comparison of Overall Time Elapsed based on Method Type", col = blues9, horizontal = TRUE, xlab = "Total Time Elapsed (ms)")


# Calculate range from 0 to max value of cars and trucks
g_range <- range(0, origamidata$total_time)

plot(origami_data, type="o", col="blue", ylim=g_range, 
     axes=FALSE, ann=FALSE)

# Make x axis using Mon-Fri labels
axis(1, at=1:5, lab=c("Mon","Tue","Wed","Thu","Fri"))

# Make y axis with horizontal labels that display ticks at 
# every 4 marks. 4*0:g_range[2] is equivalent to c(0,4,8,12).
axis(2, las=1, at=4*0:g_range[2])

# Create box around plot
box()
