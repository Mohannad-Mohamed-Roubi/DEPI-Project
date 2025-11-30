# DEPI-Project
Skin Disease Detection & Diabetes Risk Assessment System

A Dual-Function AI Medical Pre-Screening Platform

This project delivers an intelligent medical pre-screening system that combines deep learning–based skin disease classification with machine-learning–based diabetes risk prediction. Designed as a fast, accessible, and interpretable triage tool, it assists clinicians and empowers users by providing preliminary assessments—not medical diagnoses—within seconds.

Project Overview:

The system integrates two core AI pipelines:

1) Skin Disease Classification (Deep Learning)

Transfer-learning CNN model (ResNet-50 backbone)

Classifies uploaded skin lesion images into predefined dermatological categories

Provides confidence scores and top-K alternative predictions

2) Diabetes Risk Prediction (Machine Learning)

Interpretable Logistic Regression model trained on 100,000 clinical records

Uses nine demographic and clinical features (e.g., BMI, HbA1c, glucose)

Outputs probability of diabetes along with risk level interpretation

A unified frontend interface allows users to either upload images or enter clinical data, instantly receiving structured, easy-to-understand feedback.

- Goals & Key Achievements:

≥ 90% accuracy on skin disease validation set

≥ 0.85 ROC-AUC for diabetes risk prediction

End-to-end latency ≤ 5 seconds for all predictions

Secure architecture with encryption, RBAC, and safe data handling

- Technical Highlights:
  
Machine Learning Pipeline

Data cleaning, preprocessing, and SMOTE/class-weight handling

StandardScaler, one-hot encoding, and feature engineering

Stratified cross-validation and model interpretability (SHAP, coefficients)

-Deep Learning Pipeline:

Image preprocessing (224×224), augmentation, fine-tuned ResNet-50

Metrics: accuracy, precision, recall, F1, confusion matrix

Grad-CAM and probability calibration for real-world reliability

-Frontend (Streamlit):

Unified dashboard with two modules

Image uploader + clinical form validation

Color-coded results, confidence bars, and processing indicators

Prominent medical disclaimer for safe user expectations

- Backend & Infrastructure:

REST API for inference and authentication (Flask/FastAPI)

PostgreSQL database + object storage for images

Dockerized services with optional Kubernetes scaling

Monitoring for latency, drift, and system health

- Ethics, Privacy & Compliance:

End-to-end encryption and anonymized storage

User consent required for processing

Follows GDPR-aligned privacy principles

Clearly labeled as a pre-screening tool, not a diagnostic device

- Future Improvements:

Mobile app for on-the-go assessments

Expansion to more skin disease classes

Active learning based on clinician feedback

EHR integration and multi-disease prediction modules
