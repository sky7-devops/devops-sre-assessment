FROM jenkins/jenkins:lts

USER root

RUN apt-get update \
    && apt-get install -y \
        docker.io \
        curl \
        python3 \
        python3-pip \
        docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

USER jenkins