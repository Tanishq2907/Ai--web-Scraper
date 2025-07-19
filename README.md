# 🧠 AI-Powered Web Scraper

An intelligent, user-friendly web scraping tool that combines automation with natural language processing (NLP) to extract structured data from websites — without writing a single line of scraping logic.

---

## 🔍 Overview

This project simplifies web data extraction by allowing users to input a website URL and a natural language query (e.g., "Extract all book titles"). It scrapes both static and dynamic content, filters out irrelevant sections (like ads or navigation bars), and returns clean, structured results in JSON/CSV format.

---

## 🚀 Key Features

- ✅ **No-Code Scraping**: Extract data using simple natural language queries  
- ⚙️ **Dual Scraping Engine**: Uses ScrapingBee API with fallback to Selenium  
- 🧠 **AI Integration**: DeepSeek R1 LLM (via Ollama) interprets and extracts relevant content  
- 🧹 **Noise Filtering**: Removes unwanted content like ads, footers, and scripts  
- 📦 **Data Export**: Results available in JSON or CSV  
- 🧑‍💻 **User Interface**: Built with Streamlit for seamless user interaction  

---

## 🧱 Tech Stack

| Component      | Technology                        |
|----------------|-----------------------------------|
| Language       | Python 3.9+                       |
| UI Framework   | Streamlit                         |
| Web Scraping   | ScrapingBee API, Selenium, Requests, BeautifulSoup |
| AI Model       | DeepSeek R1 via Ollama (local LLM)|
| Data Handling  | JSON, CSV                         |
| Automation     | ChromeDriver                      |

---

## 🖥️ System Requirements

### Software
- Python 3.9+
- Chrome Browser + ChromeDriver
- Streamlit, BeautifulSoup, Selenium, Requests
- Ollama (for local LLM inference)
- ScrapingBee API key

### Hardware
- RAM: 16 GB minimum
- CPU: Intel i5 8th Gen / AMD Ryzen 5+
- (Optional) GPU: NVIDIA with 6GB+ VRAM for faster AI inference

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper
# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # For macOS/Linux
# OR
venv\Scripts\activate         # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Ollama with DeepSeek R1
ollama run deepseek

# 5. Start the Streamlit app
streamlit run app.py


   
