import pandas as pd
import os

# Ορίζουμε τις διαδρομές για το βασικό αρχείο της Eurostat
input_file = os.path.join('data_raw', 'isoc_sks_itsps$defaultview_linear.csv')
output_file = os.path.join('data_clean', 'clean_eurostat_ict.csv')

print(f"Διαβάζουμε το αρχείο της Eurostat: {input_file}")

try:
    # Φόρτωση του CSV
    df_eu = pd.read_csv(input_file)
    
    # Κρατάμε το σύνολο των εργαζομένων, αγνοώντας τον διαχωρισμό ανά φύλο για τη βασική πρόβλεψη
    if 'sex' in df_eu.columns:
        if 'T' in df_eu['sex'].unique(): # Η Eurostat συχνά χρησιμοποιεί 'T' για το Total
            df_eu = df_eu[df_eu['sex'] == 'T']
        elif 'Total' in df_eu['sex'].unique():
            df_eu = df_eu[df_eu['sex'] == 'Total']
    
    # Επιλογή χρήσιμων στηλών (Γεωγραφική περιοχή, Έτος, Ποσοστό/Τιμή)
    cols_to_keep = [col for col in ['geo', 'TIME_PERIOD', 'OBS_VALUE'] if col in df_eu.columns]
    df_eu_clean = df_eu[cols_to_keep].copy()
    
    # Μετονομασία για ομοιομορφία στη βάση δεδομένων
    df_eu_clean.columns = ['Country', 'Year', 'ICT_Percentage']
    
    # Αφαίρεση κενών γραμμών
    df_eu_clean = df_eu_clean.dropna(subset=['ICT_Percentage'])
    
    # Αποθήκευση του καθαρού αρχείου
    df_eu_clean.to_csv(output_file, index=False)
    
    print("\n--- ΟΛΟΚΛΗΡΩΘΗΚΕ ΕΠΙΤΥΧΩΣ ---")
    print(f"Το καθαρό αρχείο της Eurostat αποθηκεύτηκε στο: {output_file}")
    print(f"Συνολικές καθαρές εγγραφές (Χώρα/Έτος): {len(df_eu_clean)}")

except FileNotFoundError:
    print(f"Σφάλμα: Δεν βρέθηκε το αρχείο. Βεβαιώσου ότι το όνομα στο data_raw είναι ακριβώς 'isoc_sks_itsps$defaultview_linear.csv'.")
except Exception as e:
    print(f"Προέκυψε απρόσμενο σφάλμα: {e}")