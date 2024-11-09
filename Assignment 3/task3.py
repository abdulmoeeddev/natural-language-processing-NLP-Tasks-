import re
import json

def extract_medical_info(text):
    # Define regular expressions for extracting relevant information
    name_pattern = r'Patient Name: ([A-Za-z ]+)'
    disease_pattern = r'Diagnosis: ([A-Za-z ]+)'
    age_pattern = r'Age: (\d+)'
    gender_pattern = r'Gender: ([A-Za-z]+)'
    
    # Extract information using regular expressions
    name = re.search(name_pattern, text).group(1) if re.search(name_pattern, text) else None
    disease = re.search(disease_pattern, text).group(1) if re.search(disease_pattern, text) else None
    age = re.search(age_pattern, text).group(1) if re.search(age_pattern, text) else None
    gender = re.search(gender_pattern, text).group(1) if re.search(gender_pattern, text) else None
    
    # Store the extracted information in a dictionary
    medical_info = {
        "Patient Name": name,
        "Diagnosis": disease,
        "Age": age,
        "Gender": gender
    }
    
    return medical_info

# Test the function
text = "Patient Name: John Doe. Diagnosis: Diabetes. Age: 45. Gender: Male."
extracted_info = extract_medical_info(text)
print(json.dumps(extracted_info, indent=4))