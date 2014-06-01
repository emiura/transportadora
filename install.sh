#!/bin/bash

who=$(whoami)
if [ $who != "root" ]; then
   echo "Must be root!"
   exit 1
fi

if [ -f "/etc/debian_version" ]; then
   mysql=$(dpkg -l mysql-server)
   if [ -z "$mysql" ]; then
      echo "Missing mysql"
      exit 1
   fi
   easygui=$(dpkg -l python-easygui)
   if [ -z "$easygui" ]; then
      echo "Missing EasyGUI"
      exit 1
   fi
   mysqldb=$(dpkg -l python-mysqldb)
   if [ -z "$mysqldb" ]; then
      echo "Missing python mysql"
      exit 1
   fi

   username=$(grep user transportadora.conf | cut -d "=" -f 2 | tr -d ' ')
   password=$(grep password transportadora.conf | cut -d "=" -f 2 | tr -d ' ')
   database=$(grep db_name transportadora.conf | cut -d "=" -f 2 | tr -d ' ')

   echo "create database $database" | mysql -u$username -p$password
   mysql -u$username -p$password $database < sql.sql

   install -m 644 transportadora.conf /etc/
   install -m 644 transportadora.desktop /usr/share/applications/
   install -m 755 transportadora.py /usr/bin/
else
   echo "Not a debian system!"
   exit 1
fi
