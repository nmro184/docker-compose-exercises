In this mission you have a working App, the flask app is working with a mysql server. 
Tasks to be done:
- Setup a docker-compose file with the following env variables of mysql

      MYSQL_DATABASE: your_db_name
      MYSQL_USER: your_db_user
      MYSQL_PASSWORD: your_db_password
      MYSQL_ROOT_PASSWORD: root_password

- Configure a volume and bind mount the volume to make the data persistent
-  the second bind mount is for a init.sql query that creates the table for main.py file (you can use chatgpt for that purpose)
- configure some env variables for the flask app as well, you will need to look in the code itself to understand what's missing for you

Good luck!
