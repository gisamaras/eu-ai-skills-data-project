import pandas as pd
from sqlalchemy import create_engine
import os

# Βάλε τον δικό σου κωδικό της PostgreSQL
db_user = 'postgres'
db_password = '123456' 
db_host = 'localhost'
db_port = '5432'
db_name = 'eu_skills_db' # Δημιούργησε πρώτα μια κενή βάση με αυτό το όνομα

print("Σύνδεση με τη βάση δεδομένων...")
try:
    # Δημιουργία του connection engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Διαδρομές αρχείων
    file_eurostat = os.path.join('data_clean', 'clean_eurostat_ict.csv')
    file_postings = os.path.join('data_clean', 'clean_ai_postings.csv')

    # 1. Εισαγωγή Eurostat
    print("Μεταφορά δεδομένων Eurostat (1/2)...")
    df_eu = pd.read_csv(file_eurostat)
    df_eu.to_sql('eurostat_ict', engine, if_exists='replace', index=False)

    # 2. Εισαγωγή Αγγελιών Kaggle
    print("Μεταφορά αγγελιών Kaggle (2/2)...")
    df_ai = pd.read_csv(file_postings)
    df_ai.to_sql('ai_postings', engine, if_exists='replace', index=False)

    print("\n--- ΟΛΟΚΛΗΡΩΘΗΚΕ ΕΠΙΤΥΧΩΣ ---")
    print("Όλα τα δεδομένα βρίσκονται πλέον με ασφάλεια στην PostgreSQL!")

except Exception as e:
    print(f"Προέκυψε σφάλμα: {e}")