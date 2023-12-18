
import streamlit as st
from sklearn.preprocessing import LabelEncoder,StandardScaler
import pickle
model=pickle.load(open('bayes_model.pickle','rb'))
                  
st.title("Loan Solvability App")
gender=st.selectbox("Gender",["Male","Female","Other"])
married=st.selectbox("married",["Yes","Non","Other"])
dependents=st.selectbox("Dependents",["0","1","2","+3","other"])
education=st.selectbox("Education",["Graduate","Not graduate"])
self_employed=st.selectbox("Self_Employed",["No","Yes","Other"])

applicantIncome=st.text_input ("applicant Income",value=0.0)
CoapplicantIncome=st.text_input ("Coapplicant Income  ",value=0.0)
LoanAmount=st.text_input ("Loan Amount",value=0.0)
Loan_Amount_Term=st.text_input ("Loan Amount Term",value=0.0)
Credit_History=st.text_input ("Credit History",value=0.0)
Property_Area=st.selectbox("Property Area",["Urban","Rural","SemiUrban"])



features=[gender,married,dependents,education,self_employed,Property_Area,applicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History]
le=LabelEncoder()
scaler=StandardScaler()
features=le.fit_transform(features)
features=features.reshape(1,-1)

features=scaler.fit_transform(features)
pred=model.predict(features)
if st.button("Predict"):
    y=pred[0]
    if y==1:
        st.success("accorder")
    else:
        st.error("non accorder")
