Simple application that can store and manage appointments
Appointments should be persisted in a datastore

The application should have REST endpoints that do the following
- Delete appointments-
- Create new appointments-
- Update the status of an existing appointment-
- Retrieve a specific appointment from the database-
- Retrieve all appointments that are scheduled between a data range and sorted by price-
  (list items with "-" suffix represent implemented, place holder for developer)

Additionally an appointment scheduler function should create new appointments at a random interval.

To install and/or test - Use Docker Linux containers
1. Either clone or download files from github repo (if application was sent through email, copy those times to your local machine).
2. In command prompt cd into project folder (if downloaded, cd into "NielsenProject").
3. Type in the following command:
    - docker-compose run web python Scheduler/manage.py makemigrations
    - docker-compose run web python Schedule/manage.py migrate
    - docker-compose up
  In between these commands docker will return messages in regards to status of the command.
