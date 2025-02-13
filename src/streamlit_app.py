# app.py
import streamlit as st
import requests
import json
import pandas as pd
from typing import List

class ModelInterface:
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url
        
    def predict(self, input_data: List[int]) -> dict:
        try:
            response = requests.post(
                f"{self.api_url}/predict",
                json={"input_data": input_data}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error making prediction: {str(e)}")
            return None

def main():
    st.set_page_config(
        page_title="Model Prediction Interface",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("Model Prediction Interface")
    
    # Initialize model interface
    model = ModelInterface()
    
    # Input method selection
    input_method = st.radio(
        "Choose input method:",
        ["Manual Input", "CSV Upload"]
    )
    
    if input_method == "Manual Input":
        st.subheader("Enter Input Values")
        
        # Dynamic input fields
        num_inputs = st.number_input("Number of input values", min_value=1, max_value=10, value=3)
        input_values = []
        
        for i in range(num_inputs):
            value = st.number_input(f"Input {i+1}", value=0)
            input_values.append(value)
        
        if st.button("Make Prediction"):
            if input_values:
                result = model.predict(input_values)
                if result:
                    st.success("Prediction made successfully!")
                    st.json(result)
            else:
                st.warning("Please enter input values")
    
    else:  # CSV Upload
        st.subheader("Upload CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Preview of uploaded data:")
                st.dataframe(df.head())
                
                if st.button("Make Predictions"):
                    results = []
                    for _, row in df.iterrows():
                        input_data = row.tolist()
                        prediction = model.predict(input_data)
                        if prediction:
                            results.append(prediction)
                    
                    if results:
                        st.success("Predictions completed!")
                        results_df = pd.DataFrame(results)
                        st.dataframe(results_df)
                        
                        # Download button for results
                        csv = results_df.to_csv(index=False)
                        st.download_button(
                            label="Download Predictions",
                            data=csv,
                            file_name="predictions.csv",
                            mime="text/csv"
                        )
            
            except Exception as e:
                st.error(f"Error processing CSV file: {str(e)}")

if __name__ == "__main__":
    main()