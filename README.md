# 📄 End-to-End CNN Classifier – Industrial-Grade Project

---
## Project Workflow
---
## Workflows to follow:->
1. update **`config.yaml`** file  → Project configs (paths, setup)
2. update **`secrets.yaml`** file [Optional-Credentials] → Credentials (optional, secure)
3. update **`params.yaml`** → Hyperparameters (tunable, trackable)
4. update **`entity/`** → Config schema (dataclasses)
5. update **`configuration.py`** in src/config/ → Config manager
6. update **`components/`** in src/ → Independent tasks
7. update **`pipelines/`** in src/→ Workflow orchestration
8. update **`main.py`** → Entry point

## 🚀 Steps to Follow in detailed explanation:
---
### **1. Update `config.yaml`**

* Stores **general configuration** (non-sensitive).
* Examples:
  * Dataset paths
  * Model save directories
  * Logging paths
* ✅ Purpose: Keeps project flexible and avoids hardcoding.
---
---
### **2. Update `secrets.yaml` [Optional]**

* Stores **sensitive credentials** (excluded from version control).
* Examples:
  * API keys
  * Database credentials
  * Cloud tokens
* ✅ Purpose: Protects secrets and prevents accidental leaks.

---
### **3. Update `params.yaml`**

* Stores **experiment parameters / hyperparameters**.
* Examples:
  * Batch size, learning rate, dropout rate, epochs
* ✅ Purpose: Supports reproducibility and experiment tracking (DVC, MLflow).
---

### **4. Update `entity/`**

* Define **Entity Classes** (dataclasses / pydantic models).
* Examples:
  * `DataIngestionConfig`
  * `TrainingConfig`
  * `ModelConfig`
* ✅ Purpose: Provides structured configs instead of raw dicts.
---
### **5. Update `ConfigurationManager` in `src/config/configuration.py`**

* Central class to **read config files** (`config.yaml`, `params.yaml`, `secrets.yaml`).
* Converts them into **Entity objects** for clean usage.
* ✅ Purpose: Single point of configuration handling.
---
### **6. Update `components/` in `src/components/`**

* Write **modular components** for each task.
* Examples:
  * `data_ingestion.py` → Load/download dataset
  * `data_validation.py` → Schema checks
  * `model_trainer.py` → Train model
  * `model_evaluation.py` → Evaluate metrics
* ✅ Purpose: Each component = independent, reusable, testable.
---
### **7. Update `pipeline/` in `src/pipelines/`**

* Define **workflow pipelines** using components.
* Examples:
  * `training_pipeline.py` → ingestion → validation → training → evaluation
  * `prediction_pipeline.py` → preprocessing → inference
* ✅ Purpose: Orchestrates multiple tasks into an end-to-end pipeline.
---
### **8. Update `main.py` in `src/`**

* Project **entry point**.
* Calls pipeline(s) for execution.
* Example:
```bash
from src.pipelines.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline()
```
* ✅ Purpose: Run the whole workflow with one command:
```bash
  python main.py
```
---


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

```bash
#to see Tensorboard UI
$ tensorboard --logdir=artifacts/callbacks/tensorboard_root_log_dir/
```
```bash
## How to Run

1. conda create -n catdog python=3.7 -y
2. conda activate catdog
3. pip install -r requirements.txt
4. python app.py
5. open in browser: http://localhost:8080/
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

```bash
	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 412962593190.dkr.ecr.us-east-1.amazonaws.com/catdog
	
## 4. Create EC2 machine (Ubuntu) 
     - downlaod .pem file for EC2
## 5. Open EC2 and Install docker in EC2 Machine:
	
	#optinal
# here we are updating package manager
	sudo apt-get update -y
	sudo apt-get upgrade
	
	#required
#installing docker in vertual machine
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker ubuntu
	newgrp docker 
  # also check docker version $ docker --version
	
# 6. Configure EC2-Vertual machine as self-hosted runner with GitHub Actions:
    go to specific github project repository settings > actions > runner > new self hosted runner > choose os > then run all commands one by one.
 ![commands available]("documents/self hosted runner commands.png")


# 7. Setup github secrets:
 - in gitHub > secrets and variables > Actions > New repository secret> add one by one all
 ## dowmnloaded from AWS ECR
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
## see in AWS right corner
    AWS_REGION = us-east-1
## ECR URI copied after creation of ECR
    AWS_ECR_LOGIN_URI = demo>>  412962593190.dkr.ecr.us-east-1.amazonaws.com
    ECR_REPOSITORY_NAME = catdog

## commit to Github main branch --> finaly your APP is LIVE!
	

```