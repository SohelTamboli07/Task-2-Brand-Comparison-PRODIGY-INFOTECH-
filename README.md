# Task-2-Brand-Comparison-PRODIGY-INFOTECH
Apple vs Samsung — Public Opinion Sentiment Analysis 📱📊
A simple, end-to-end sentiment analysis project that compares public opinions about Apple vs Samsung using a small, sample social media dataset. It performs basic text preprocessing, lexicon-based sentiment scoring, and generates visualizations including histograms, brand-wise counts, a pie chart, and word clouds.

✨ Features
Lightweight, no external APIs needed
Clean, readable Python code
Lexicon-based sentiment scoring (positive vs negative words)
Brand-wise comparison (Apple vs Samsung)
Visualizations:
Sentiment score distribution
Brand-wise sentiment counts
Overall sentiment pie chart
Word clouds for Apple and Samsung
🧰 Tech Stack
Python 3.8+
pandas, re
matplotlib, seaborn
wordcloud
📦 Installation
Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
(Optional) Create a virtual environment
python -m venv .venv
On Windows: .venv\Scripts\activate
On macOS/Linux: source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
or
pip install pandas matplotlib seaborn wordcloud
requirements.txt

pandas
matplotlib
seaborn
wordcloud
▶️ How to Run
Run the script (adjust filename if different):

python apple_samsung_sentiment.py
What it does:

Loads a small, hardcoded dataset of Apple and Samsung tweets
Cleans text (lowercase, remove URLs, punctuation)
Scores each tweet using a simple positive/negative lexicon
Prints a table with scores and sentiment labels
Displays:
Sentiment histogram
Brand-wise sentiment count plot
Overall sentiment pie chart
Word clouds for each brand
🗂️ Project Structure (suggested)
.
├── apple_samsung_sentiment.py # Main script (your code)
├── requirements.txt
├── README.md
└── assets/ # (Optional) Save generated plots here
🧪 Sample Dataset (first few rows)
tweet	brand
I love the new Apple iPhone, camera quality is best!	Apple
Samsung battery life is amazing.	Samsung
Apple phones are too expensive.	Apple
Samsung UI is bad and full of lag.	Samsung
I am happy with my Apple device!	Apple
The full dataset is defined directly in the script.

🧠 How It Works
Text preprocessing
Lowercasing
Removing URLs
Removing punctuation and extra spaces
Lexicon-based sentiment
Positive words: good, great, awesome, amazing, fantastic, love, best, happy, smooth, liked, fast, excellent
Negative words: bad, terrible, hate, worst, expensive, lag, drains, overheat
Score = count(positive tokens) - count(negative tokens)
Label: positive if score > 0, negative if score < 0, else neutral
Visualizations
Sentiment score histogram
Brand-wise sentiment comparison (countplot)
Overall sentiment distribution (pie)
Word clouds per brand
🖼️ Saving Plots (optional)
If you want to save plots instead of showing them:

Replace plt.show() with:
plt.savefig("assets/plot_name.png", dpi=200, bbox_inches="tight"); plt.close()
📈 Example Insights (from the sample)
Apple: generally positive (ecosystem, performance) with some negatives (price, battery drain)
Samsung: praise for battery, camera, and display; negatives around UI lag and occasional heating
Note: These are based on a tiny sample for demonstration only.

🔧 Customization
Add more tweets
Update the data list in the script
Expand the sentiment lexicon
Add stems/variations (e.g., fast vs fastest) or implement lemmatization
Try better sentiment models
VADER (rule-based), TextBlob, or transformer-based models (Hugging Face)
Improve cleaning
Handle emojis, hashtags, contractions, negations (e.g., “not good”)
Export results
df.to_csv("results.csv", index=False)
⚠️ Limitations
Very small, synthetic dataset
Lexicon approach is simplistic (no context, negation, or sarcasm handling)
Token matching is exact (e.g., "fastest" ≠ "fast" unless added)
🤝 Contributing
Contributions are welcome!

Fork the repo
Create a feature branch
Submit a pull request with a clear description
📜 License
Add your preferred license (e.g., MIT). If none is provided, the default is “All rights reserved.”

🙌 Acknowledgments
Matplotlib, Seaborn, WordCloud, and pandas communities
Inspired by classic lexicon-based sentiment analysis approaches
📬 Contact
Questions or suggestions? Open an issue or reach out via GitHub Discussions.

Happy analyzing! 🚀






