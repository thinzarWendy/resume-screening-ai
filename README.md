# Resume Screening AI

Resume Screening AI is a simple AI-based system that matches resumes with job descriptions. Users can upload a resume in PDF or DOCX format, select a job role, and get a match score with matched keywords.

## Features

- Upload PDF or DOCX resumes
- Extract text from resumes
- Load job descriptions from JSON
- Match resume and job description using semantic similarity
- Show match score and matched keywords
- Streamlit frontend and FastAPI backend
- Optional fine-tuning support

## Tech Stack

- Python
- FastAPI
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyMuPDF
- python-docx

## Project Structure

```text
resume-screening-ai/
├── backend/
├── frontend/
└── README.md
```

## Run the Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Backend URL:
`http://127.0.0.1:8000`

API Docs:
`http://127.0.0.1:8000/docs`

## Run the Frontend

```bash
cd frontend
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app/main.py
```

Frontend URL:
`http://localhost:8501`

## API Endpoints

- `GET /` → backend running check
- `GET /health` → health check
- `GET /jobs/` → load job descriptions
- `POST /match/` → upload resume and get match result

## Fine-Tuning

Training data file:
`backend/data/labeled_pairs.csv`

Train:
```bash
cd backend
python -m app.ml.train_model
```

Evaluate:
```bash
python -m app.ml.evaluate_model
```

Compare models:
```bash
python -m app.ml.compare_models
```

## Limitations

- Basic keyword extraction
- Small fine-tuning dataset
- Limited job descriptions
- English only
- No authentication
- No database yet

## Author

Wendy
