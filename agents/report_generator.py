# report_generator.py

class ReportGeneratorAgent:
    def generate_report(self, insights):
        report_lines = [
            "Retail Sales Analysis Report",
            "=============================",
            f"Total Sales: ${insights['total_sales']:.2f}",
            f"Total Word Count: {insights['total_word_count']}",
            "",
            "Sales by Region:"
        ]

        for region, sales in insights['sales_by_region'].items():
            report_lines.append(f" - {region}: ${sales:.2f}")

        report_lines.append("\nSales by Product:")
        for product, sales in insights['sales_by_product'].items():
            report_lines.append(f" - {product}: ${sales:.2f}")

        return "\n".join(report_lines)
