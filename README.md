# 📄 End-to-End CNN Classifier – Industrial-Grade Project

## 1. Executive Summary
This project implements an **industrial-grade Convolutional Neural Network (CNN) image classification system** designed for real-world deployment.  
It covers the complete ML lifecycle:
- **Data ingestion → preprocessing → training → evaluation → deployment → monitoring → maintenance**
- Built with **modularity, scalability, and production reliability** in mind
- Uses **CI/CD**, **Docker**, and **cloud deployment** on AWS

**Example Industrial Applications:**
- Defect detection in manufacturing
- Emergency vehicle identification for toll gate automation
- Product categorization in e-commerce
- Medical imaging anomaly detection

---

## 2. Business Problem Statement
Traditional manual classification is **slow, error-prone, and costly**.  
Our CNN classifier automates this process by:
- Reducing **human workload**
- Improving **accuracy and speed**
- Providing **real-time predictions** for decision-making

**Business Goals:**
- Achieve **>95% accuracy** on test data
- Serve predictions within **<200 ms latency**
- Ensure system uptime **>99%**

---

## 3. System Architecture

### 3.1 High-Level Flow
[Data Sources] → [Data Preprocessing & Augmentation] → [CNN Model Training]
→ [Model Evaluation & Optimization] → [FastAPI Deployment in Docker]
→ [AWS Cloud Deployment] → [Monitoring & Logging]


### 3.2 Architecture Diagram
    +------------------+           +------------------+
    | Raw Dataset      |           | Real-Time Input  |
    +--------+---------+           +--------+---------+
             |                              |
             v                              v
     +-------+--------+              +------+------+
     | Data Preproc. |-------------->| FastAPI API |
     +-------+--------+              +------+------+
             |                              |
             v                              v
    +--------+---------+          +--------+----------+
    | Model Training   |          | Predictions       |
    +--------+---------+          +-------------------+
             |
             v
    +--------+---------+
    | AWS ECR/EC2      |
    +------------------+

---

## 4. Dataset
- **Source:** Public dataset or custom-collected industrial images
- **Size:** Example: 50,000 images (train/test/val split: 70/15/15)
- **Classes:** Example: `Emergency`, `Non-Emergency`
- **Format:** JPG, PNG
- **Preprocessing:**
  - Image resizing: `224x224`
  - Normalization: `0-1` pixel scaling
  - Data augmentation: rotation, shift, zoom, flip

---

## 5. Data Pipeline
1. **Data Ingestion**
   - Load images from storage or API
   - Handle missing/corrupted files
2. **Data Cleaning**
   - Remove duplicates
   - Standardize formats
3. **Data Augmentation**
   - Random flips, rotations, brightness changes
4. **Dataset Splitting**
   - Train / validation / test sets

---

## 6. Model Development

### 6.1 CNN Architecture
Example architecture:
- **Conv2D(32 filters, 3x3, ReLU)**
- **MaxPooling2D(2x2)**
- **Conv2D(64 filters, 3x3, ReLU)**
- **MaxPooling2D(2x2)**
- **Conv2D(128 filters, 3x3, ReLU)**
- **Flatten**
- **Dense(128, ReLU)**
- **Dense(64, ReLU)**
- **Dense(1, Sigmoid)**

### 6.2 Training Strategy
- **Loss function:** Binary Crossentropy
- **Optimizer:** Adam
- **Learning rate scheduling**
- **Early stopping** to avoid overfitting
- **Checkpoints** to save best model

---

## 7. Model Evaluation
**Metrics Used:**
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

**Example Results:**
| Metric    | Train | Validation | Test |
|-----------|-------|------------|------|
| Accuracy  | 99%   | 96%        | 95%  |
| Precision | 98%   | 96%        | 95%  |
| Recall    | 99%   | 95%        | 94%  |

---

## 8. Deployment

### 8.1 Local Deployment
- **FastAPI** REST API for predictions
- Endpoint: `/predict`
- Accepts image uploads, returns classification result

### 8.2 Containerization
- **Dockerfile** for reproducible builds
- **Image pushed to AWS ECR**

### 8.3 Cloud Deployment (AWS EC2)
- Pull Docker image from ECR
- Run containerized API
- Nginx reverse proxy for load balancing
- HTTPS enabled

---

## 9. CI/CD Pipeline
- **GitHub Actions**:
  - On code push: run tests, build Docker image, push to ECR
  - Trigger EC2 instance to pull and restart container
- **Automated rollback** if deployment fails

---

## 10. Monitoring & Logging
- **AWS CloudWatch** for metrics (CPU, memory, latency)
- **Prometheus + Grafana** for API request tracking
- **Database logging** of predictions (timestamp, input, output, confidence)
- Alerts on:
  - API downtime
  - Accuracy drop >2%
  - High latency (>500 ms)

---

## 11. Scalability & Fault Tolerance
- Horizontal scaling with multiple EC2 instances
- Load balancing via AWS ALB
- Backup model storage in AWS S3
- Disaster recovery plan with regular snapshot backups

---

## 12. Security
- **JWT authentication** for API access
- **HTTPS** encryption
- Restricted IAM roles for AWS services

---

## 13. How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Mahadevkharmate/End-to-End-Industrial-Grade-DL-Project.git
cd cnn-classifier
```
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train.py --config config.yaml

# Start API
uvicorn deployment.app:app --reload

API docs: http://127.0.0.1:8000/docs

```bash
## Dataset Description
The training archive contains 25,000 images of dogs and cats. Train your algorithm on these files and predict the labels for test1.zip (1 = dog, 0 = cat).
Files -> 3 files
Size-> 853.96 MB
Type-> zip, csv
```