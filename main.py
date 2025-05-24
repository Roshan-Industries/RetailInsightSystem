from agents.data_collector import DataCollectorAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_generator import ReportGeneratorAgent
from agents.visualizer import VisualizerAgent

def run_analysis():
    collector = DataCollectorAgent()
    data = collector.collect_data()

    analyst = DataAnalystAgent()
    sales_summary = analyst.summarize_sales(data)

    visualizer = VisualizerAgent()
    chart_path = visualizer.plot_sales(sales_summary)

    reporter = ReportGeneratorAgent()
    report_text = reporter.generate_report(sales_summary)

    return report_text, chart_path

if __name__ == "__main__":
    report, chart = run_analysis()
    print(report)
    print(f"Chart saved at: {chart}")
