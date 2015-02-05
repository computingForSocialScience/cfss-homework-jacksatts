import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)


### enter your code below
def get_avg_latlng(data):
	'''computes the average latitude and longitude and 
	constructs permits in Hyde Park and prints it to the console'''
	numrows = len(data)
	sumlatitude = 0
	sumlongitude = 0
	for row in data:
		sumlatitude = float(row[128]) + sumlatitude
		sumlongitude = float(row[129]) + sumlongitude
	l = sumlatitude/numrows
	o = sumlongitude/numrows
	return (l, o)

hpp = readCSV('permits_hydepark.csv')
print get_avg_latlng(hpp)

#clean HP dataset
cleaned_zip = []
for row in readCSV('permits_hydepark.csv'):
	if row[28] == "":
		pass
	elif len(row[28]) == 6:
		cleaned_zip.append(int(row[28].split('-')[0]))
	else:
		cleaned_zip.append(int(row[28]))

#print cleaned_zip

#note - I was told by Hunter to use Contractor 1 zipcode, 
#and to leave ignore the blank zipcode if one was not included.

#make a histogram!

import matplotlib.pyplot as plt
import numpy as np

#print np.unique(cleaned_zip, return_counts=True)

def zip_code_barchart(data):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	unique_zip_array = np.unique(data)
	unique_zip = unique_zip_array.tolist()
	zip_counts = np.unique(data, return_counts=True)
	ax.bar(range(len(unique_zip)), zip_counts[1])
	ax.set_title("Hyde Park Zip Code Bar Chart")
	ax.set_xlabel("Zip Codes")
	ax.set_ylabel("Frequency")
	xTickMarks = [str(x) for x in unique_zip]
	ax.set_xticks(np.arange(37)+.5)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=45, size = 8)
	#plt.show()
	fig.savefig("hpzip_bar.jpg")

zip_code_barchart(cleaned_zip)


#combine into an executable program
def zip_code_barchart2(data):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	unique_zip_array = np.unique(data)
	unique_zip = unique_zip_array.tolist()
	zip_counts = np.unique(data, return_counts=True)
	ax.bar(range(len(unique_zip)), zip_counts[1])
	ax.set_title("Hyde Park Zip Code Bar Chart")
	ax.set_xlabel("Zip Codes")
	ax.set_ylabel("Frequency")
	xTickMarks = [str(x) for x in unique_zip]
	ax.set_xticks(np.arange(37)+.5)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=45, size = 8)
	plt.show()
	#ax.savefig("hpzip_bar.jpg")


if sys.argv[1]=="latlong":
	print get_avg_latlng(hpp)
elif sys.argv[1]=="hist":
	zip_code_barchart2(cleaned_zip)