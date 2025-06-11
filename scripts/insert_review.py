import pandas as pd
import oracledb

# DB connection config
DB_USER = "bank_admin"
DB_PASSWORD = "root"
DB_DSN = "localhost/XEPDB1"

# Load CSV
df = pd.read_csv("data/bank_reviews_20250609_035132.csv")
print(f" Data shape: {df.shape}")

# Connect to Oracle
conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
cursor = conn.cursor()

# Step 1: Insert unique banks
banks = df["bank_name"].dropna().unique()
print(f" Found {len(banks)} unique banks")

for bank in banks:
    cursor.execute("""
        MERGE INTO banks b
        USING (SELECT :name AS name FROM dual) input
        ON (b.name = input.name)
        WHEN NOT MATCHED THEN
            INSERT (name) VALUES (:name)
    """, {"name": bank})

conn.commit()

# Step 2: Build bank_name → bank_id map
cursor.execute("SELECT bank_id, name FROM banks")
bank_map = {name: bank_id for bank_id, name in cursor}
print(f" Bank map: {bank_map}")

# Step 3: Insert reviews
inserted = 0
for _, row in df.iterrows():
    bank_id = bank_map.get(row["bank_name"])
    if not bank_id:
        print(f" Bank not found for: {row['bank_name']}")
        continue

    cursor.execute("""
        INSERT INTO reviews (bank_id, review_text, rating, review_date, source)
        VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)
    """, (
        bank_id,
        row["review_text"],
        row["rating"],
        row["date"],
        row["source"]
    ))
    inserted += 1

conn.commit()
print(f"Inserted {inserted} reviews")

cursor.close()
conn.close()
