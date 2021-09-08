import unittest
import product


class TestProduct(unittest.TestCase):
    def test_create(self):
        p = product.Product('MINT', 100 , 490.1)
        self.assertEqual(p.name, "MINT")
        self.assertEqual(p.quant, 100)
        self.assertEqual(p.price, 490.1)

    def test_cost(self):
        p = product.Product('MINT', 100, 490.199)
        self.assertEqual(p.cost, 49019)

    def test_sell(self):
        p = product.Product('MINT', 100, 490.199)
        p.sell(10)
        self.assertEqual(p.quant, 90)

    def test_bad_quant(self):
        p = product.Product('MINT', 100, 490.199)
        # p.quant = '50'
        # self.assertRaises(TypeError)
        with self.assertRaises(TypeError):
            p.quant = '50'


if __name__ == "__main__":
    unittest.main()
