class DataCollectorAgent:
    def collect(self, data):
        # Perform any cleaning if needed
        cleaned_data = data.dropna(subset=['product_name', 'sales'])
        return cleaned_data
