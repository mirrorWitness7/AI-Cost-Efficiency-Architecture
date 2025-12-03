def log_openai_completion(response, session_id):
    tokens = response["usage"]["total_tokens"]
    turns = 1
    return {"tokens": tokens, "turns": turns}
