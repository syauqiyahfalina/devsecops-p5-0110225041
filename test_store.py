import unittest
from database import initialize_database
from store import Store
from payments import PaymentService

class StoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initialize_database()
        cls.store=Store()
        cls.payments=PaymentService()

    def test_list_products(self):
        products=self.store.list_products()
        self.assertGreaterEqual(len(products),3)
        self.assertIn("name",products[0])

    def test_search_product(self):
        self.assertTrue(any(p["name"]=="Pulpen Biru" for p in self.store.search_products("Pulpen")))

    def test_order_history(self):
        oid=self.store.create_order(1,1,"TestCustomer")
        self.assertTrue(any(o["id"]==oid for o in self.store.order_history("TestCustomer")))

    def test_demo_payment(self):
        oid=self.store.create_order(2,1,"PayCustomer")
        self.assertIn("berhasil",self.payments.process_payment(oid,"demo"))

    def test_reject_zero_quantity(self):
        with self.assertRaises(ValueError): self.store.create_order(1,0,"Tester")

if __name__=="__main__": unittest.main()
