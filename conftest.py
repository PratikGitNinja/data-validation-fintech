import pytest
import pandas as pd

# read the csv input data : 
@pytest.fixture(scope="session")
def raw_df():
    return pd.read_csv('raw_data.csv')

# Target Data (mocked for this test) : 
@pytest.fixture(scope="session")
def target_data():
    data =  [
        {"transaction_id": "TXN001", "customer_id": 101, "customer_name": "John Doe", "email": "john.doe@example.com", "transaction_amount": 100.50, "transaction_date": "2024-04-01", "status": "Success"},
        {"transaction_id": "TXN002", "customer_id": 102, "customer_name": "Jane Smith", "email": "jane.smith@example.com", "transaction_amount": 300.00, "transaction_date": "2024-04-02", "status": "Failed"},
        {"transaction_id": "TXN003", "customer_id": 103, "customer_name": None, "email": "noemail@", "transaction_amount": 150.00, "transaction_date": "2024-04-03", "status": "Success"},
        {"transaction_id": "TXN004", "customer_id": 104, "customer_name": "Sam Roy", "email": "sam.roy@example.com", "transaction_amount": 0.0, "transaction_date": "2024-04-05", "status": "Success"},
        {"transaction_id": "TXN005", "customer_id": 101, "customer_name": "John Doe", "email": "john.doe@example.com", "transaction_amount": 500.00, "transaction_date": "2024-04-07", "status": "Success"}
    ]
    return pd.DataFrame(data)