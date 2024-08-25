# installing the package
pip install pandas numpy scikit-learn matplotlib seaborn streamlit

# reading the data
"metaverse_transactions_dataset.csv" file need to be in the same directory as the files

# Run the Jupyter Notebook
run the cells in jupyter notebook - app.ipynb
This will process the data, train the model and save it in decision_tree_model.pkl

# Run the streamlit application
In the terminal run - streamlit run app.py

### Data Augmentation

1) payment_option: A new feature payment_option was created to classify the payment solution based on transaction amount, location region, and risk level. The rules used are:
    ACH for low-risk transactions under $400 in North America.
    SEPA for low-risk transactions under $800 in Europe.
    Western Union for low-risk transactions under $500 in Asia.
    International Wire for transactions over $500 in South America with moderate risk.
    Metaverse Wallet for high-risk transactions in Asia.
    Blockchain Transfer for other cases.
2) transaction_time: Added a transaction_time feature representing the estimated time taken for each payment option, simulated within specific ranges:
    ACH: 1-3 days (in minutes).
    SEPA: 1 hour to 1 day.
    Western Union: Minutes to 2 days.
    International Wire: 2-5 days.
    Metaverse Wallet: Instantly or within an hour.
    Blockchain Transfer: Minutes to 1 day.
3) Transaction_fee: Transaction_fee was added to represent the fee associated with each payment option. Fees were assigned as:
    ACH: $0.1 to $1.
    SEPA: $0.5 to $5.
    Western Union: $5 to $20.
    International Wire: $15 to $50.
    Metaverse Wallet: $0 to $2.
    Blockchain Transfer: $1 to $10.

4) Feature Encoding: 
    Categorical features like location_region and payment_option were converted to numeric codes to make them suitable for the Decision Tree model.
    
    Removing Unnecessary Columns: Columns that were not needed for the model, such as 'age_group', 'purchase_pattern', 'timestamp', 'hour_of_day', 'sending_address', 'receiving_address', 'transaction_type', 'ip_prefix', 'login_frequency', 'session_duration' were removed to simplify the dataset and improve model performance.

This augmentation enhances the dataset to provide meaningful features for predicting the optimal payment solution option based on transaction attributes.






