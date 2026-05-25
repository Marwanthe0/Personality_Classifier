# Deployment Guide

## Overview

This guide covers deploying the Personality Classifier to various platforms.

## Local Deployment

### 1. Development Environment

```bash
# Clone repository
git clone https://github.com/Marwanthe0/Personality_Classifier.git
cd Personality_Classifier

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Train model (if needed)
python src/model.py

# Run Gradio interface
python src/app.py
```

Access at: `http://localhost:7860`

### 2. Production Environment (Local)

Using Gunicorn + Uvicorn:

```bash
pip install gunicorn

gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.api:app --bind 0.0.0.0:8000
```

Access at: `http://localhost:8000`

---

## Cloud Deployment

### Hugging Face Spaces (Recommended)

**Current Deployment:** https://huggingface.co/spaces/marwanthe0/Personality_Classifier

#### Steps:

1. **Create Space:**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose Gradio as the Space type
   - Add Space name and license

2. **Upload Files:**
   - Push to Hugging Face via git:
   ```bash
   git clone https://huggingface.co/spaces/marwanthe0/Personality_Classifier
   cd Personality_Classifier
   git add .
   git commit -m "Deploy Personality Classifier"
   git push
   ```

3. **Configure `app.py`:**
   ```python
   import gradio as gr
   # ... (your app code)
   
   app.launch(server_name="0.0.0.0", server_port=7860)
   ```

4. **Add Requirements:**
   - Ensure `requirements.txt` is in root directory
   - Hugging Face will automatically install dependencies

**Advantages:**
- Free tier available
- Simple git-based deployment
- Automatic scaling
- No credit card required for basic usage

---

### Docker Deployment

#### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 7860 8000

# Default command
CMD ["python", "src/app.py"]
```

#### Build and Run:

```bash
# Build image
docker build -t personality-classifier:latest .

# Run container
docker run -p 7860:7860 -p 8000:8000 personality-classifier:latest

# Run with volume mount (for model updates)
docker run -p 7860:7860 -v $(pwd)/models:/app/models personality-classifier:latest
```

#### Docker Compose

```yaml
version: '3.8'

services:
  personality-classifier:
    build: .
    ports:
      - "7860:7860"
      - "8000:8000"
    volumes:
      - ./models:/app/models
      - ./data:/app/data
    environment:
      - GRADIO_SHARE=False
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
```

---

### AWS EC2

1. **Launch Instance:**
   - AMI: Ubuntu 22.04 LTS
   - Instance Type: t3.medium (or larger)
   - Security Group: Allow ports 7860, 8000, 22

2. **SSH into Instance:**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Setup:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pip python3-venv git

   git clone https://github.com/Marwanthe0/Personality_Classifier.git
   cd Personality_Classifier

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python src/model.py
   ```

4. **Run with systemd:**
   ```bash
   sudo nano /etc/systemd/system/personality-classifier.service
   ```

   ```ini
   [Unit]
   Description=Personality Classifier API
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Personality_Classifier
   ExecStart=/home/ubuntu/Personality_Classifier/venv/bin/python src/app.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable personality-classifier
   sudo systemctl start personality-classifier
   ```

5. **Access:**
   - `http://your-instance-ip:7860` (Gradio)
   - `http://your-instance-ip:8000` (API)

---

### Heroku

1. **Create App:**
   ```bash
   heroku login
   heroku create personality-classifier
   ```

2. **Add Procfile:**
   ```
   web: python src/app.py
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

4. **View Logs:**
   ```bash
   heroku logs --tail
   ```

---

### Google Cloud Run

1. **Install Cloud SDK:**
   ```bash
   curl https://sdk.cloud.google.com | bash
   gcloud init
   ```

2. **Build and Push:**
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT-ID/personality-classifier
   ```

3. **Deploy:**
   ```bash
   gcloud run deploy personality-classifier \
     --image gcr.io/PROJECT-ID/personality-classifier \
     --platform managed \
     --region us-central1 \
     --port 7860
   ```

---

### DigitalOcean App Platform

1. **Connect Repository:**
   - Link GitHub repository to DigitalOcean

2. **Create App:**
   - Select Python as runtime
   - Auto-detect requirements.txt

3. **Configure:**
   ```yaml
   name: personality-classifier
   services:
   - name: api
     github:
       repo: marwanthe0/Personality_Classifier
       branch: main
     build_command: pip install -r requirements.txt
     run_command: python src/app.py
     http_port: 7860
   ```

---

## Environment Variables

Create `.env` file for configuration:

```env
# Model Configuration
MODEL_PATH=models/RF_Model.pkl
DATA_PATH=data/personality_dataset.csv

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Security
CORS_ORIGINS=*
RATE_LIMIT=100

# Feature Flags
ENABLE_API=True
ENABLE_GRADIO=True
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH", "models/RF_Model.pkl")
```

---

## Model Versioning

### Version Management

```python
# model_config.py
MODEL_VERSION = "1.0.0"
MODEL_TRAINED_DATE = "2026-05-25"
MODEL_ACCURACY = 0.9293

# In app.py
from model_config import MODEL_VERSION

@app.get("/model-info")
def get_model_info():
    return {"version": MODEL_VERSION, "accuracy": MODEL_ACCURACY}
```

### Model Registry

Store model versions:
```
models/
├── RF_Model_v1.0.0.pkl  (Current)
├── RF_Model_v0.9.0.pkl  (Previous)
└── model_registry.json
```

---

## Monitoring & Logging

### Application Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

### Performance Monitoring

Track API metrics:
```python
from time import time
from functools import wraps

def log_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        duration = time() - start
        logger.info(f"{func.__name__} took {duration:.3f}s")
        return result
    return wrapper
```

---

## Security Considerations

### 1. Environment Variables
- Never commit secrets
- Use `.env` files (add to `.gitignore`)
- Use secure secret management in production

### 2. Input Validation
- Validate all API inputs
- Sanitize data before processing
- Implement rate limiting

### 3. HTTPS/TLS
```bash
# Let's Encrypt with Certbot
sudo certbot certonly --standalone -d your-domain.com
```

### 4. API Authentication
```python
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/predict")
async def predict(data: PredictionInput, credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    # Validate token
    return prediction_result
```

---

## Scaling Strategies

### Horizontal Scaling
- Deploy multiple instances behind load balancer
- Use Kubernetes for orchestration

### Vertical Scaling
- Increase instance size/resources
- Optimize model for smaller memory footprint

### Caching
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_predict(features_hash):
    return prediction
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Model not found | Check MODEL_PATH in config |
| Out of memory | Use smaller batch size or reduce max_depth |
| Slow inference | Profile code, consider model quantization |
| API crashes | Check logs, verify input validation |

### Debug Mode

```bash
# Run with verbose logging
python src/app.py --debug

# Or in code
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## Maintenance

### Regular Tasks
- Monitor performance metrics
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Retrain model periodically
- Backup model artifacts

### Backup Strategy
```bash
# Backup models
tar -czf models_backup_$(date +%Y%m%d).tar.gz models/

# Backup data
tar -czf data_backup_$(date +%Y%m%d).tar.gz data/
```

---

For more information, see [README.md](../README.md) and [ARCHITECTURE.md](./ARCHITECTURE.md).
