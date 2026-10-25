import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings('ignore')

print("Σύνδεση με την PostgreSQL και άντληση δεδομένων...")
engine = create_engine('postgresql://postgres:123456@localhost:5432/eu_skills_db')

try:
    df = pd.read_sql('SELECT * FROM eurostat_ict', engine)
    
    # Υπολογισμός της γενικής τάσης ανά έτος
    df_trend = df.groupby('Year')['ICT_Percentage'].mean().reset_index()

    X = df_trend[['Year']]
    y = df_trend['ICT_Percentage']

    print("Εκπαίδευση του αλγορίθμου Linear Regression (Γραμμική Παλινδρόμηση)...")
    model = LinearRegression()
    model.fit(X, y)

    future_years = pd.DataFrame({'Year': [2027, 2028, 2029, 2030, 2031]})
    predictions = model.predict(future_years)
    future_years['Predicted_ICT_Percentage'] = predictions

    print("\n--- ΑΠΟΤΕΛΕΣΜΑΤΑ ΠΡΟΒΛΕΨΗΣ (2027-2031) ---")
    for index, row in future_years.iterrows():
        print(f"Έτος {int(row['Year'])}: Εκτιμώμενη τιμή -> {row['Predicted_ICT_Percentage']:.2f}")
        
    future_years.to_sql('ml_predictions_linear', engine, if_exists='replace', index=False)
    print("\nΕπιτυχία! Οι ρεαλιστικές προβλέψεις αποθηκεύτηκαν στον πίνακα 'ml_predictions_linear'.")

except Exception as e:
    print(f"Προέκυψε σφάλμα: {e}")