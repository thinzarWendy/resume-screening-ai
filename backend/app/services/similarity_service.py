from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity_score(resume_embedding, job_embedding) -> float:
    score = cosine_similarity([resume_embedding], [job_embedding])[0][0]
    return float(score)


def convert_score_to_percentage(score: float) -> float:
    return round(score * 100, 2)