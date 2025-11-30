import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
def load_models():
    try:
        diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
        return diabetes_model
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None

# Function to get user input for diabetes prediction
def get_diabetes_input():
    col1, col2, col3 = st.columns(3)
    try:
        with col1:
            Pregnancies = int(st.text_input('Number of Pregnancies', '0'))
        with col2:
            Glucose = float(st.text_input('Glucose Level', '0'))
        with col3:
            BloodPressure = float(st.text_input('Blood Pressure value', '0'))
        with col1:
            SkinThickness = float(st.text_input('Skin Thickness value', '0'))
        with col2:
            Insulin = float(st.text_input('Insulin Level', '0'))
        with col3:
            BMI = float(st.text_input('BMI value', '0'))
        with col1:
            DiabetesPedigreeFunction = float(st.text_input('Diabetes Pedigree Function value', '0'))
        with col2:
            Age = int(st.text_input('Age of the Person', '0'))
        return Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
    except ValueError:
        st.error("Please enter valid numbers for all fields.")
        return None


# Prediction function
def make_prediction(model, input_data):
    try:
        prediction = model.predict([input_data])
        return prediction[0]
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

# Main function
def main():
    # Load models
    diabetes_model= load_models()
    if not diabetes_model :
        return
    
    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu('Disease Prediction System',
                               ['Diabetes Prediction'],
                               icons=['activity', 'heart', 'person'],
                               default_index=0)
    
    # Diabetes Prediction
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        input_data = get_diabetes_input()
        if input_data and st.button('Diabetes Test Result'):
            result = make_prediction(diabetes_model, input_data)
            if result == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')
    

if __name__ == '__main__':
    main()
