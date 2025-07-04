# 💰 IFB/2024/8.5 Earnings Calculator

This is a **Flask web application** that allows investors to monitor and calculate the **expected earnings from the Infrastructure Bond (IFB1/2024/8.5)** issued by the **Central Bank of Kenya in February 2024**.

The application provides a user-friendly interface to determine interest payouts, amortization payments, and total returns over the life of the bond based on the investment amount.

---

## 📈 What the Project Does

- Accepts an investment amount in Kenyan Shillings (KES)
- Validates that the amount is in chunks of **KES 50,000**
- Floors any input amount to the nearest lower multiple of 50,000
- Computes and displays:
  - Semi-annual interest payments
  - Principal amortizations (20% and 30% scheduled during bond life)
  - Total interest earned
  - Total gross payback at maturity

Example:  
If you invest **KES 120,000**, only **KES 100,000** will be considered.

---

## 🧮 Bond Details (IFB1/2024/8.5)

- **Issued:** 19 February 2024
- **Maturity Date:** 9 August 2032
- **Tenor:** 8.5 years
- **Interest Rate:** 18.4607% per annum (paid semi-annually)
- **Amortization Schedule:**
  - **20%** on 15 Feb 2027
  - **30%** on 11 Feb 2030

Read the full prospectus [here](https://www.centralbank.go.ke/uploads/treasury_bonds_prospectuses/2087959385_February%202024%20IFB1-2024-8.5%20%20DATED%2019-02-2024.pdf)

---

## 🖥️ Application Structure

```plaintext
├── application.py           # Flask entrypoint
├── ifb.py                   # Core bond logic and calculation
├── templates/
│   ├── index.htm            # Home input form
│   └── payout.html          # Result page with payout table
├── static/
│   └── web_styles.css       # Custom CSS for UI
├── requirements.txt         # Python dependencies
├── run.sh                   # Gunicorn startup script
├── app.wsgi                 # WSGI entrypoint
├── README.md                # You’re here
└── .gitignore
```

## 🚀 Running the Project Locally

1. Clone the Repo
```
git clone https://github.com/karianjahi/ifb-2024.git
cd ifb2024
```

2. Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Run the application
```
python application.py
```

5. Then visit: http://127.0.0.1:5000 in your browser.

## 📊 Example Output
After submitting your investment (e.g., KES 250,000), the app displays:

All interest payments over the years

Dates and amounts for amortization

Total interest earned

Total gross amount payable at maturity

## ⚠️ Investment Rule
Only amounts in KES 50,000 chunks are valid. Inputs like 75,000 or 98,000 will be floored to the nearest valid chunk (e.g., 50,000).

## ✅ Technologies Used
- Python 3

- Flask

- HTML, CSS, JS (for input formatting)

- Babel (for currency formatting)

- Gunicorn (optional for production)

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
Joseph Karianjahi
📧 nkarianjahi@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/josephkarianjahinjeri)
🔗 [GitHub](https://github.com/karianjahi)

## 🙌 Contributions
- Feel free to fork this repository and submit pull requests. 
- Feature suggestions, bug reports, and improvements are always welcome!
