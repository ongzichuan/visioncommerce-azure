# VisionCommerce Azure

AI-Powered E-Commerce Image Optimisation Platform built using Microsoft Azure, Azure AI Vision, OpenAI, Azure Blob Storage, Azure Container Apps, Docker, and Azure DevOps.

---

## Project Overview

VisionCommerce Azure is a cloud-native AI-powered e-commerce platform that helps sellers optimise product images and generate marketplace-ready product listings.

Users can upload a product image, automatically remove the image background, analyse the image using Azure AI Vision, and generate professional product listings using OpenAI.

The project demonstrates practical implementation of cloud computing, artificial intelligence, containerisation, and DevOps automation on Microsoft Azure.

---

## Live Demo

Application URL:

```text
https://visioncommerce-app.purplemushroom-a6faaee0.southeastasia.azurecontainerapps.io/
```

---

## Features

### Image Upload

Upload product images in JPG, JPEG, or PNG format.

### Background Removal

Automatically remove image backgrounds using rembg.

### Azure AI Vision Analysis

Generate image captions and extract image tags using Azure AI Vision.

### Product Quality Assessment

Evaluate image quality based on Azure Vision analysis.

### AI Listing Generation

Generate marketplace-ready product listings using OpenAI.

### Azure Blob Storage

Store uploaded product images securely in Azure Storage.

### Cloud Deployment

Deploy and host the application using Azure Container Apps.

### CI/CD Automation

Automatically build and deploy new versions using Azure DevOps Pipelines.

---

## Architecture

### 
<img width="1536" height="1024" alt="visioncommerce_arch_diagram" src="https://github.com/user-attachments/assets/b9402092-9f43-4e86-a7c5-e843003b729d" />

### User Workflow

```text
User Upload Product Image
            │
            ▼
Azure Container Apps
(Streamlit Frontend)
            │
            ├───────────────► Azure Blob Storage
            │
            ▼
Background Removal (rembg)
            │
            ▼
Azure AI Vision
(Caption + Tags)
            │
            ▼
OpenAI GPT
(Listing Generation)
            │
            ▼
Marketplace Ready Listing
```

### DevOps Workflow

```text
GitHub Repository
        │
        ▼
Azure DevOps Pipeline
        │
        ▼
Docker Build
        │
        ▼
Azure Container Registry
        │
        ▼
Azure Container Apps
```

---

## Technology Stack

| Component            | Technology               |
| -------------------- | ------------------------ |
| Frontend             | Streamlit                |
| Programming Language | Python                   |
| Containerisation     | Docker                   |
| CI/CD                | Azure DevOps Pipelines   |
| Container Registry   | Azure Container Registry |
| Hosting              | Azure Container Apps     |
| Storage              | Azure Blob Storage       |
| Computer Vision      | Azure AI Vision          |
| Generative AI        | OpenAI GPT               |
| Background Removal   | rembg                    |
| Source Control       | GitHub                   |

---

## Azure Services Used

### Azure Container Apps

Hosts the Streamlit web application.

### Azure Container Registry

Stores Docker container images.

### Azure Blob Storage

Stores uploaded product images.

### Azure AI Vision

Provides image captioning and image tag extraction.

### Azure DevOps

Provides automated CI/CD deployment.

---

## Project Workflow

### Step 1

User uploads a product image.

### Step 2

Image background is removed using rembg.

### Step 3

Original image is uploaded to Azure Blob Storage.

### Step 4

Azure AI Vision analyses the image.

Outputs:

* Image Caption
* Image Tags

### Step 5

OpenAI generates:

* Product Title
* Product Description
* Key Selling Points
* Marketplace Listing Content
* SEO Keywords

### Step 6

Results are displayed to the user.

---

## Screenshots

### Home Page

Insert Screenshot 01

### Product Upload

Insert Screenshot 02

### Background Removal

Insert Screenshot 03

### Azure Vision Analysis

Insert Screenshot 04

### AI Listing Generation

Insert Screenshot 05

### Azure DevOps Pipeline Success

Insert Screenshot 06

### Azure Container Apps Deployment

Insert Screenshot 07

### Azure Blob Storage Upload

Insert Screenshot 08

---

## CI/CD Pipeline

The project uses Azure DevOps Pipelines to automate deployments.

Pipeline Process:

```text
Git Push
   │
   ▼
Azure DevOps Pipeline
   │
   ▼
Docker Build
   │
   ▼
Azure Container Registry
   │
   ▼
Azure Container Apps Deployment
```

---

## Challenges Encountered

### Azure Container Apps Revision Management

Understanding revision deployment and traffic routing.

### Container Image Updates

Ensuring latest Docker images are successfully deployed.

### Memory Allocation

Background removal required increasing container memory allocation from 1 Gi to 2 Gi.

### OpenAI Integration

Configuring API keys and prompt engineering for listing generation.

### Azure DevOps Automation

Building a fully automated CI/CD deployment pipeline.

---

## Key Learnings

Through this project, I gained practical experience in:

* Azure Container Apps
* Azure Container Registry
* Azure Blob Storage
* Azure AI Vision
* OpenAI API Integration
* Docker Containerisation
* Azure DevOps CI/CD
* Cloud Native Application Deployment
* AI-Powered Application Development

---

## Future Improvements

Potential enhancements include:

* AI Category Detection
* Automatic Product Name Generation
* Listing History Tracking
* Database Integration
* User Authentication
* Multi-language Listing Generation
* SEO Optimisation Suggestions

---

## Repository Structure

```text
visioncommerce-azure
│
├── app
│   ├── main.py
│   └── services
│       ├── background_service.py
│       ├── openai_service.py
│       ├── scoring_service.py
│       ├── storage_service.py
│       └── vision_service.py
│
├── Dockerfile
├── requirements.txt
├── azure-pipelines.yml
├── .env.example
├── .gitignore
└── README.md
```

---

## Author

### Ong Zichuan

Singapore

GitHub:

```text
https://github.com/ongzichuan
```

Project:

```text
VisionCommerce Azure
```

---

## Project Status

Current Status:

✅ Completed

Version:

```text
v2
```

Deployment:

```text
Azure Container Apps
```

Environment:

```text
Production
```
