import psycopg2
import uuid

#class Tweetv2(models.Model):
#        id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1)
#DB: django
#User: django
#Pass: As4g98HO8J

try:
	conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
	cur = conn.cursor()
except:
	print "failed connecting to database"

#Inserting

try:

	#Generate unique ID
	bidoof = str(uuid.uuid1())
	
	cur.execute("""
		INSERT INTO website_tweetv2
		(id, tweet, symptom)
		VALUES
		('{}', 'Kenneth better get a cup of coffee for this', 'Sleep Deprived')
		""".format(bidoof))
	conn.commit()
except:
	print "If the following 6 lines of code above does not work, this should print"


#Now let's see our insert in action baby
try:
	cur.execute("""
		SELECT * FROM website_tweetv2 
	""")
except:
	print "If the following 3 lines of code above does not work, this should print"

rows = cur.fetchall()
dict = {}

print "\n And here is the database \n"


#Prints the database
for row in rows:
	print row


