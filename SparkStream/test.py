'''
Make sure this script is in the same directory the 
application is in, and you can run it.

You may need to modify the script for different drugs
or adjust the time interval as you see fit (default is 6 hours-21,600 sec)
'''
import os               # For running terminal commands
import time             # For Date/time
import psycopg2
import uuid
drug = 'advair'			# For every drug

while True:
	# Start TwitterSpark Streaming
	print "Starting Spark Streaming Application at " + time.strftime("%c")
	os.system("echo hello world")
	time.sleep(5)
	# Stop SparkStreaming after a period of time
	print "Stopping Spark Streaming Application at " + time.strftime("%c")
	# When SparkStreaming is stopped, store Tweets to the database
	'''
	DB: django
	User: django
	Pass: As4g98HO8J
	'''
	try:
	        conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
	        cur = conn.cursor()
	except:
	        print "failed connecting to database"

	#Inserting
	with open('TweetFile.txt', 'r') as f:
	        for line in f:
	                try:
	                        #Generate unique ID
	                        bidoof = str(uuid.uuid1())
	                        cur.execute("""
	                                INSERT INTO website_tweetv2
	                                (id, tweet, symptom)
	                                VALUES
	                                ('{}', '{}', '{}')
	                                """.format(bidoof, line, drug))
	                        conn.commit()
	                except:
	                        print line

	                #Now let's see our insert in action baby
	                try:
	                        cur.execute("""SELECT * FROM website_tweetv2""")
	                except:
	                        print "If the following 3 lines of code above does not work, this should print"

	# Run cTAKESAnalyzer on this Tweet File
	print "Starting cTAKESAnalyzer at " + time.strftime("%c")


	print "Stopping cTAKESAnalyzer at " + time.strftime("%c")
	# Remove The old Tweet file
	#os.system("rm -rf TweetFile.txt")
	print "Removed TweetFile.txt at " + time.strftime("%c")

	# Clean the output.txt file
		# Lower case everything
	with open('output.txt','r') as f2:
		for line in f2:
			print line
			line = line.lower()
			print line
		# Remove drug name

	# Send cleaned output to the database

	# Remove cleaned output file
	#os.system("rm -rf TweetFile.txt")
	print "Removed OutputFile.txt at " + time.strftime("%c")
	# End of while loop, the program will continue since the while loop does not end
	break
                                           
