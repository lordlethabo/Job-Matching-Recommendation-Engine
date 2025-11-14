import numpy as np

# TEMP: local sample data until we connect OpenSearch
SAMPLE_JOBS = [
    {"title": "Junior Cloud Engineer", "company": "AWS Partner", "embedding": np.random.rand(1536)},
    {"title": "AI Support Engineer", "company": "Tech Startup", "embedding": np.random.rand(1536)},
    {"title": "Cloud Support Associate", "company": "Global Cloud Co", "embedding": np.random.rand(1536)},
]

def cosine_sim(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def search_jobs(candidate_vector):
    results = []
    for job in SAMPLE_JOBS:
        sim = cosine_sim(candidate_vector, job["embedding"])
        results.append({
            "title": job["title"],
            "company": job["company"],
            "score": round(sim, 4),
            "skills": "N/A"
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)
