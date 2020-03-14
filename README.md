<img src="https://i.imgur.com/EZPrEEX.png" height="300">

## Flight Passport OAuth Server

While there are many authentication and identity providers inlcuding products from big cloud companies, all of them have some limitations. In the context of U-Space / UTM, issuing Javascript Web Token (JWTs) as a way to authenticate and issue credentials are parts of standards (e.g. DSS). Commercial service providers may or may not suffice for all cases, therefore this project is developed to enable maximum flexiblity and still issue secure JWT tokens. This project can be deployed on any cloud service provider (national or international) and can be customized in any way to suit local needs. 

## Technical Details   
Flight Passport is a OAuth Provider that runs on Django and the fantastic [Authlib](https://authlib.org/) library and [Django OAuth Toolkit](https://github.com/jazzband/django-oauth-toolkit). 


## Self-install
This is a Django project that uses Django and other opensource libraries. 

### 1. Install Dependencies

Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. For Local testing turn off Securing API endpoints

Go to `settings.py` and set `SECURE_API_ENDPOINTS` as `False` to disable secure endpoints for local testing. This means that you dont need the JWT tokens for Identity and Authenication, for more information about Identity and Roles are managed, please review [Identitiy and Authentication paper](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md) 

### 2. Create Initial Database

Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite.

#### Image credit

[source](https://www.vecteezy.com/free-vector/open)
