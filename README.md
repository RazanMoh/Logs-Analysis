# Logs Analysis

## Introduction

Building a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Running

#### ***Project Setup:***
> 1.	Install Vagrant: https://www.vagrantup.com/downloads.html 
2.	Install Virtual Machine: https://www.virtualbox.org/wiki/Downloads
3.	Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm 
4.	Download the newsdata.sql  from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

#### ***Starting the Virtual Machine:***
> Once you get the above software installed, follow the following instructions: 
```bash
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
```

#### ***Setting up the database***:
> Run the following command to execute it in news database.
```bash
psql -d news -f newsdata.sql 
```
> Once you have the data loaded into your database, connect to your database using
```bash
psql -d news 
```

> The “newsdata.sql” has three different tables: 
1. Authors: table includes information about the authors of articles. 
2. Articles: table includes the articles themselves. 
3. Log: table includes one entry for each time a user has accessed the site. 


#### ***Running the project:***
```bash
python3 newsdata.py
```
