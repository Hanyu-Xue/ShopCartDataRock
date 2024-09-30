# Checkout System for Datarock Computer Store

## Overview

This project is a checkout system for Datarock's computer store. The system processes products from the store's catalogue and applies certain pricing rules for discounts and deals. The checkout system supports scanning products in any order and computes the total cost based on the following pricing rules:

### Catalogue

| SKU  | Name          | Price   |
| ---- | ------------- | ------- |
| ipd  | Super iPad     | $549.99 |
| mbp  | MacBook Pro    | $1399.99 |
| atv  | Apple TV       | $109.50 |
| vga  | VGA adapter    | $30.00  |

### Special Pricing Rules

1. **Apple TV (SKU: atv)** - "3 for 2" deal: Buy 3 Apple TVs and only pay for 2.
2. **Super iPad (SKU: ipd)** - Bulk discount: If more than 4 iPads are purchased, the price drops to $499.99 each.
3. **MacBook Pro (SKU: mbp)** - Free VGA adapter: Buy a MacBook Pro and get a VGA adapter for free.

## Features

- Scan items in any order.
- Flexible pricing rules, allowing for future changes.
- Special deals automatically applied during checkout.

## Installation

To run this project, you need Python 3.x installed. Follow these steps to set up and run the project:

1. Clone the repository:

```bash
git clone https://github.com/Hanyu-Xue/ShopCartDataRock.git
cd ShopCartDataRock
```

2. Install required dependencies (if any). No external libraries are needed for the core system, but for testing, you may need `unittest` which is included with Python.

```bash
pip install unittest
```

3. Run the main code tests:

```bash
python main.py
```

4. To run the unit tests, use:

```bash
python -m unittest Utest
```

## Usage

The checkout system can be used as follows:

1. **Initialize the Checkout System**:
   
   ```python
   from PriceRules import pricing_rules
   from CheckOut import Checkout

   co = Checkout(pricing_rules)
   ```

2. **Scan Items**:
   
   ```python
   co.scan("atv")
   co.scan("ipd")
   co.scan("mbp")
   ```

3. **Calculate Total**:
   
   ```python
   total = co.total()
   print(f"Total: ${total:.2f}")
   ```

### Example Scenario

Here’s an example of how the checkout system works:

```python
# Example 1: SKUs Scanned: atv, atv, atv, vga
# Total expected: $249.00 (Apple TV 3 for 2 deal applied)
co.scan("atv")
co.scan("atv")
co.scan("atv")
co.scan("vga")
total = co.total()
print(f"Total: ${total:.2f}")  # Output: Total: $249.00
```

## Code Structure

- **CheckOut.py**: Contains the `Checkout` class that implements the checkout logic.
- **PriceRules.py**: Contains the `priceing_rules` class that implements special pricing rules applied during checkout.
- **Utest.py**: Contains unit tests for the checkout system, ensuring that the correct pricing and rules are applied.

### Checkout Class

The `Checkout` class implements the following key methods:

- `scan(item_sku)`: Adds a product to the checkout system.
- `total()`: Returns the total cost after applying all pricing rules.

## Pricing Rules

The pricing rules are defined in a flexible way to allow easy modifications. The system currently supports three special offers:

- **Apple TV**: Buy 3, pay for 2.
- **Super iPad**: Price drops to $499.99 when purchasing more than 4.
- **MacBook Pro**: Free VGA adapter with every MacBook Pro purchase.

## Testing

Unit tests are included to validate the functionality and correctness of the checkout system. The tests are located in the `tests` directory and can be run using the following command:

```bash
python -m unittest Utest
```


