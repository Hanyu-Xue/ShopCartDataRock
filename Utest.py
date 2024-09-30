import unittest
from main import PricingRules,Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = PricingRules()
        self.co = Checkout(self.pricing_rules)

    def test_scenario1(self):
        """
        Check the atv deal
        """
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 249.00)

    def test_scenario2(self):
        """
        Check the ipad
        """
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 2718.95)

    def test_scenario3(self):
        """
        Check the mbp and vga
        """
        self.co.scan('mbp')
        self.co.scan('vga')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 1949.98)


if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestSuite()

    # Add tests to the suite
    suite.addTest(unittest.makeSuite(TestCheckout))

    # Create a test runner and run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)