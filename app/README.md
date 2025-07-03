# 🚀 Caprae Lead Tools

Lightweight, powerful tools to supercharge lead generation and qualification — built for Caprae Capital’s **AI-Readiness Pre-Screening Challenge**.

---

## 🧩 Features

### ✅ 1. Email & Domain Verifier
- Validates if the email is **properly formatted**
- Checks if the **domain is active** and accessible

### 🔥 2. Hot Lead Scorer
- Crawls a lead's website content
- Detects keywords that indicate **AI, automation, hiring, growth, or innovation**
- Assigns a **score (0–15)** to help prioritize hot leads
- Displays **which keywords** were found for transparency

### 📥 3. Export to CSV
- After verification and scoring, users can **download lead data**
- File includes email, domain, lead score, found keywords, and website
- Ready for use in CRM systems or manual outreach

---

## 💻 Tech Stack

- Python 🐍
- [Streamlit](https://streamlit.io/) – UI framework
- Requests + BeautifulSoup – Web scraping
- Pandas – Data processing and CSV export

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/CapraeLeadTools.git
cd CapraeLeadTools
2. Install the required packages
pip install -r requirements.txt

3. Run the Streamlit App
streamlit run app/app.py

📌 Sample Output
Email & Domain Verifier:
Email Format: ✅ Valid format
Domain Status: ✅ Active
Lead Score: 9/15
🔥 This lead looks HOT!
Keywords found: AI, automation, we’re hiring
CSV Export Output:

Email: someone@example.com

Domain: example.com

Lead Score: 9

Keywords Found: AI, automation

Website: https://example.com

🧠 Why These Tools Matter
These tools help businesses:

Clean their lead data ✅

Prioritize high-potential prospects ✅

Save time on cold or fake leads ✅

Integrate leads into CRMs easily ✅