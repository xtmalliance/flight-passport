<img src="https://i.imgur.com/EZPrEEX.png" height="300">

## Flight Passport OAuth Server

A OAuth proivder focused on UTM / U-Space that can be self hosted and used to issue JWT tokens for software like DSS, Regsitry etc. compatible with current U-Space standards.

## Why? 

The upcoming standards being developed at ASTM, EuroCAE etc. on drones use JWT / OAuth 2.0 based tokens to exchange credentials and permissions. There are many open and closed sourced solutions avaiable for this. However, based on my work / research there are a few limitations of the current offerings:
- National Entities may or may not be interested in using private commercial companies for authentication and identity. since this is a national function, they would prefer to host the platform locally.
- OAuth / OpenID / Open ID Connect stack are a “general purpose” authenication and identity standard and the solutions available price it very differently. Some charge by number of users, some charge by number of tokens / clients etc. All of this is not really suitable for UTM / U-Space operations. 
- There are very specific OAuth related things that some services do not support. E.g. Azure does not support “scope” in Client Credentials grant, but is required per the Remote ID standard. 
- On the [open source side](https://oauth.net/code/), a number of them are not totally ready or have very complex installation procedures. 

### Background 

While there are many authentication and identity providers that support OAuth 2.0 and OpenID / OpenID Connect Credentials, all of them have some limitations in the context of U-Space / UTM. As of February 2020, OAuth 2.0 and Javascript Web Token (JWTs) as a way to authenticate and issue credentials are parts of upcoming UTM / U-Space standards (e.g. DSS). Commercial service providers may or may not suffice for all cases, therefore this project is developed to enable maximum flexiblity and still issue secure JWT tokens. This project can be deployed on any cloud service provider (national or international) and can be customized in any way to suit local needs. 

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
