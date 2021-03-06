# A MUSIC-WEBSITE for Flask Apps

This is our music collaborating website creating flask applications that require user authentication.  It draws heavily from 1.LEWIS NJAGI
                                                    2.GIDION OLE
                                                    3.JOEL MWANGAI
                                                    4.DAVID HASHISOMA

incredible [Flask Mega MUSIC WEBSITE]() and uses [Bootstrap.js](https://getbootstrap.com/docs/3.3/getting-started/#template) for a nice responsive design.

This is available for you to use, but comes with no guarantee or warranty.  Use at your own risk.

# Getting up and Running

    virtualenv env
    source virtual/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=apprunner.py
    flask db init
    flask db migrate -m "Initial database build"
    flask db upgrade
    flask run

Copy the template configuration file [app.conf](./app.conf) to create a custom configuration file (e.g., `cp app.conf app.local.conf`). 

Edit your custom configuration file (e.g., `app.local.conf`) and define your environment values. Thereafter, the file might look like this:
```ini
[ServiceConfiguration]
springbootadminserverurl = http://localhost:5000/
springbootadminserveruser = admin
springbootadminserverpassword = admin
servicename = myname
serviceport = 5000
servicehost = http://127.0.0.1
servicedescription = my component is doing some magic
```


# Deploying to Azure

* Follow these deploy to HEroku[  Python](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python) instructions through your first push to Heroku.
  * Create an App Service Plan, Service, and Resource Group to hold the services.
  * Create a deployment user.
  * Add api as a remote repository.
* Configure the [App Service for Python](https://docs.microsoft.com/en-us/visualstudio/python/managing-python-on-azure-app-service)
  * Add the Python 3.6 extension.
  * Ensure that the web.config file reflects the location of your installed extension.
  * On the kudu console, cd into the folder containing the python installed by the extension.
  * python -m pip install -r requirements.txt while in that folder.
* OPTIONAL: Create an Azure SQL DB Server and Database
  * [Quick Start](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-get-started-portal)
  * Create an [application user](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-2017) and grant them [permissions](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions?view=sql-server-2017#permission-hierarchy).

    --On master
    CREATE LOGIN some_application_user 
	WITH PASSWORD = 'SomeSecurePassword'
    
    --On your application db
    CREATE USER some_application_user 
	FOR LOGIN some_application_user 
	WITH DEFAULT_SCHEMA = dbo
    GO

    -- Add user to the database owner role
    EXEC sp_addrolemember N'db_datareader', N'some_application_user'
    GO
    EXEC sp_addrolemember N'db_datawriter', N'some_application_user'
    GO

* MISCELLANEOUS Checklist
  * Add the environment variables to web.config.
  * Create any additional folders on the kudu console.

# Working with VS Code and Flask Apps

* Setting an environment variable.
  * Powershell: $env:MyVariable=SomeValue
  * CMD: set MyVariable=SomeValue
  * Linux: export MyVariable=SomeValue
* Viewing an environment variable
  * Powershell:  Get-ChildItem Env:MyVariable
  * CMD: echo %MyVariable%
  * Linux: echo $MyVariable
