def generate_text_preview(text: str, max_length: int = 500) -> str:
    if not text:
        return ""

    if len(text) <= max_length:
        return text

    return text[:max_length]