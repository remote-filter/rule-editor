FROM centos
RUN yum -y install http://mirror.redsox.cc/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y install yum -y install python python-pip python-devel gcc
RUN yum -y install openssh-server passwd

RUN mkdir /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 
RUN sed -i "s/#PermitRootLogin yes/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s|HostKey /etc/ssh/ssh_host_ecdsa_key|#HostKey /etc/ssh/ssh_host_ecdsa_key|g" /etc/ssh/sshd_config
RUN sed -i "s|HostKey /etc/ssh/ssh_host_ed25519_key|#HostKey /etc/ssh/ssh_host_ed25519_key|g" /etc/ssh/sshd_config
RUN sed -i "s|#PermitEmptyPasswords no|PermitEmptyPasswords yes|g" /etc/ssh/sshd_config
RUN echo -e "newpass\nnewpass" | (passwd --stdin root)

ADD . /root/code
WORKDIR /root/code
RUN chmod a+x /root/code/start.sh
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 22
