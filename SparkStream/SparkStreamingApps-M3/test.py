import os
import time
import psutil

print "Starting Spark Streaming Application at " + time.strftime("%c")
os.system('sbt "run-main sparkapps.ctakes.Driver"')
time.sleep(60)
# Stop SparkStreaming after a period of time
os.kill
print "Stopping Spark Streaming Application at " + time.strftime("%c")
