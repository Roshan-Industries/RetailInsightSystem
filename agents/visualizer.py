# agents/visualizer.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud

class VisualizerAgent:
    def generate_word_chart(self, sales_by_product, output_path="output/word_chart.png"):
        word_freq = {product: int(sales) for product, sales in sales_by_product.items()}

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=0)

        plt.savefig(output_path)
        plt.close()
        return output_path
