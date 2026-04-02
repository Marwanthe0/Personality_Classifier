# Personality Test Project

A machine learning application that predicts whether a person is an Introvert or Extrovert based on their social behavior data.
##Live Demo
Try it on Hugging Face:
https://huggingface.co/spaces/marwanthe0/Personality_Classifier
## Features

- Predict personality type using a trained Random Forest model
- Interactive web interface built with Gradio
- Data preprocessing and model training pipeline

## Requirements

- Python 3.8+
- See `requirements.txt` for exact dependency versions (Gradio, scikit-learn, pandas, etc.)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Marwanthe0/Personality_Test_Classifier.git
   cd Personality_Test_Classifier
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # Windows (cmd.exe)
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Train the model (if not already trained):
   ```bash
   # from project root
   python src/model.py
   ```
   - The script should save the trained model to a file (e.g., `models/model.pkl`). If it doesn't, check `src/model.py` and note the output path.

2. Run the application:
   ```bash
   python src/app.py
   ```
   - Gradio typically serves on http://localhost:7860 by default — check the console output for the exact URL.

3. Open the provided URL in your browser to use the interface.

## Example

- Provide a short example of inputs (or a screenshot) showing how to use the web UI or a sample CLI/API call. This helps users try the app quickly.

## Project Structure

```
Personality_Test_Classifier/
├── .gitignore
├── LICENSE
├── requirements.txt
├── README.md
└── src/
    ├── app.py                   # Gradio web application
    ├── model.py                 # Model training script
    └── personality_dataset.csv  # Training dataset (consider moving to data/)
    └── models/                  # recommended: store trained artifacts here (add to .gitignore)
```

Notes:
- Consider moving large datasets to a `data/` directory and adding `data/` or `models/` to `.gitignore` if they are not meant to be committed.
- If `src/model.py` writes a model file, include the path in the README.

## Model Details

- Algorithm: Random Forest Classifier
- Features: time spent alone, stage fear, social event attendance, etc.
- Target: Personality (Introvert / Extrovert)
- Evaluation: add accuracy / precision / recall numbers and how they were computed (cross-validation, test split, etc.)

## Contributing

Please follow standard Python coding practices:
- Open issues for bugs and feature requests
- Submit PRs with clear descriptions and tests for new features
- Use consistent formatting (e.g., Black / isort) and type hints where appropriate

## Testing

- Add a `tests/` folder and instructions on how to run tests (e.g., `pytest`).

## License

Licensed under the MIT License — see the top-level LICENSE file for details.

MIT License

Copyright (c) 2026 Marwanthe0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
