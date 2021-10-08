FROM gcr.io/spark-operator/spark-py:v3.0.0
LABEL MAINTAINER Carlos Barbosa 
LABEL EMAIL carlos.barbosa@a3data.com.br

# using root
USER root:root

# create directory for applications
RUN mkdir -p /app 

RUN rm $SPARK_HOME/jars/guava-14.0.1.jar
ADD https://repo1.maven.org/maven2/com/google/guava/guava/23.0/guava-23.0.jar $SPARK_HOME/jars
ADD https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-hadoop2.jar $SPARK_HOME/jars
RUN mkdir -p /opt/hadoop/conf
COPY conf/core-site.xml /opt/hadoop/conf
COPY conf/spark-env.sh $SPARK_HOME/conf

#set main work directory
WORKDIR /app

#user
USER root