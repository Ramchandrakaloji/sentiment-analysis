from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from backend.firebase import save_to_firebase

app = FastAPI()

# Load pre-trained model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class ReviewRequest(BaseModel):
    review: str

@app.post("/classify")
async def classify_review(data: ReviewRequest):
    result = sentiment_pipeline(data.review)[0]
    sentiment, confidence = result['label'], result['score']

    # Save result to Firebase
    save_to_firebase(data.review, sentiment, confidence)

    return {"review": data.review, "sentiment": sentiment, "confidence": confidence}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
