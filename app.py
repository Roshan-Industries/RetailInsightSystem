# app.py

import streamlit as st
import csv
import requests

from agents.data_analyzer import DataAnalyzerAgent
from agents.visualizer import VisualizerAgent
from agents.report_generator import ReportGeneratorAgent
from agents.chatbot_agent import ChatbotAgent
from agents.gpt_agent import GPTAgent

st.set_page_config(page_title="Retail Insight System", layout="wide")

st.title("🧠 Retail Insight System")

# Sidebar navigation
tabs = ["📊 Data Dashboard", "🤖 Chatbot Assistant"]
selected_tab = st.sidebar.radio("Select a tab", tabs)

# === TAB 1: DASHBOARD ===
if selected_tab == "📊 Data Dashboard":
    uploaded_file = st.file_uploader("Upload your retail sales CSV", type=["csv"])

    if uploaded_file:
        reader = csv.DictReader(uploaded_file.read().decode("utf-8").splitlines())
        data = list(reader)

        analyzer = DataAnalyzerAgent()
        insights = analyzer.analyze(data)

        st.subheader("Key Insights")
        st.write(f"Total Sales: **${insights['total_sales']:.2f}**")
        st.write(f"Total Word Count: **{insights['total_word_count']}**")

        st.subheader("Sales by Region")
        st.bar_chart(insights['sales_by_region'])

        st.subheader("Sales by Product")
        st.bar_chart(insights['sales_by_product'])

        # Generate report
        reporter = ReportGeneratorAgent()
        report = reporter.generate_report(insights)
        st.download_button("📥 Download Insights Report", report.encode(), file_name="insights_report.txt")

        # Word cloud image
        visualizer = VisualizerAgent()
        image_path = visualizer.generate_word_chart(insights['sales_by_product'])
        st.image(image_path, caption="Sales Word Chart")

# === TAB 2: CHATBOT ===
chatbot_agent = ChatbotAgent()

st.subheader("🧠 Retail Insight System")
st.subheader("🤖 Ask the Assistant")

user_query = st.text_input("Type your question here...")

if user_query:
    response = chatbot_agent.chat(user_query)
    st.write(response)
