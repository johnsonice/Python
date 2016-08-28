#install Anaconda in cloud 9
# look at this guy 
https://github.com/mGalarnyk/Installations_Mac_Ubuntu_Windows/blob/master/Anaconda/Anaconda_Install_Instructions_Ubuntu.ipynb
https://zenagiwa.wordpress.com/2015/10/24/chi-py-mentorship-program-day-2-setting-up-a-python-dev-environment-on-the-cloud-9/
#all anaconda repos 
http://repo.continuum.io/archive/

#steps 
# 1 download Anaconda latest Linux 64 bit version 
	mkdir Downloads
	cd Downloads
	wget http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
# install Anaconda
	bash Anaconda2-4.0.0-Linux-x86_64.sh

	# you should say now when it is trying to prepend the path 
	# otherwise you need to do it your self 

	export PATH=~/anaconda2/bin:$PATH

	#Prepending PATH=/home/ubuntu/anaconda2/bin to PATH in /home/ubuntu/.bashrc
	#A backup will be made to: /home/ubuntu/.bashrc-anaconda2.bak
	
# now close terminal, open a new one 
	#update jupyter 
	conda update --all --yes

#check conda environment 
	conda env export -n root
	conda list 
# start jupyter note book 
jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser  #now jupyter server is running 

#go to following address and run jupyter notebook 
http://python-johnsonice.c9users.io:8080/tree

#to make the default python runner to get anaconda packages, 
#add /home/ubuntu/anaconda2/lib/python2.7/site-packages to environment variable 



##################################################################################
##################################################################################
####   Start mysql database from c9 ##############################################
mysql-ctl start       #start instance
mysql-ctl stop		  #end instance 
mysql-ctl cli         #open mysql console 



