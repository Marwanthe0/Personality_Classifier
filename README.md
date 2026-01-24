# Personality Test Project

A machine learning application that predicts whether a person is an Introvert or Extrovert based on their social behavior data.

## Features

- Predict personality type using a trained Random Forest model
- Interactive web interface built with Gradio
- Data preprocessing and model training pipeline

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Personality_Test_Project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Train the model (if not already trained):
   ```bash
   cd src
   python model.py
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open the provided URL in your browser to use the interface.

## Project Structure

```
Personality_Test_Project/
├── .gitignore
├── requirements.txt
├── README.md
└── src/
    ├── app.py              # Gradio web application
    ├── model.py            # Model training script
    └── personality_dataset.csv  # Training dataset
```

## Model Details

- Algorithm: Random Forest Classifier
- Features: Time spent alone, stage fear, social event attendance, etc.
- Target: Personality (Introvert/Extrovert)

## Contributing

Please follow standard Python coding practices and add tests for new features.

## License

[Add license information]</content>
<parameter name="filePath">c:\Users\marwa\Artificial_Intelligence\phitron\Machine Learning\Final Exam M30\Personality_Test_Project\README.md