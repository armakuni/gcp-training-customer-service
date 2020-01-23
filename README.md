# GCP Training Customer Service

This is a RESTful API which can store and retrieve customer information using a Firestore database.

### Requirements

- A Firestore instance up and running in your Google Cloud account
- google service account to access the Firestore

#### Refer below link for more detail about setting up the environment to use google Firestore

- https://cloud.google.com/firestore/docs/quickstart-servers

### Environment variables

The service uses the below variables in its configuration. They all have default values as shown below if they are not otherwise specified:

```
CUSTOMER_NAMESPACE=customers(default)
PORT=5000(default)
```

### To run linter

```bash
make lint
```

### To run tests

```bash
make test
```

### To run the service locally
Before starting the application locally you must create Google Service Account and store credentials json file locally to authenticate.

Once you have stored the credentials locally, export it to the environment variable as below:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_CREDENTIALS_FILE]/[SERVICE_ACCOUNT_CREDENTIALS_FILENAME].json 
```

```bash
make run
```

### Deployment

This repository contains a cloudbuild.yaml file to deploy this service on to Cloud Run:

Execute below command to trigger the Cloud Build deployment through CLI.
```bash
gcloud builds submit --substitutions=_CUSTOMER_NAMESPACE="[CUSTOMER_NAMESPACE]"
```

where [CUSTOMER_NAMESPACE] is the name of the Firestore collection that contains the customer information.

### API documentation

You can access the API documentation by launching the application and visiting [swagger ui](http://localhost:5000/docs/).
For accessing in Cloud Run append ```/docs/``` after the endpoint exposed by Cloud Run service.
