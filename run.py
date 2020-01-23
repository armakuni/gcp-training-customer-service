from customer_service.app import create
from customer_service.infrastructure.firestore_customer_repository import \
    FirestoreCustomerRepository
import os

if __name__ == "__main__":
    firestore_namespace = os.getenv('CUSTOMER_NAMESPACE', 'customers')
    customer_repository = FirestoreCustomerRepository(firestore_namespace)
    app = create(customer_repository=customer_repository)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
