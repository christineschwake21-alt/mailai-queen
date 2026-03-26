import os
import psycopg2

# Citim cheia "DATABASE_URL" de pe Railway
DATABASE_URL = os.environ.get('DATABASE_URL')

def init_db():
    """Creează seiful pentru cele 300.000 de lead-uri"""
    try:
        # Ne conectăm folosind cheia universală
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id SERIAL PRIMARY KEY,
                email TEXT UNIQUE,
                company_name TEXT,
                source_url TEXT,
                status TEXT DEFAULT 'New',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("SISTEM: Seiful este deschis și gata!")
    except Exception as e:
        print(f"EROARE DB: {e}")
