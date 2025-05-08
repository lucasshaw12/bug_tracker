## Getting Started

Install Python3 onto your machine using `brew install python`.

Ensure `pipenv` is installed on your machine with `pip3 install pipenv`.

To run the application from your local machine. From the `bug_tracker` root directory, enter the command `pipenv install -r requirements.txt`. This will install the required dependencies that are needed to run the application.

Run the application in your local server using `python3 manage.py runserver`.

### Setting up and accessing the database:

To access the Administrator database, visit `127.0.0.1:8000/admin/`. You can then create your own superuser starting with the command `python3 manage.py createsuperuser`. Use the credentials to access the database admin dashboard.

The Admin app is used for manually managing all models within the application. This is Users and Bugs. New instances of these can created, existing instances can be modified and deleted.

### Logging in


### Prerequisites
All required dependencies should be install when the Getting Started instructions have been followed.


### Installation

1. Clone the repo
   ```sh
   git clone
   ```
2. Navigate into the project directory
   ```sh
   cd bug_tracker
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

### Signing up
Sign up to create a user before you can interact with the application. After clicking 'sign up' an authentication token will be displayed within your terminal. Visit the given url to submit the token to verify your user. You MUST do this before you can sign in.

### Custom User model
Custom user models have been implemented within the application. The purpose of which is to ensure that if any amendments are required to the user model later in the applications lifecycle, this is easier with a custom user model. It is recommended within the Django documentation here - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project.

Users in this application needs are proxies for staff members within a software development organisation and its many teams. Besides Software Developers, these include, User Researchers, Interation Designers, Content Designs, Business Analysts and Project Managers. So additional fields such as user_role and team_name are required for this. The num_bugs_assigned field is useful for workload metrics and staff utilisation.


### Testing and test coverage
Run all tests with the command `python3 manage.py test`.

-

### Linting and Style
[Black](https://github.com/psf/black) and [Djlint](https://github.com/djlint/djlint) for HTML are used for consistency across all files and to ensure formatting standards are met. Then using a pre commit Git hook to run all formatting packages ensures they won't be forgotten.
To run black in local development use the command `black .` which formats all files. The command `djlint .` performs linting on all files.

Pre-commit hook guide found [here](https://dev.to/earthcomfy/django-code-formatting-and-linting-made-easy-a-step-by-step-pre-commit-hook-tutorial-592f#black)
-
<p align="right">(<a href="#readme-top">back to top</a>)</p>
