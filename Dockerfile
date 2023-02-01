FROM jenkins/jenkins:2.375.2
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
#start docker 
RUN apt install -y docker.io
#install systemctl
RUN apt-get install -y systemd


RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3
RUN pip3 install docker-compose
#user docker 
RUN usermod -aG docker jenkins
RUN usermod -aG docker root
#add to user jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
#in which port is jenkins running
EXPOSE 8080