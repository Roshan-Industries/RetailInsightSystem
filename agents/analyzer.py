# analyzer.py

class Analyzer:
    def analyze(self, data):
        insights = {
            'total_sales': 0.0,
            'sales_by_region': {},
            'sales_by_product': {},
            'total_word_count': 0
        }

        for row in data:
            region = row.get('region', 'Unknown')
            product = row.get('product', 'Unknown')
            sales_value = row.get('sales')
            try:
                amount = float(sales_value) if sales_value is not None else 0.0
            except ValueError:
                amount = 0.0

            insights['total_sales'] += amount

            insights['sales_by_region'][region] = insights['sales_by_region'].get(region, 0.0) + amount
            insights['sales_by_product'][product] = insights['sales_by_product'].get(product, 0.0) + amount

            insights['total_word_count'] += len(product.split())

        return insights
