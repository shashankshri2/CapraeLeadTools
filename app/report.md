# 📄 Caprae Capital – AI-Readiness Challenge Submission

## 🎯 Objective

To design lightweight, high-impact tools that optimize and streamline the lead generation process by:

- ✅ Verifying email and domain quality
- 🔥 Scoring leads based on business intent
- 📥 Enabling easy export for outreach/CRM integration

Built in under 5 hours for Caprae Capital’s AI-Readiness Challenge.

---

## 🧩 Tools Developed

### 1. ✅ Email & Domain Verifier

- **Validates email format** using regex
- **Checks domain status** by pinging the domain via HTTP
- Prevents outreach to fake or unreachable leads
- Saves time by instantly filtering invalid inputs

---

### 2. 🔥 Hot Lead Scorer

- Crawls the lead’s website using `requests` and `BeautifulSoup`
- Scans for **growth, hiring, and AI-related keywords** like:
  - `"AI"`, `"machine learning"`, `"book a demo"`, `"we're hiring"`, `"automation"`, `"data-driven"`, etc.
- Assigns a **lead score from 0 to 15**
- Displays **which keywords were found** to explain scoring
- Prioritizes leads with **high growth potential** and **AI readiness**

---

### 3. 📥 Export to CSV

- Once a lead is verified and scored, it can be **downloaded as a CSV**
- Fields exported: email, domain, lead score, keywords found, website URL
- Optimized for **easy upload into CRM systems** or follow-up lists

---

## 🛠 Tech Stack

- **Python** – core development
- **Streamlit** – fast UI for testing and demonstration
- **BeautifulSoup + Requests** – scraping and parsing website data
- **Pandas** – handling CSV export

---

## 📌 Evaluation Criteria Alignment

| Criteria | Description |
|---------|-------------|
| **Business Use Case Understanding** | Focuses on solving real sales problems: lead prioritization, quality filtering, and export-ready data |
| **UX/UI** | Minimalistic, clean UI via Streamlit for fast and effective interaction |
| **Technicality** | Handles HTTP requests, domain validation, web scraping, scoring logic, and CSV handling |
| **Design** | Clear visual structure, keyword display, result highlighting, download button |
| **Other / Innovation** | Keyword highlighting, CRM-friendly format, modular code for future enhancements |

---

## 💼 Business Value

- Reduces time spent on invalid or cold leads
- Helps sales teams focus on **high-quality, high-intent targets**
- Improves productivity with ready-to-export data
- Supports Caprae's goal of **AI-focused transformation** in business operations

---

## 🔚 Summary

This submission includes:
- ✅ Practical, usable tools
- ⚙️ Fast and scalable implementation
- 🎯 Real-world application for Caprae’s M&A and SaaS/AI goals

We look forward to the opportunity to contribute to Caprae’s mission of building world-class, operator-led businesses.

