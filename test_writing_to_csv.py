import csv 

#mode 'a' is for appending data onto csv file.
with open('origami_data.csv', mode='a') as dataFile:
	dataWriter = csv.writer(dataFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL);
	
	dataWriter.writerow(["Swan", 'First1', 'Normal', 'None', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2019-02-21 14:05:09']);
	
#	dataWriter.close();