import logging

from google.cloud import firestore

from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


class FirestoreCustomerRepository:
    def __init__(self, customer_collection):
        db = firestore.Client()
        self.customer_repo = db.collection(customer_collection)

    def store(self, customer):
        doc_ref = self.customer_repo.document()
        doc_id = doc_ref.id
        firestore_response = doc_ref.set(
            {"customer_id": doc_id, u"firstName": customer.first_name,
             u"surname": customer.surname})
        logging.info(firestore_response)
        customer.customer_id = doc_id

    def fetch_by_id(self, customer_id):
        doc_ref = self.customer_repo.document(customer_id)
        doc = doc_ref.get()
        logging.info("document: {}".format(doc))
        logging.info(u'Document data: {}'.format(doc.to_dict()))

        customer_json = doc.to_dict()
        if customer_json is not None:
            return Customer(customer_id=customer_json["customer_id"],
                            first_name=customer_json["firstName"],
                            surname=customer_json["surname"])
        else:
            raise CustomerNotFound()
