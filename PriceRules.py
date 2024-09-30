class PricingRules:
    """
    Define the Pricing Rules
    Create pricing rules that apply special deals like:
        "3 for 2 on Apple TV,"
        bulk discount on iPads,
        free VGA adapter with MacBook Pro.
    """
    def __init__(self):
        self.rules = {
            'atv': {'price': 109.50, 'deal': '3-for-2'},
            'ipd': {'price': 549.99, 'bulk_discount': {'min_qty': 5, 'discount_price': 499.99}},
            'mbp': {'price': 1399.99, 'bundle': 'vga'},
            'vga': {'price': 30.00}
        }

    def apply_deals(self, items):
      """
      Apply special deals to the items based on the rules.
      """
      total = 0
      item_count = {item: items.count(item) for item in set(items)}

      # Handle MacBook Pro (mbp) free VGA adapter first
      if 'mbp' in item_count and 'vga' in item_count:
          vga_qty = min(item_count.get('vga', 0), item_count['mbp'])  # Free VGA for each mbp
          item_count['vga'] -= vga_qty

      # Apply other deals
      for sku, qty in item_count.items():
          rule = self.rules.get(sku)

          # Apply 3-for-2 deal for Apple TV (atv)
          if sku == 'atv' and rule.get('deal') == '3-for-2':
              total += (qty // 3) * 2 * rule['price'] + (qty % 3) * rule['price']

          # Apply bulk discount for iPads (ipd)
          elif sku == 'ipd' and qty >= rule.get('bulk_discount', {}).get('min_qty', 0):
              total += qty * rule.get('bulk_discount', {}).get('discount_price', rule['price'])

          # Calculate the price for other items
          elif rule:
              total += qty * rule['price']

      return total