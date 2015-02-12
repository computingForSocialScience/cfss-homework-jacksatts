import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    """creates x and y values to use in the plotBarChart function"""
    f_artists = open('artists.csv') #reads/opens csv file I made of the artists
    f_albums = open('albums.csv') #reads/opens csv file I made of the artist's albums

    artists_rows = csv.reader(f_artists) #used to later call the data rows in the artists csv file
    albums_rows = csv.reader(f_albums) #used to later call the data rows in the albums csv file

    artists_header = artists_rows.next() #used to call the heading row in artists.csv
    albums_header = albums_rows.next() #used to call the heading row in albums.csv

    artist_names = [] #creates an empty list of artist names
    
    decades = range(1900,2020, 10) #makes a list of decades, every 10 years from 1900 to 2020
    decade_dict = {} #creates an empty dictionary to fill in the following for loop
    for decade in decades: 
        decade_dict[decade] = 0 #adds the decades from range function and fills the empty dictionary
    
    for artist_row in artists_rows: #loops through all rows in artist.csv
        if not artist_row: 
            continue #if there is no data in the artist row, don't stop the loop, just skip (Checks if the row is a header row)
        artist_id,name,followers, popularity = artist_row #add the info from artist row into variable artist_row
        artist_names.append(name) #appends the name of the artist to the list artist_names

    for album_row  in albums_rows: #loops through data rows from albums.csv
        if not album_row:
            continue #if there is no data in the album row, don't stop the loop, just skip (Checks if the row is a header row)
        artist_id, album_id, album_name, year, popularity = album_row #assigns the elements from the rows to a variable, album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)): #if the year is greater than one decade bin, but less than the following decade bin...
                decade_dict[decade] += 1 #add a count to that decade
                break

    x_values = decades #sets x values for bar chart (number of albums released in a particular decade)
    y_values = [decade_dict[d] for d in decades] #counts of x values
    return x_values, y_values, artist_names #returns values to be used in bar chart

#print getBarChartData()

def plotBarChart():
    """ creates a bar chart of the number of albums an artist(s) has released in each decade"""
    x_vals, y_vals, artist_names = getBarChartData() #calls input data from previous function
    
    fig , ax = plt.subplots(1,1) #uses the matplotlib subplot function to create figure/bar chart
    ax.bar(x_vals, y_vals, width=10) #creates the bar graph with bar width 10
    ax.set_xlabel('decades') #labels the x-axis
    ax.set_ylabel('number of albums') #labels the y axis
    ax.set_title('Totals for ' + ', '.join(artist_names)) #title's the bar graph
    plt.show() #show the bar chart

#plotBarChart()