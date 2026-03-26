import os
import requests
import re
import database # Importăm seiful nostru

# Avem nevoie de un API Key de la Serper.dev (e gratuit pentru primele căutări)
SERPER_API_KEY = os.environ.get('SERPER_API_KEY')

def search_google(query):
    """Căutăm pe Google site-uri relevante"""
    url = "https://google.serper.dev/search"
    payload = {"q": query, "num": 10}
    headers = {'X-API-KEY': SERPER_API_KEY, 'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get('organic', [])

def extract_emails(text):
    """Căutăm pattern-uri de email în text"""
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def start_mining(niche="firme constructii Romania"):
    """Funcția principală de minerit"""
    print(f"DEBUG: Începem mineritul pentru nișa: {niche}")
    results = search_google(f'"{niche}" contact email')
    
    for res in results:
        snippet = res.get('snippet', '')
        emails = extract_emails(snippet)
        
        for email in emails:
            lead = {
                'email': email,
                'company_name': res.get('title'),
                'source_url': res.get('link'),
                'ip_address': '0.0.0.0', # Placeholder
                'hoster': 'Cloud'
            }
            database.save_lead(lead)
            print(f"SUCCES: Am găsit și salvat {email}")

if __name__ == "__main__":
    # Inițializăm baza de date înainte de minerit
    database.init_db()
    start_mining()
