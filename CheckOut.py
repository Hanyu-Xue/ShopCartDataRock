class Checkout:
    """
    Define the Checkout System
    The Checkout class uses the PricingRules to calculate the total price based on scanned items.
    """
    def __init__(self, pricing_rules):
        self.items = []
        self.pricing_rules = pricing_rules

    def scan(self, item):
        """
        Add an item to the list of scanned items.
        """
        self.items.append(item)

    def total(self):
        """
        Calculate the total cost based on the scanned items and pricing rules.
        """
        return self.pricing_rules.apply_deals(self.items)