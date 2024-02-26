# loan_application.py
import streamlit as st

def main():
    st.title('Vehicle Loan Application')

    # Get user inputs
    portfolio_link = st.text_input('Portfolio Link * ')
    gender = st.selectbox('Gender *', ['Male', 'Female', 'Other'])
    age = st.number_input('Age *', min_value=18, max_value=100, value=18)
    marital_status = st.selectbox('Marital Status *', ['Single', 'Married', 'Divorced'])
    dwelling_type = st.selectbox('Dwelling Type', ['House', 'Apartment', 'Other'])
    employment_status = st.selectbox('Employment Status', ['Employed', 'Unemployed'])
    education_level = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    car_ownership = st.selectbox('Car Ownership', ['Own', 'Lease', 'None'])
    property_ownership = st.selectbox('Property Ownership', ['Own', 'Rent', 'Other'])
    equities = st.number_input('Equities', min_value=0.0, value=0.0)
    bonds = st.number_input('Bonds', min_value=0.0, value=0.0)
    derivatives = st.number_input('Derivatives', min_value=0.0, value=0.0)
    funds = st.number_input('Funds', min_value=0.0, value=0.0)
    physical_assets = st.number_input('Physical Assets', min_value=0.0, value=0.0)

    # Check if gender, age, and marital status are provided
    if not portfolio_link:
        st.warning('Please provide valid portfoilio link subjected to SEBI.')
        st.stop()  # Stop execution if any of these fields are not provided

    # Add predict button
    if st.button('Predict'):
        eligible = check_eligibility(age, employment_status, equities, bonds, derivatives, funds, physical_assets)

        if eligible:
            st.success('Congratulations! You are eligible for a vehicle loan.')
        else:
            st.error('Sorry, you are not eligible for a vehicle loan based on the provided information.')

def check_eligibility(age, employment_status, equities, bonds, derivatives, funds, physical_assets):
    # Simple eligibility check (you can modify this based on your criteria)
    if age >= 18 and employment_status == 'Employed':
        total_investment = equities + bonds + derivatives + funds + physical_assets
        if total_investment >= 10000:  # Example threshold
            return True
    return False

if __name__ == '__main__':
    main()
