# Resume Screening AI Backend

This is the FastAPI backend for the Resume Screening AI project.

## Features

- Load job descriptions from JSON
- Upload resume files in PDF or DOCX format
- Extract text from resumes
- Clean extracted text
- Generate embeddings using Sentence Transformers
- Compute similarity score between resume and job description
- Extract matched keywords
- Return match results through API endpoints

## Project Structure

```resume-screening-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes_jobs.py
│   │   │   └── routes_match.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── parser_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── similarity_service.py
│   │   │   ├── keyword_service.py
│   │   │   └── job_service.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── file_handler.py
│   │   │   ├── text_cleaner.py
│   │   │   └── validators.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── request_models.py
│   │   │   └── response_models.py
│   │   │
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── sample_jobs.json
│   │   └── sample_resumes/
│   │
│   ├── uploads/
│   │   └── resumes/
│   │
│   ├── requirements.txt
│    
│ 
│
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── file_uploader.py
│   │   │   ├── job_selector.py
│   │   │   ├── score_card.py
│   │   │   └── keyword_tags.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── api_client.py
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── constants.py
│   │   │   └── formatter.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│
│
├── .gitignore
├── README.md

```

## Requirements

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Backend

From the `backend/` folder:

```bash
python -m uvicorn app.main:app --reload
```

## API Endpoints

### Root
- `GET /`

### Health Check
- `GET /health`

### Jobs
- `GET /jobs/`

### Match Resume
- `POST /match/`

## API Docs

After starting the server, open:

- `http://127.0.0.1:8000/docs`

## Supported Resume Formats

- PDF
- DOCX

## Embedding Model

- `all-MiniLM-L6-v2`

## Notes

- Uploaded resumes are saved in `uploads/resumes/`
- Job descriptions are loaded from `data/sample_jobs.json`

