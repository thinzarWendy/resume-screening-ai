def extract_matched_keywords(resume_text: str, job_description: str):
    resume_text_lower = resume_text.lower()
    job_description_lower = job_description.lower()

    # Simple keyword list from job description
    raw_keywords = job_description_lower.replace(",", " ").replace(".", " ").split()
    unique_keywords = list(dict.fromkeys(raw_keywords))

    matched_keywords = [
        keyword for keyword in unique_keywords
        if keyword in resume_text_lower and len(keyword) > 2
    ]

    return matched_keywords