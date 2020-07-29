<img src="https://i.imgur.com/EZPrEEX.png" height="300">

## Flight Passport OAuth Server

A OAuth proivder focused on UTM / U-Space that can be self hosted and used to issue JWT tokens for software UTM software like DSS, Registries, Remote ID Display providers (e.g. [Flight Spotlight](https://www.github.com/openskies-sh/flight-spotlight)) etc.

## Why?

The upcoming standards being developed at ASTM, EuroCAE etc. on drones use JWT / OAuth 2.0 based tokens to exchange credentials and permissions. There are many open and closed sourced solutions avaiable for issuing tokens. However, based on my work / research there are a few limitations to the current offerings:

- National Entities may or may not be interested in using private commercial companies for authentication and identity. Since this can be / is a national function, they would prefer to host the platform locally.
- OAuth / OpenID / Open ID Connect stack are a “general purpose” authentication and identity standard and the commerical solutions available price it very differently. Some charge by number of users, some charge by number of tokens / clients etc. All of this is not really suitable for UTM / U-Space operations.
- The Remote ID standard and demos use the `sub` and `aud` claim in a specific way that a number of commercial solutions do not support out-of-the-box. e.g. Azure does not support “scope” in Client Credentials grant, this is required per the Remote ID standard.
- On the [open source side](https://oauth.net/code/), a number of them are not totally ready or have very complex installation procedures or have too many features that make it bulky: e.g. user management. These make them unsuitable / overkill for the specific use-cases.

### Background

While there are many authentication and identity providers that support OAuth 2.0 and OpenID / OpenID Connect Credentials, all of them have some limitations in the context of U-Space / UTM. As of February 2020, OAuth 2.0 and Javascript Web Token (JWTs) as a way to authenticate and issue credentials are parts of upcoming UTM / U-Space standards (e.g. DSS). Commercial service providers may or may not suffice for all cases, therefore this project is developed to enable maximum flexiblity and still issue secure JWT tokens. This project can be deployed on any cloud service provider (national or international) and can be customized in any way to suit local UTM / U-Space needs.

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

### 4. Start Server

Run  `python manage.py runserver`

### 5. Login to Administration interface and create a client

Go to `http://localhost:8000/admin` and login to the Django Admin interface and create a new client.

### 6. Create a .env file

Rename the `.env.example` to `.env` and fill in approrpriately. You might have to create new key. Follow instructions [here](https://www.howtoforge.com/linux-basics-how-to-install-ssh-keys-on-the-shell) for example.

### 7. Make a Client Credentials request

Use a API client such as Postman or Insomnia to run a `client_credentials` request.

### 8. Authorization Code request

Once a Application has been created, you can run the  [Sample Client](https://github.com/openskies-sh/flight_passport_sample_client) to run the Authorization Code grant.

#### Image credit

[Passport Vectors by Vecteezy](https://www.vecteezy.com/free-vector/passport)
