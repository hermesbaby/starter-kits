###############################################################################
#### Linux-Umgebung für docs-as-code toolchain ################################
###############################################################################

### Einfaches Dockerfile für die Entwicklung ##################################

FROM artifactory.vitronic.de:443/docker/ci/cibsbuildagentubuntu2204:3


### SSH Server im Docker-Container für Visual Studio Code - RemoteSSH #########

# SSH Server installieren, starten
USER root
RUN apt-get install -y  \
  openssh-server

RUN service ssh start

# Expose docker port 22 fo ssh
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]


### Set default shell to bash #################################################

SHELL ["/bin/bash", "-c"]


### Install general development environment ###################################

RUN apt-get update       \
  && apt-get install -y  \
  curl                   \
  unzip                  \
  git                    \
  byobu


### Install dependencies of docs-as-code environment ##########################

RUN apt-get update       \
  && apt-get install -y  \
  openjdk-8-jdk


### EOF #######################################################################
