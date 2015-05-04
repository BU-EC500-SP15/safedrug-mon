import psycopg2

try:
	conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
except:
	print "I am unable to connect to the db!"

cur = conn.cursor()
cur.execute("""
	SELECT * FROM website_tweetv2
""")

rows = cur.fetchall()
print "show me the database"
dict = []
for row in rows:	
	dict.append( {'drug' : str(row[2]), 'tweet' : str(row[1])} )



for a in dict:
	print a['tweet']

