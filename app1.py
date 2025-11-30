import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ================== إعداد الصفحة ==================
st.set_page_config(
    page_title="Smart Health AI - Disease Prediction",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================== تحميل النماذج ==================
def load_models():
    try:
        diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
        return diabetes_model
    except Exception as e:
        st.error(f"❌ Error loading models: {e}")
        return None, None, None


# ================== تصميم الواجهة ==================
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            color: #1e293b;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #2563eb;
            color: white;
            border-radius: 10px;
            height: 3em;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1e40af;
            transform: scale(1.05);
        }
        .success-box {
            background-color: #dcfce7;
            border: 1px solid #22c55e;
            padding: 10px;
            border-radius: 10px;
            color: black;
        }
        .error-box {
            background-color: #fee2e2;
            border: 1px solid #ef4444;
            padding: 10px;
            border-radius: 10px;
            color: black;            
        }
    </style>
""", unsafe_allow_html=True)


# ================== واجهة القائمة الجانبية ==================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966484.png", width=100)
    st.title("🩺 Smart Health AI")
    selected = option_menu(
        menu_title="Main Menu",
        options=["Diabetes Prediction"],
        icons=["activity", "heart", "person"],
        menu_icon="cast",
        default_index=0,
    )

# ================== دوال الإدخال ==================
def get_diabetes_input():
    col1, col2, col3 = st.columns(3)
    Pregnancies = col1.number_input('Pregnancies', 0)
    Glucose = col2.number_input('Glucose Level', 0.0)
    BloodPressure = col3.number_input('Blood Pressure', 0.0)
    SkinThickness = col1.number_input('Skin Thickness', 0.0)
    Insulin = col2.number_input('Insulin Level', 0.0)
    BMI = col3.number_input('BMI', 0.0)
    DiabetesPedigreeFunction = col1.number_input('Diabetes Pedigree Function', 0.0)
    Age = col2.number_input('Age', 0)
    return [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]


# ================== دالة التنبؤ ==================
def make_prediction(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]


# ================== التطبيق الرئيسي ==================
def main():
    diabetes_model = load_models()
    if not all([diabetes_model]):
        st.stop()

    if selected == "Diabetes Prediction":
        st.header("🩸 Diabetes Prediction")
        st.markdown("Enter the patient's health data to predict the likelihood of diabetes.")
        input_data = get_diabetes_input()
        if st.button("🔍 Predict Diabetes"):
            result = make_prediction(diabetes_model, input_data)
            if result == 1:
                st.markdown('<div class="error-box">⚠️ The person is diabetic.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ The person is not diabetic.</div>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()
