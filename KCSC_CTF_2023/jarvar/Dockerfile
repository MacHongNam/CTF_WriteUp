FROM openjdk:8u222-slim

RUN apt-get update -y \
    && apt-get install curl -y \
    && useradd ctf \
    && mkdir /opt/app

COPY java.security /usr/local/openjdk-8/jre/lib/security/java.security
COPY kcscctf.jar /opt/app
COPY flag.txt /flag.txt

WORKDIR /opt/app
EXPOSE 8080

USER ctf
CMD ["java","-jar", "/opt/app/kcscctf.jar"]
