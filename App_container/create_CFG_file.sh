#!/bin/bash
sudo echo -e "[client]\nuser = $MYSQL_USER\npassword = $MYSQL_PASSWORD\nhost = $MYSQL_HOST\nport = $MYSQL_PORT\ndatabase = $MYSQL_DATABASE" > connection.cfg
