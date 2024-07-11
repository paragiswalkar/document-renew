# Document Expiration Management System
## Description

This project manages document expiration dates using SQLite for data storage. It allows users to add documents, display existing documents with their expiration dates, and manually renew document expirations.

## Features

- **SQLite Database**: Stores document details including ID, name, and expiration date.
- **Add Document**: Allows users to add new documents to the database with a specified expiration date.
- **Display Documents**: Retrieves and displays all stored documents with their IDs and expiration dates.
- **Renew Document**: Updates the expiration date of a selected document based on user input.
- **Manual Renewal**: Provides a user interface to manually select a document ID and specify the number of days to extend its expiration.
- **Example Usage**: Includes example usage scenarios for adding documents and manually renewing them.

## Installation and Setup

### Requirements

- Python (version X.X)
- SQLite3 (version X.X) installed on your system

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   cd repository

### Creating a Virtual Environment
```bash
python -m venv myvenv
```
Using a virtual environment (myvenv) is recommended to keep your project dependencies isolated. Follow these steps to create and activate a myvenv for this project:

On Windows
Open a command prompt and navigate to your project directory:
```bash
myvenv\Scripts\activate
```
After running the script

```bash
py document_expiration.py
```
