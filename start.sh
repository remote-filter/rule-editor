#!/bin/bash

#SSH_USERPASS=newpass
#echo -e "$SSH_USERPASS\n$SSH_USERPASS" | (passwd --stdin root)
#echo ssh root password: $SSH_USERPASS

#for dev time, we are just gonna start the sshd server
/usr/sbin/sshd -D
#python app.py

