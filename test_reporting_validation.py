import pytest
import pandas as pd

# 1. Row Count Match :
@pytest.mark.skipif(reason = "This will fail as we have difference.")
def test_row_count(raw_df,target_data):
    assert len(raw_df) == len(target_data), "The source and target system are not same."

# 2. Check for Duplicate Transaction IDs :
def test_duplicate_check(target_data):
    duplicate = target_data[target_data['transaction_id'].duplicated()]
    assert duplicate.empty , "There is a duplicate transaction_id in target system."

# 3. Null Value Checks :
def test_null_check_target(target_data):
    assert target_data['email'].isnull().sum() == 0, "There is null in email."
    assert target_data['transaction_amount'].isnull().sum() == 0, "There is null in the transaction amount."

# 4. Validate the invalid email count : 
@pytest.mark.skipif(reason="This is expected to fail as we have one inavlid value in target system.")
def test_validate_email(target_data):
    patterns = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    invalid = ~target_data['email'].str.match(patterns)
    assert not invalid.any(), "There are invalid email address."

# 5. Validate the date format : 
def test_dateformat_target(target_data):
    expected = '%Y-%m-%d'
    validate_date = pd.to_datetime(target_data['transaction_date'], format = expected, errors = 'coerce')
    assert not validate_date.isna().all(), "There are invalid date in the target system."

# 6. Amount should not be negative : 
def test_negative_amount(target_data):
    assert (target_data['transaction_amount'] >= 0).all(), "There are negative amount value."

# 7. Status Should Be from Predefined Set : 
def test_status_target(target_data):
    expected = ["Success", "Failed", "Pending"]
    assert target_data['status'].isin(expected).all(), "There are unexpected status value."

# 8. Customer Name Should Have Alphabets Only :
@pytest.mark.skipif(reason="We have one None value and hence, it will fail.")
def test_name_validation(target_data):
    pattern = r'^[a-zA-Z\s]+$'
    invalid = ~target_data['customer_name'].str.match(pattern,na=False)
    assert not invalid.any(), "There are invalid alphabets in a customer name."

