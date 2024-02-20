# Import necessary libraries
import gradio as gr
import skops.io as sio

# Loading the scikit-learn pipeline and the model.
pipe = sio.load("./Model/drug_pipeline.skops", trusted=True)

# Define the function to predict drugs based on patient features.
def predict_drug(age, sex, blood_pressure, cholesterol, na_to_k_ratio):
    """Predict drugs based on patient features.

    Args:
        age (int): Age of patient
        sex (str): Sex of patient
        blood_pressure (str): Blood pressure level
        cholesterol (str): Cholesterol level
        na_to_k_ratio (float): Ratio of sodium to potassium in blood

    Returns:
        str: Predicted drug label
    """
    features = [age, sex, blood_pressure, cholesterol, na_to_k_ratio]
    predicted_drug = pipe.predict([features])[0]

    label = f"Predicted Drug: {predicted_drug}"
    return label

# Define input UI components using Gradio sliders and radios
inputs = [
    gr.Slider(15, 74, step=1, label="Age"),
    gr.Radio(["M", "F"], label="Sex"),
    gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure"),
    gr.Radio(["HIGH", "NORMAL"], label="Cholesterol"),
    gr.Slider(6.2, 38.2, step=0.1, label="Na_to_K"),
]

# Define output UI components
outputs = [gr.Label(num_top_classes=5)]

# Create sample inputs for easy testing of the model.
examples = [
    [30, "M", "HIGH", "NORMAL", 15.4],
    [35, "F", "LOW", "NORMAL", 8],
    [50, "M", "HIGH", "HIGH", 34],
]

# Define metadata for the Gradio Interface
title = "Drug Classification"
description = "Enter the details to correctly identify Drug type?"
article = "Thanks to [The guide to CI/CD for Machine Learning documentation](https://www.datacamp.com/portfolio/kingabzpro)" 

# Create and launch the Gradio Interface with specified settings
gr.Interface(
    fn=predict_drug,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme=gr.themes.Soft(),
).launch()
