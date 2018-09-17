# Blog

<p align = "center">
    <b>By Rreuben</b>  
</p>

### Description
This is a web based application where I express my ideas and opinions. Other users can read and comment on what I share with them.

***
#### The app specifications 
This website will:

    Allow a user to view the posts a writer a submitted
    Allow a user to to comment on writers' posts
    Display my a writer's most recent posts
    Provide a subsciption service for users who want to be alerted when a writer posts
    Provide an authentication service for users that wish to have accounts
    Allow a writer to create a blog
    Allow a writer to delete comments they find insulting or degrading
    Allow a writer to update or delete blogs they have submitted

#### Technologies
* Python
* Flask (in Python)
* Bootstrap (for styling)
* Postgresql (the database)

View the source code at [GitHub](https://github.com/Rreuben/blog)

#### Installation/Setup
You need to have Python 3.6 installed to run this program.

`$ git clone <this-repository>`<br />

Create a virtual enironment and activate it.

`$ virtualenv -p python`<br />
`$ source virtual/bin/acivate` and `(virtual)$ deactivate` is to deactivate the environment.

In the virtual environment:

`(virtual)$ pip install -r requirements.txt`<br />

Running the app.

    Prepare the environment variables.
    
        (virtual)$exportDATABASE_URL='postgresqlpsycopg2://username:password@localhost/pitch'`<br/>
        `(virtual)$ export SECRET_KEY='Your secret key'

    Run Database Migrations.

        (virtual)$ python manage.py db init
        (virtual)$ python manage.py db migrate -m "Initial migration"
        (virtual)$ python manage.py db upgrade

    Run the app.

        (virtual)$ touch start.sh

        Put #!/usr/bin/env bash as the first line in start.sh
        Put python3.6 manage.py server as the second line in start.sh

        (virtual)$ chmod a+x start.sh
        (virtual)$ ./start.sh

#### Alternatively
* Open browser (Google Chrome Recommended)
* Visit the live [website](https://name of deployed app.herokuapp.com)

#### Further Development
Some features that are to come soon:

    Commenting and deleting posts

#### Known Bugs
Heroku is not picking up styling links. The navbar and footer will look weird on load up.

***

<p align = "center">
    <a href = "https://github.com/Rreuben/blog/blob/master/LICENSE">LICENSE</a>
</p>
