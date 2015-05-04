import psycopg2

#DB: django
#User: django
#Pass: As4g98HO8J


def getSymptomOccurance(drug):
	try:
		conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
	except:
		print "I am unable to connect to the database. Obviously, this shouldn't print, but why not?"

	cur = conn.cursor()
	cur.execute("""
		SELECT symptom, count(symptom) from website_drugtweet WHERE drug = '{}' GROUP BY symptom
	""".format(drug))


	rows = cur.fetchall()
	dict = {}

	#print "here's the database!!"
	#print rows
	for row in rows:
		dict[row[0]] = {str(row[0]) : int(row[1])}

	#print dict
	return dict
foo = getSymptomOccurance('advair')


#Pie Chart
def getPieChart(drug):
	foo = getSymptomOccurance(drug)
	arg1 = "["
	for k, v in foo.iteritems():
		arg1 = arg1 + "['" + k + "'," + str(v[k]) + "],"
	arg1 = arg1 + "]"	
	return arg1
print getPieChart('advair')

#Bar Chart
#['Giant', 1, 'silver']
def getBarChart(drug):
	foo = getSymptomOccurance(drug)
	arg2 = "["
	for k, v in foo.iteritems():
		arg2 = arg2 + "['" + k + "', "  + str(v[k]) + " , 'silver'],"
	return arg2
print getBarChart('advair')

#Word Cloud
#2 word\n
def getWordCloud(drug):
	foo = getSymptomOccurance(drug)
	arg3 = ""
	for k, v in foo.iteritems():
		arg3 = arg3 + str(v[k]) + ' ' + k + '\n'
	#print arg3
	return arg3
print getWordCloud('advair')
