<img src="https://i.imgur.com/EZPrEEX.png" height="300">


**April 2020: This software is under heavy development and really ready for production use yet**

## Flight Passport OAuth Server

A OAuth proivder focused on UTM / U-Space that can be self hosted and used to issue JWT tokens for software UTM software like DSS, Registries, Remote ID Display providers (e.g. [Flight Spotlight](https://www.github.com/openskies-sh/flight-spotlight)) etc. 


## Why? 

The upcoming standards being developed at ASTM, EuroCAE etc. on drones use JWT / OAuth 2.0 based tokens to exchange credentials and permissions. There are many open and closed sourced solutions avaiable for this. However, based on my work / research there are a few limitations of the current offerings:

- National Entities may or may not be interested in using private commercial companies for authentication and identity. since this is a national function, they would prefer to host the platform locally.
- OAuth / OpenID / Open ID Connect stack are a “general purpose” authenication and identity standard and the solutions available price it very differently. Some charge by number of users, some charge by number of tokens / clients etc. All of this is not really suitable for UTM / U-Space operations.
- The Remote ID standard and demos use the `sub` and `aud` claim in a specific way that a number of commercial solutions do not support out-of-the-box.
- There are very specific OAuth related things that some services do not support. E.g. Azure does not support “scope” in Client Credentials grant, but is required per the Remote ID standard.
- On the [open source side](https://oauth.net/code/), a number of them are not totally ready or have very complex installation procedures or user management etc. that are not really necessary for the authorization use-case.

### Background 

While there are many authentication and identity providers that support OAuth 2.0 and OpenID / OpenID Connect Credentials, all of them have some limitations in the context of U-Space / UTM. As of February 2020, OAuth 2.0 and Javascript Web Token (JWTs) as a way to authenticate and issue credentials are parts of upcoming UTM / U-Space standards (e.g. DSS). Commercial service providers may or may not suffice for all cases, therefore this project is developed to enable maximum flexiblity and still issue secure JWT tokens. This project can be deployed on any cloud service provider (national or international) and can be customized in any way to suit local needs. 

## Technical Details   
Flight Passport is a OAuth Provider that runs on Django and the fantastic [Authlib](https://authlib.org/) library and [Django OAuth Toolkit](https://github.com/jazzband/django-oauth-toolkit). 


## Self-install
This is a Django project that uses Django and other opensource libraries. 

### 1. Install Dependencies

Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. Create Initial Database

Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite.

### 3. Create a Django administrator

Use `python manage.py createsuperuser` to create a administrator.

### 3. Login to Administration interface and create a client

Go to `http://localhost:8000/admin` and login to the Django Admin interface and create a new client. 

#### Image credit

[source](https://www.vecteezy.com/free-vector/open)
