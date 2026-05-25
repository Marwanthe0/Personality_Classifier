# API Documentation

## Overview

This document describes the API endpoints available for the Personality Classifier service.

## Base URL

```
http://localhost:8000
```

## Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Check if the API service is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

**Status Code:** `200 OK`

---

### 2. Single Prediction

**Endpoint:** `POST /predict`

**Description:** Predict personality type for a single person based on their input features.

**Request Body:**
```json
{
  "time_spent_alone": 4.0,
  "stage_fear": "No",
  "social_event_attendance": 4.0,
  "going_outside": 6.0,
  "drained_after_socializing": "No",
  "friends_circle_size": 13.0,
  "post_frequency": 5.0
}
```

**Response:**
```json
{
  "personality": "Extrovert",
  "confidence": 0.95
}
```

**Status Code:** `200 OK`

**Error Response:**
```json
{
  "detail": "Invalid input: time_spent_alone must be between 0 and 11"
}
```

**Status Code:** `422 Unprocessable Entity`

---

### 3. Batch Prediction

**Endpoint:** `POST /predict_batch`

**Description:** Predict personality type for multiple people in a single request.

**Request Body:**
```json
{
  "samples": [
    {
      "time_spent_alone": 4.0,
      "stage_fear": "No",
      "social_event_attendance": 4.0,
      "going_outside": 6.0,
      "drained_after_socializing": "No",
      "friends_circle_size": 13.0,
      "post_frequency": 5.0
    },
    {
      "time_spent_alone": 9.0,
      "stage_fear": "Yes",
      "social_event_attendance": 1.0,
      "going_outside": 2.0,
      "drained_after_socializing": "Yes",
      "friends_circle_size": 5.0,
      "post_frequency": 2.0
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "personality": "Extrovert",
      "confidence": 0.95
    },
    {
      "personality": "Introvert",
      "confidence": 0.92
    }
  ]
}
```

**Status Code:** `200 OK`

---

### 4. Model Information

**Endpoint:** `GET /model-info`

**Description:** Get information about the trained model.

**Response:**
```json
{
  "model_type": "Random Forest Classifier",
  "framework": "scikit-learn",
  "n_estimators": 150,
  "max_depth": 20,
  "training_samples": 1000,
  "features": [
    "Time_spent_Alone",
    "Stage_fear",
    "Social_event_attendance",
    "Going_outside",
    "Drained_after_socializing",
    "Friends_circle_size",
    "Post_frequency"
  ],
  "target_classes": ["Introvert", "Extrovert"],
  "last_updated": "2026-05-25T12:00:00Z"
}
```

**Status Code:** `200 OK`

---

## Request/Response Examples

### cURL Example

```bash
# Single Prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "time_spent_alone": 4.0,
    "stage_fear": "No",
    "social_event_attendance": 4.0,
    "going_outside": 6.0,
    "drained_after_socializing": "No",
    "friends_circle_size": 13.0,
    "post_frequency": 5.0
  }'
```

### Python Example

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "time_spent_alone": 4.0,
    "stage_fear": "No",
    "social_event_attendance": 4.0,
    "going_outside": 6.0,
    "drained_after_socializing": "No",
    "friends_circle_size": 13.0,
    "post_frequency": 5.0
}

response = requests.post(url, json=data)
print(response.json())
# Output: {"personality": "Extrovert", "confidence": 0.95}
```

### JavaScript Example

```javascript
const data = {
  time_spent_alone: 4.0,
  stage_fear: "No",
  social_event_attendance: 4.0,
  going_outside: 6.0,
  drained_after_socializing: "No",
  friends_circle_size: 13.0,
  post_frequency: 5.0
};

fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Input Validation Rules

### Numeric Fields
- **time_spent_alone**: 0-11 (hours per day)
- **social_event_attendance**: 0-10 (rating scale)
- **going_outside**: 0-7 (days per week)
- **friends_circle_size**: ≥ 0 (integer)
- **post_frequency**: ≥ 0 (posts per week)

### Categorical Fields
- **stage_fear**: "Yes" or "No"
- **drained_after_socializing**: "Yes" or "No"

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid JSON format"
}
```

### 422 Unprocessable Entity
```json
{
  "detail": "Invalid input: stage_fear must be 'Yes' or 'No'"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Model inference failed. Please try again later."
}
```

---

## Authentication

Currently, the API does not require authentication. For production deployments, implement:
- API Key authentication
- OAuth 2.0
- JWT tokens

---

## Rate Limiting

Not currently implemented. For production, recommended limits:
- 100 requests per minute per IP
- 10,000 requests per day per API key

---

## CORS Configuration

Enable CORS for web clients:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Deployment

### Local Development
```bash
python -m uvicorn src.api:app --reload
```

### Production
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.api:app
```

### Docker
```bash
docker build -t personality-classifier .
docker run -p 8000:8000 personality-classifier
```

---

## Performance

| Metric | Value |
|--------|-------|
| Average Response Time | <100ms |
| Memory Usage | ~500MB |
| Throughput | ~100 req/s |
| Model Load Time | ~2s |

---

For more information, see [README.md](../README.md) and [ARCHITECTURE.md](./ARCHITECTURE.md).
