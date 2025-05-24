class DataAnalystAgent:
    def summarize_sales(self, data):
        region_sales = {}
        for row in data:
            region = row.get('region', 'Unknown')
            sales = float(row.get('sales') or 0)
            region_sales[region] = region_sales.get(region, 0) + sales
        return region_sales
