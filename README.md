# Customer Service

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
make tests
```

### To run the service locally

```bash
make run
```

### Deployment

This repository contains a cloudbuild.yaml file to deploy this service on to Cloud Run:

```bash
gcloud builds submit --substitutions=_CUSTOMER_NAMESPACE="[CUSTOMER_NAMESPACE]"
```

where [CUSTOMER_NAMESPACE] is the name of the Firestore collection that contains the customer information.

### API documentation

You can access the API documentation by launching the application and visiting [swagger ui](http://localhost:5000/docs/)
