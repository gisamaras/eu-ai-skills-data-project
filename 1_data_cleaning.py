import pandas as pd
import re
import os

# Ορίζουμε τις διαδρομές των φακέλων που φτιάξαμε
input_file = os.path.join('data_raw', 'postings.csv')
output_file = os.path.join('data_clean', 'clean_ai_postings.csv')

# Δημιουργία του φακέλου data_clean αν δεν υπάρχει
os.makedirs('data_clean', exist_ok=True)

# Λέξεις-κλειδιά για να εντοπίσουμε αγγελίες Τεχνολογίας & Κανονιστικής Συμμόρφωσης
it_keywords = ['data scientist', 'machine learning', 'artificial intelligence', 
               ' ai ', 'data engineer', 'software', 'developer', 'nlp', 'compliance', 'cybersecurity']

print(f"Διαβάζουμε το αρχείο: {input_file}")
print("Η διαδικασία ίσως διαρκέσει 1-2 λεπτά λόγω του μεγέθους των 516MB...")

try:
    # 1. Φόρτωση του CSV
    df = pd.read_csv(input_file)
    
    # Μετατρέπουμε τα ονόματα των στηλών σε πεζά (lowercase) για να μην έχουμε θέματα
    df.columns = [col.lower() for col in df.columns]
    
    print(f"Φορτώθηκαν συνολικά {len(df)} αγγελίες. Ξεκινάει το φιλτράρισμα...")
    
    # 2. Φιλτράρισμα με βάση τον τίτλο (title)
    pattern = '|'.join(it_keywords)
    df_filtered = df[df['title'].astype(str).str.lower().str.contains(pattern, na=False)].copy()
    
    # 3. Καθαρισμός του κειμένου της περιγραφής (description) - Προετοιμασία για NLP
    def clean_text(text):
        text = str(text)
        text = re.sub(r'<[^>]+>', ' ', text) # Αφαίρεση HTML (π.χ. <br>, <li>)
        text = re.sub(r'[^a-zA-Z0-9\s.,]', '', text) # Κρατάμε μόνο αλφαριθμητικά
        text = re.sub(r'\s+', ' ', text).strip() # Αφαίρεση πολλαπλών κενών
        return text

    print("Γίνεται καθαρισμός του αδόμητου κειμένου (NLP Regex Cleaning)...")
    df_filtered['clean_description'] = df_filtered['description'].apply(clean_text)
    
    # 4. Αποθήκευση του καθαρού αρχείου
    df_filtered.to_csv(output_file, index=False)
    
    print("\n--- ΟΛΟΚΛΗΡΩΘΗΚΕ ΕΠΙΤΥΧΩΣ ---")
    print(f"Από τις {len(df)} αρχικές αγγελίες, εντοπίστηκαν και καθαρίστηκαν {len(df_filtered)} σχετικές αγγελίες.")
    print(f"Το νέο αρχείο αποθηκεύτηκε στο: {output_file}")

except FileNotFoundError:
    print(f"Σφάλμα: Δεν βρέθηκε το αρχείο {input_file}. Βεβαιώσου ότι το έβαλες μέσα στον φάκελο data_raw.")
except Exception as e:
    print(f"Προέκυψε απρόσμενο σφάλμα: {e}")