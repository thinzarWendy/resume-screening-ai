def format_keywords(matched_keywords):
    if matched_keywords:
        return ", ".join(matched_keywords)
    return "No matched keywords found."


def format_match_score(score):
    if score is None:
        return "N/A"
    return f"{score}%"