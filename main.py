from PriceRules import PricingRules
from CheckOut import Checkout

if __name__ == "__main__":
    """
    Create some example scenarios to test the implementation.
    """
    print('=================Load Price Rules=================')
    # Pricing rules
    pricing_rules = PricingRules()

    # Scenario 1: atv, atv, atv, vga
    print('=================Scenario 1=======================')
    co = Checkout(pricing_rules)
    co.scan('atv')
    co.scan('atv')
    co.scan('atv')
    co.scan('vga')
    print('Items in the cart:', co.items)
    print(f'Total: {co.total():.2f}')  # Should be $249.00

    # Scenario 2: atv, ipd, ipd, atv, ipd, ipd, ipd
    print('=================Scenario 2=======================')
    co = Checkout(pricing_rules)
    co.scan('atv')
    co.scan('ipd')
    co.scan('ipd')
    co.scan('atv')
    co.scan('ipd')
    co.scan('ipd')
    co.scan('ipd')
    print('Items in the cart:', co.items)
    print(f'Total: {co.total():.2f}')  # Should be $2718.95

    # Scenario 3: mbp, vga, ipd
    print('=================Scenario 3=======================')
    co = Checkout(pricing_rules)
    co.scan('mbp')
    co.scan('vga')
    co.scan('ipd')
    print('Items in the cart:', co.items)
    print(f'Total: {co.total():.2f}')  # Should be $1949.98