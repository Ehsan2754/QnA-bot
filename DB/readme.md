# MySQL on python


## Install process 

### Prerequisites 

 on linux serever should be followed as the [tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)

### Installing MySQL

```linux
# update the package manager
sudo apt update
# install MySQL from apt
sudo apt install mysql-server

```

### Configuring MySQL

For fresh installations of MySQL, you’ll want to run the DBMS’s included security script. This script changes some of the less secure default options for things like remote root logins and sample users.

``` linux
# Run the script 
sudo mysql_secure_installation
# OUTPUT

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:
 2
```
Regardless of whether you choose to set up the Validate Password Plugin, the next prompt will be to set a password for the MySQL root user. Enter and then confirm a secure password of your choice:
```linux
#OUTPUT

Please set the password for root here.


New password: 

Re-enter new password: 

```

### Test mySQL

To run MySQL service on the machine run the command : 
```linux
sudo systemctl start mysql
```
In order to check out if mySQL is running : 
```linux
systemctl status mysql.service
#OUTPUT
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset:>
     Active: active (running) since Mon 2020-06-15 15:49:34 MSK; 38min ago
   Main PID: 112958 (mysqld)
     Status: "Server is operational"
      Tasks: 40 (limit: 9300)
     Memory: 326.7M
     CGroup: /system.slice/mysql.service
             └─112958 /usr/sbin/mysqld

Jun 15 15:49:33 LIFEBOOK-E752 systemd[1]: Starting MySQL Community Server...
Jun 15 15:49:34 LIFEBOOK-E752 systemd[1]: Started MySQL Community Server.
lines 1-12/12 (END)

```
For an additional check, you can try connecting to the database using the mysqladmin tool, which is a client that lets you run administrative commands. For example, this command says to connect to MySQL as root (-u root), prompt for a password (-p), and return the version.

```linux
sudo mysqladmin -p -u root version
#OUTPUT
mysqladmin  Ver 8.0.20-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version		8.0.20-0ubuntu0.20.04.1
Protocol version	10
Connection		Localhost via UNIX socket
UNIX socket		/var/run/mysqld/mysqld.sock
Uptime:			39 min 41 sec

Threads: 2  Questions: 13  Slow queries: 0  Opens: 128  Flush tables: 3  Open tables: 49  Queries per second avg: 0.005

```

### Install MySQL Driver for python 

install MySQL Connector
```linux
pip3 install mysql-connector-python
```

