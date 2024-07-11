import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('documents.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    expiration_date DATE NOT NULL
)
''')

# Function to add a document
def add_document(name, expiration_date):
    c.execute('INSERT INTO documents (name, expiration_date) VALUES (?, ?)', (name, expiration_date))
    conn.commit()

# Function to display documents
def display_documents():
    c.execute('SELECT * FROM documents')
    documents = c.fetchall()
    print("Documents:")
    for doc in documents:
        print(f"ID: {doc[0]}, Name: {doc[1]}, Expiration Date: {doc[2]}")

# Function to renew a document's expiration date
def renew_document(doc_id, new_expiration_date):
    c.execute('UPDATE documents SET expiration_date = ? WHERE id = ?', (new_expiration_date, doc_id))
    conn.commit()

# Function to manually perform renewals
def perform_manual_renewal():
    display_documents()
    try:
        doc_id = int(input("Enter the ID of the document you want to renew: "))
        renewal_days = int(input("Enter the number of days to renew the document for: "))
        
        # Fetch document details
        c.execute('SELECT * FROM documents WHERE id = ?', (doc_id,))
        document = c.fetchone()

        if document:
            doc_name = document[1]
            current_expiry = datetime.strptime(document[2], '%Y-%m-%d').date()
            new_expiry = current_expiry + timedelta(days=renewal_days)
            
            # Renew the document
            renew_document(doc_id, new_expiry.isoformat())
            print(f"Document '{doc_name}' with ID {doc_id} has been renewed until {new_expiry}.")
        else:
            print(f"Document with ID {doc_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid document ID and number of days.")

# Example of adding documents for testing (comment out after initial testing)
add_document('Document 1', '2024-07-01')
add_document('Document 2', '2023-12-31')
add_document('Document 3', (datetime.now() + timedelta(days=10)).date().isoformat())  # expires in 10 days
add_document('Document 4', (datetime.now() + timedelta(days=5)).date().isoformat())  # expires in 5 days

# Example of manually renewing a document
perform_manual_renewal()

# Close the connection
conn.close()