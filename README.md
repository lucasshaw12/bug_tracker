## Getting Started with development and running locally

Install Python3 onto your macOS machine using `brew install python`.

Ensure `pipenv` is installed on your machine with `pip3 install pipenv`.


1. Clone the repo
   ```sh
   git clone https://github.com/lucasshaw12/bug_tracker
   ```
2. Navigate into the project directory
   ```sh
   cd bug_tracker
   ```

Install PipFile dependencies `pipenv install`.

Then ensure that the pipenv environment is activated using `pipenv shell` from the applications route directory `(bug_tracker/)`.

Run the application in your local server using `python3 manage.py runserver`.

### Setting up and accessing the database:

To access the Administrator database, visit `127.0.0.1:8000/admin/`. You can then create your own superuser starting with the command `python3 manage.py createsuperuser`. Use the credentials to access the database admin dashboard.

The Admin app is used for manually managing all models within the application. This is Users and Bugs. New instances of these can created, existing instances can be modified and deleted.

## Running the live site
To run the live application, visit -

### Logging in


### Prerequisites
All required dependencies should be install when the Getting Started instructions have been followed.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

### Existing users
Admin user
username: admin
password: pass

Normal user
username: newuser1
password: workworkwork

### Create your own user
Sign up to create a user before you can interact with the application. After clicking 'sign up' an authentication token will be displayed within your terminal. Visit the given url to submit the token to verify your user. You MUST do this before you can sign in.

### Custom User model
Custom user models have been implemented within the application. The purpose of which is to ensure that if any amendments are required to the user model later in the applications lifecycle, this is easier with a custom user model. It is recommended within the Django documentation here - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project.

Users in this application needs are proxies for staff members within a software development organisation and its many teams. Besides Software Developers, these include, User Researchers, Interation Designers, Content Designs, Business Analysts and Project Managers. So additional fields such as user_role and team_name are required for this. The num_bugs_assigned field is useful for workload metrics and staff utilisation.

Preventing unauthorised access to the Bug dashboard, the bug_tracker view uses LoginMixin which checks for a valid user session. If none exists, the service redirects the user to the login template.

### How to
Bugs are added using the "Add bug" link in the navigation bar. Once created the bug will appear on the dashboard, containing all relevant details. Each card has an edit link to allow the bug details to be amended when neccesary. The list of bugs is sorted by `date_raised` with the oldest being at the top of the list.

Whenever a bug is completed successfully, the `complete bug` button should be selected. This will highlight the whole card in green, change the badge to `fixed` and show the `completed_on` date and time. Similarly, if the bug is closed without fixing it, the `close bug` button should be selected and the badge will state `closed without fix`. The bug card will be greyed and will also include the `completed_on` details.

If a bug is closed from either being `completed` or `Closed without fix`, it is not longer editable.

### Testing and test coverage
Run all tests with the command `python3 manage.py test`.

-

### Linting and Style
[Black](https://github.com/psf/black) and [Djlint](https://github.com/djlint/djlint) for HTML are used for consistency across all files and to ensure formatting standards are met. Then using a pre commit Git hook to run all formatting packages ensures they won't be forgotten.
To run black in local development use the command `black .` which formats all files. The command `djlint .` performs linting on all files.

Pre-commit hook guide found [here](https://dev.to/earthcomfy/django-code-formatting-and-linting-made-easy-a-step-by-step-pre-commit-hook-tutorial-592f#black)
-


### Libraries
Bootstrap is a css framework to improve the front-end of a Web Application. It provides HTML, CSS and Javascript templates for an easier way to build applications with a focus on responsive design. This application uses the content delivery network (CDN) provided by Bootstrap. CDN's allow for the application to connect to the CDN network of multiple servers, rather than hosting all the static files within the application itself on a single server. This makes it easy to remain updated and ensures reliability if there was an error with the service of the otherwise static files. The use of mulitple servers increase the speed of the request, speeding up the web page response to the client.

Instead of the default forms used within Django. [Crispy forms](https://github.com/django-crispy-forms/django-crispy-forms?tab=readme-ov-file) is a more conventient way to produce and style forms, along with its Bootstrap support. Default Django forms are less functionally equipped and offer less styling. Crispy forms help maintain DRY principles. Simply adding `{% load crispy_forms_tags %}` to the start of the template loads in the template tag library. Then swap out `.as_p` from the form context variable to `|crispy`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
