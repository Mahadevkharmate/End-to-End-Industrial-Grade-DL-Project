# Step 1: Base Image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy all project files into container
COPY . /app


# Install AWS CLI
#installs the AWS Command Line Interface (CLI) tool inside the image. To install AWS CLI so your container can interact with AWS services (like S3, EC2, etc.) directly.
RUN apt update -y && apt install awscli -y 

# Step 4: Install dependencies for OpenCV, audio/video, unzip, and Python packages
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt

# Step 5: Expose port Flask will run on
# EXPOSE 5000

# Step 6: Command to run the Flask app
CMD ["python", "app.py"]
