Simple application that can store and manage appointments
Appointments should be persisted in a datastore

The application should have REST endpoints that do the following
- Delete appointments-
- Create new appointments-
- Update the status of an existing appointment-
- Retrieve a specific appointment from the database-
- Retrieve all appointments that are scheduled between a date range and sorted by price-
  (list items with "-" suffix represent implemented, place holder for developer)

Additionally an appointment scheduler function should create new appointments at a random interval.

**To install and/or test - Use Docker Linux containers
1. Either clone or download files from github repo (if application was sent through email, unzip the files to your local machine).
2. In command prompt cd into project folder (if downloaded/cloned, cd into "NielsenProject").
3. Type in the following command:
    - docker-compose run web python Scheduler/manage.py makemigrations
      -*status*
    - docker-compose run web python Schedule/manage.py migrate
      -*status*
    - docker-compose up
      -*status*
  *status* - In between these commands docker will return messages in regards to status of the command.
  **
  If there are errors setting up the docker image, please contact me and I will assist in resolving your issue.

**How to use application
1. After running through the installation instructions listed above, you will now be able to access the application via local host.
2. In a web browser, navigate to "localhost:8000/home/", this is where the appointment generator lives.
3. To access the HTTP methods GET and POST, visit "localhost:8000/api/schedule/" this will present the information being requested.
  3.1 - To retrieve all appointments that are scheduled between a date range and sorted by price use the 'Filter' button located on the top right of the screen.
4. To access the HTTP methods DELETE and UPDATE, visit "localhost:8000/api/schedule/'#'/" - '#' being an ID inside of a record.
**
