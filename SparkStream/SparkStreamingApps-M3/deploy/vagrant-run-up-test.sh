echo "WARNING REMOVING ALL CONTAINERS in 5 SECONDS !"

sleep 5

# Remove all containers. 

docker rm -f `docker ps --no-trunc -aq` 

echo "NOW RESTARTING DOCKER !" 

service docker restart 

echo "NOW CREATING VAGRANT DOCKER CLUSTER "

vagrant destroy --force && vagrant up --no-parallel

## Run calculate pi. 

echo "RUNNING smoke tests..." 

docker exec -i -t scale1 \
/opt/spark-1.2.0-bin-hadoop2.4/bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://scale1.docker:7077 /scale-shared/spark-examples_2.10-1.1.1.jar 10000

echo "DONE TESTING .  RESULTS ^ " 
