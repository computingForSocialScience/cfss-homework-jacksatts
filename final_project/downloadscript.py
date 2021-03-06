import requests
import pymysql

#Choose Tables
census = ["B01001", "B02001", "B16008", "B16009", "B16010", "B99163"]

#Collect Table Information
def gettableinfo(table_id):
	url = "http://api.censusreporter.org/1.0/table/" + table_id
	req=requests.get(url)
	data=req.json()
	table_info = []
	table_title = data['table_title']
	denominator = data['denominator_column_id']
	for key, value in data['columns'].iteritems():
		column_title = value["column_title"]
		col_tag = key
		parent_col = value["parent_column_id"]
		"""if parent_col = null:
			parent_col = col_tag
		else:
			parent_col = parent_col"""
		tuple_list = (table_id, table_title, denominator, column_title, col_tag, parent_col)
		#table_info.append(tuple_list)
	#return table_info
	return tuple_list

#run code for table information for select tables
table_info_list = []
for table in census:
	table_info_list.append(gettableinfo(table))

#check appending issues
'''for l in table_info_list:
	if len(l) != 6: 
		print len(l)'''

#table data
FIPS_dict = {"Mississippi": "28", "Oklahoma": "40", "Delaware": "10", "Minnesota": "27", "Illinois": "17", "Arkansas": "05", "New Mexico": "35", "Indiana": "18", "Maryland": "24", "Louisiana": "22", "Idaho": "16", "Wyoming": "56", "Tennessee": "47", "Arizona": "04", "Iowa": "19", "Michigan": "26", "Kansas": "20", "Utah": "49", "Virginia": "51", "Oregon": "41", "Connecticut": "09", "Montana": "30", "California": "06", "Massachusetts": "25", "West Virginia": "54", "South Carolina": "45", "New Hampshire": "33", "Wisconsin": "55", "Vermont": "50", "Georgia": "13", "North Dakota": "38", "Pennsylvania": "42", "Florida": "12", "Alaska": "02", "Kentucky": "21", "Hawaii": "15", "Nebraska": "31", "Missouri": "29", "Ohio": "39", "Alabama": "01", "New York": "36", "South Dakota": "46", "Colorado": "08", "New Jersey": "34", "Washington": "53", "North Carolina": "37", "District of Columbia": "11", "Texas": "48", "Nevada": "32", "Maine": "23", "Rhode Island": "44"}
states = FIPS_dict.keys()
FIPSCode = FIPS_dict.values()
#print FIPSCode

def gettabledata(table_id):
	for code in FIPSCode:
		url = "http://api.censusreporter.org/1.0/data/show/latest?table_ids=" + table_id + "&geo_ids=140|04000US" + code
		req=requests.get(url)
		data=req.json()
		table_data = []
		if not data['data']:
			print "BROKEN LINK", url
		else: 
			for num in data['data'].keys():
				col_num = data['data'][num].keys()
				for col in col_num:
					responses = data['data'][num][col]['estimate'].items()
					for (x,y) in responses:
						info = (table_id, code, num, col_num, x, y)
						#table_data.append(info)
		#return table_data
	return info

#run code to get table data from select tables
table_data_list = []
for table in census:
	table_data_list.append(gettabledata(table))
	print len(table_data_list)

#check appending issues
'''for l in table_data_list:
	if len(l) != 6: 
		print len(l)'''

"""
#create MySQL database
dbname="final"
host="localhost"
user="root"
passwd="snoopy21"
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

#populate database
cur = db.cursor()

CreateTableInfo = '''CREATE TABLE IF NOT EXISTS TableInfo (TableId VARCHAR(255), TableTitle VARCHAR(255), Denominator VARCHAR(255), ColumnTitle VARCHAR(255), ColumnId VARCHAR(255), ParentColId VARCHAR(255));'''
CreateTableData = '''CREATE TABLE IF NOT EXISTS TableData (TableId VARCHAR(255), FIPSCode INTEGER, ColumnId VARCHAR(255), ResponseCategory VARCHAR(255), Response INTEGER);'''

cur.execute(CreateTableInfo)
cur.execute(CreateTableData)

insertQuery = '''insert into TableInfo (TableId, TableTitle, Denominator, ColumnTitle, ColumnID, ParentColId)
values (%s, %s, %s, %s, %s, %s);'''

cur.executemany(insertQuery, table_info_list)

insertQuery2 = '''insert into TableData (TableId, FIPSCode, ColumnId, ResponseCategory, Response)
values (%s, %s, %s, %s, %s);'''

cur.executemany(insertQuery2, table_data_list)

db.commit()
cur.close()
"""