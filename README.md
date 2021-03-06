# FullThrottleAssignment



## Backend setup

*Note: Make sure you have any version of python 3 installed before proceding to  furthur steps. To download visit https://www.python.org/downloads/*



1. Clone the code from the **git** repository into the local machine using the *git clone* command. Provide the access keys when prompted.

   ` $ git clone URL_TO_REPO FOLDER_NAME`

   For instance
   ` $ git clone https://github.com/Moinalee/FullThrottleAssignment root`

------

2. Navigate into the folder the code has copied into. To keep dependencies required by this project separately, create a virtual environment in the same folder.

   `$ cd root`

   `$ virtualenv -p python3 .`

   

   (if you do not have *virtualenv* installed, do   `$ pip install virtualenv`)

------

3. Enter the virtual environment by executing:

   ​     `$ source bin/activate`

   on Windows OS:  

   `$ .\Scripts\activate`

   if you do a   `$ pip freeze`   now, you will see that you have no packages installed.

------

4. To install all the packages required for the project (*mentioned in requirement.txt file*), do:

   `$ pip install -r requirements.txt`

   Proceed when all the packages are successfully installed.

------

5. To use a local database for development purpose, replace the existing *database* to any local database.
   Here is an instance of using *sqlite* for the same.

   `open /root/asmp/settings.py`

   update the default database to following:

```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
  }
```
   Here is an instance for using *mysql* for the same.

```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'PASSWORD_HERE',
    }
}
```
   
  *Note: if you are using Linux mysql is preffered or else errors will occur related to timezone and if still you want use sqlite in Linux change USE_TZ = True in src/user_project/settings.py but it will not give appropriate timezone data*
------

6. Make migrations to the database.

   `$ python3 manage.py migrate`

    (*make sure you are in the root folder where manage.py is present*)

   do to populate data

   `$ python manage.py populate_data`

   
------

7. Create a super user.

   `$ python3 manage.py createsuperuser`

   Use the credentials for logging into Django admin interface after next step.

------

8. Start the Django server

   `$ python3 manage.py runserver`

   The local server should be up and running. Happy developing.


------

9. Request URL
   
   `http://localhost:8000`

   Home page is opened,click on hyper link to see admin page use the credentials for logging in and now we can see the user and Activityperiod models populated with dummy data.

------

10. API to serve data

    Create the user profile and enter the Activityperiod data.

    To check API servinig data in json call the API.It can be done easily by using curl in terminal.

    `$ curl --location --request GET 'http://127.0.0.1:8000/api/accounts/activity-period'`

    For proper json format

    `$ curl --location --request GET 'http://127.0.0.1:8000/api/accounts/activity-period'|json_reformat`

    If logging is needed use

    `$ curl --location --request GET 'http://127.0.0.1:8000/api/accounts/activity-period'|json_reformat >> api_log.json`

