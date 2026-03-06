**ENGLISH**

🚀 QuantAnalysis AI: Financial Intelligence Platform
This project is an end-to-end FinTech solution designed to analyze corporate financial statements, provide ratio-based insights, and interpret complex data using Gemini AI integration. It bridges the gap between raw balance sheet data and actionable investment intelligence.

Link of application : https://balance-sheet-qb2x9kqofdxs8dqc8xf4gz.streamlit.app/

🌟 Key Objectives
To simplify financial statement analysis for individual investors.

To leverage Generative AI (GenAI) for professional-grade financial commentary.

To demonstrate a scalable software architecture using Object-Oriented Programming (OOP).

🛠️ Tech Stack & Engineering
The project is built with a focus on high scalability and clean code standards:

Language: Python 3.11+

Web Framework: Streamlit (For a fast, interactive, and data-driven UI).

Artificial Intelligence: Google Gemini API (gemini-3-flash-preview) with custom System Instructions.

Data Analysis: Pandas (Financial data wrangling).

Visualization: Matplotlib (Professional financial plotting).

Architecture: * OOP & Abstraction: Utilizes Abstract Base Classes (ABC) to define a strict contract for financial ratios and calculations.

Layered Design: Distinct separation between Logic (rates.py), AI Services (Gemini.py), and Presentation (ui.py).



🏗️ Version Control & Git Management
This project is managed using Git to ensure professional development standards:

Feature-Based Commits: Logical separation of development milestones (e.g., UI implementation, AI integration, Ratio logic).

Security: Sensitive credentials (API Keys) are managed via .env files and protected by .gitignore.

CI/CD Workflow: Integrated with Streamlit Cloud for Continuous Deployment. Every git push automatically updates the live production environment.



✨ Core Features
Automated Ratio Analysis: Calculation of Current Ratio, ROE (Return on Equity), and Financial Leverage using a robust class-based system.

AI Financial Advisor: A custom-prompted Gemini model acts as a "Quant Trader" to explain ratios in plain language.

Dynamic Charting: Visualizes financial trends over time (Quarterly analysis).

Resilient Design: Comprehensive error handling for network issues (ConnectionError) or data inconsistencies (ValueError).

Bonus Tools: Personal finance modules including BES (Private Pension) calculators and budget trackers.



📂 Project Structure
├── .env                  # Secure API Credentials (Ignored by Git)
├── Gemini.py             # GenAI Service Layer & External APIs
├── rates.py              # Financial Logic & OOP Ratio Classes
├── financial_calculations.py # Personal Finance Logic
├── ui.py                 # Main Entry Point & Streamlit Interface
├── requirements.txt      # Project Dependencies
└── README.md             # Documentation


📊 Deployment
The application is live and hosted on Streamlit Cloud. It is synchronized with this GitHub repository for seamless updates.

⚠️ Disclaimer
This application is for informational purposes only and does not constitute investment advice. Financial markets involve significant risk. Always consult with a professional advisor before making investment decisions.





**TÜRKÇE**


🚀 Finansal Zeka ve Analiz Platformu (QuantAnalysis AI)
Bu proje, şirketlerin finansal tablolarını analiz eden, rasyo bazlı içgörüler sunan ve Gemini AI entegrasyonu ile verileri yorumlayan uçtan uca bir FinTech çözümüdür.

Uygulamanın Linki : https://balance-sheet-qb2x9kqofdxs8dqc8xf4gz.streamlit.app/


🛠️ Teknik Mimari ve Stack
Proje, modern yazılım mühendisliği standartları ve modüler yapı prensipleriyle inşa edilmiştir:
Dil: Python 3.11+
Web Framework: Streamlit
Yapay Zeka: Google Gemini API (Sistem Talimatlı GenAI Entegrasyonu)
Veri Yönetimi: Pandas & Matplotlib
Mimari: OOP (Object Oriented Programming), Abstract Base Classes (ABC)

🏗️ Git ile Versiyon Kontrolü ve Proje Yönetimi
Bu proje, geliştirme süreci boyunca Git sürüm kontrol sistemi ile yönetilmiştir. Bu sayede:
Modüler Geliştirme: Her bir özellik (UI, Finansal Hesaplamalar, AI Entegrasyonu) mantıksal commit'lerle takip edilmiştir.
Sürdürülebilirlik: Kod tabanındaki değişiklikler izlenebilir ve geri döndürülebilir yapıdadır.
Deployment Pipeline: Git entegrasyonu sayesinde Streamlit Cloud üzerinden sürekli dağıtım (Continuous Deployment) sağlanmıştır.


✨ Öne Çıkan Özellikler
Gelişmiş Rasyo Analizi: Cari Oran, ROE ve Kaldıraç gibi rasyoların ABC mimarisiyle hesaplanması.
Yapay Zeka Yorumu: Ham finansal verilerin Gemini API aracılığıyla "Profesyonel Analist" tonunda yorumlanması.
Dinamik Görselleştirme: Matplotlib ile zaman serisi analizleri.
Hata Yönetimi: Ağ kopmaları veya hatalı veri girişlerine karşı dirençli (Resilient) kod yapısı.


📂 Dosya Yapısı
├── .env                  # Hassas API Anahtarları (Gitignore ile korunur)
├── Gemini.py             # GenAI Servis Katmanı
├── rates.py              # Finansal Hesaplama Katmanı (OOP)
├── financial_calculations.py # Ek Yatırım Araçları
├── ui.py                 # Ana Uygulama ve Arayüz
├── requirements.txt      # Bağımlılık Listesi
└── README.md             # Proje Dokümantasyonu


📊 Deployment
Proje, Streamlit Cloud üzerinde canlıda çalışmaktadır. GitHub deposuyla senkronize olan bu yapı, her git push işleminde uygulamayı otomatik olarak günceller.
