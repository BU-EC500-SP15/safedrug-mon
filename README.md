# safedrug-mon
Real Time Drug Safety Monitoring in the Cloud

*In depth SBT And SparkStreaming + Scala Primer* 

https://www.youtube.com/watch?v=gfWIUOapUp4

- The above URL should be *actively* watched, it might take someone a day or more to really grasp all the concepts (intellij, scala, sbt, etc), and assumes that the watcher will google around for individual concepts and play with them.  
- It also assumes basic working knowledge of the linux terminal, using commands like ls, grep and so on.

- And of course, some understanding of java.


In any case, that video can provide a good giudepost  .  Once you understand the concepts in it and can reproduce it, you are really ready to start hacking on the spark streaming twitter application.

5/5/2015-------------------

Updated Youtube Video Regarding Project:
https://www.youtube.com/watch?v=BhF4xEbvMJM

Watch video first to understand how everything should work once it is setup.

Program is NOT able to run unless you get the UMLS dictionary
/SparkStream/SparkStreamingApps-M3/org/apache/ctakes/orgs was removed because of Github size limitations.

Once you acquire the dictionary and add it to ~/SparkStreaming/SparkStreamingApps-M3, modify paths for output files and Twitter credentials, you should be able to run everything either in an IDE (like IntelliJ IDE) or from the terminal if you have SBT installed on your machine using following commands run in ~/SparkStreaming/SparkStreamingApps-M3 directory:

TERMINAL COMMANDS TO RUN PROGRAM
To run sparkstreaming to collect tweets: sbt "run-main sparkapps.ctakes.Driver"
To run CTakesTermAnalyzer: sbt "run-main sparkapps.ctakes.CtakesTermAnalyzer"

 
