# VisionCommerce Azure

AI-Powered E-Commerce Image Optimisation Platform built using Microsoft Azure, Azure AI Vision, OpenAI, Azure Blob Storage, Azure Container Apps, Docker, and Azure DevOps.

---

## Project Overview

VisionCommerce Azure was created to solve a common problem faced by online sellers on platforms such as Shopee, Lazada, Carousell, Facebook Marketplace, and other e-commerce marketplaces.

Many sellers want professional-looking product images and attractive product descriptions, but they often face two challenges:

1. They need clean product photos with backgrounds removed.
2. They struggle to write effective product listings due to limited copywriting skills or lack of confidence in English.

As a result, many users end up paying for third-party software or online services just to remove image backgrounds or generate product descriptions.

VisionCommerce Azure provides an AI-powered solution that automates these tasks. Users can upload a product image, automatically remove the background, analyse the image using Azure AI Vision, and generate marketplace-ready product listings using AI.

This project serves as a practical implementation of the knowledge gained throughout Microsoft's AI certification pathway, including:

* AI-901: Microsoft Azure AI Fundamentals
* AI-103: Azure AI Apps and Agents Developer Associate
* AI-200: Azure AI Cloud Developer Associate Learning Path
* AI-300: Machine Learning Operations Engineer Associate Learning Path

The goal of this project was to utilise Microsoft-native cloud and AI services wherever possible to demonstrate real-world application of Azure technologies.

Due to Azure OpenAI quota limitations on a student subscription, OpenAI API was used for generative content creation. Apart from this limitation, the majority of the solution is built using native Microsoft Azure services.

---

## Problem Statement

Online sellers frequently encounter the following challenges:

* Poor-quality product images with distracting backgrounds
* Lack of copywriting skills for product listings
* Limited English proficiency
* Expensive subscription-based tools for image editing
* Additional costs for AI-generated product descriptions
* Time-consuming listing creation process

VisionCommerce Azure addresses these challenges by providing an all-in-one AI-powered workflow that helps users create professional product listings quickly and efficiently.

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

Automatically remove image backgrounds using rembg to create clean and professional product photos.

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

### <img width="1536" height="1024" alt="visioncommerce_arch_diagram" src="https://github.com/user-attachments/assets/4f58a4f3-070e-4d9e-ae0d-4456db0a1e87" />

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

Hosts the Streamlit web application and provides scalable cloud deployment.

### Azure Container Registry

Stores Docker container images used for deployment.

### Azure Blob Storage

Stores uploaded product images securely in the cloud.

### Azure AI Vision

Provides image captioning and image tag extraction capabilities.

### Azure DevOps

Provides automated CI/CD deployment pipelines.

---

## AI Capabilities

### Computer Vision

Azure AI Vision analyses uploaded images and generates:

* Image captions
* Product-related tags
* Visual insights

### Generative AI

OpenAI generates:

* Product titles
* Product descriptions
* Key selling points
* Marketplace-ready listing content
* SEO-friendly keywords

### Image Enhancement

Background removal improves product presentation and creates cleaner images suitable for online marketplaces.

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

## Certification Knowledge Applied

This project was designed to apply concepts learned from Microsoft's AI certification pathway.

### AI-901

Applied concepts:

* Artificial Intelligence fundamentals
* Computer Vision
* Generative AI
* Responsible AI principles

### AI-103

Applied concepts:

* Azure AI Vision integration
* AI service implementation
* API integration
* AI solution development

### AI-200

Applied concepts:

* AI application workflows
* AI service orchestration
* Cloud-based AI deployment

### AI-300

Applied concepts:

* AI solution architecture
* Cloud-native AI design
* Scalable AI application deployment

### Azure and DevOps Skills

Applied concepts:

* Azure Container Apps
* Azure Container Registry
* Azure Blob Storage
* Docker containerisation
* Azure DevOps CI/CD
* Cloud-native application deployment

---

## Screenshots

### Home Page

<img width="1600" height="760" alt="WhatsApp Image 2026-06-09 at 4 24 51 PM" src="https://github.com/user-attachments/assets/fb370934-97c8-4169-808f-6993de64300d" />

### Product Upload

<img width="1600" height="964" alt="WhatsApp Image 2026-06-09 at 4 26 02 PM" src="https://github.com/user-attachments/assets/f28353f6-5275-40f5-92e3-8fefd495479c" />

### Background Removal

<img width="1328" height="1600" alt="WhatsApp Image 2026-06-09 at 4 26 25 PM" src="https://github.com/user-attachments/assets/61928afd-52b9-4105-94ac-6b730dd83103" />

### Azure Vision Analysis

<img width="847" height="1259" alt="WhatsApp Image 2026-06-09 at 4 28 05 PM" src="https://github.com/user-attachments/assets/7628abb3-bcd8-4a86-81ac-4dfe2138788c" />

### AI Listing Generation

<img width="1600" height="848" alt="WhatsApp Image 2026-06-09 at 4 30 00 PM" src="https://github.com/user-attachments/assets/62323048-51ef-4869-a7ed-f15b2868cd1f" />

### Azure DevOps Pipeline Success

<img width="1600" height="856" alt="WhatsApp Image 2026-06-09 at 4 29 08 PM" src="https://github.com/user-attachments/assets/196b8e62-5c26-46c1-9903-b958fb7eb124" />

### Azure Container Apps Deployment

<img width="1600" height="377" alt="WhatsApp Image 2026-06-09 at 4 35 35 PM" src="https://github.com/user-attachments/assets/511b3ad1-4b8b-4f7d-b529-7f51c1359240" />

### Azure Blob Storage Upload

<img width="1600" height="491" alt="WhatsApp Image 2026-06-09 at 4 36 21 PM" src="https://github.com/user-attachments/assets/e424c0b1-92e4-4a8f-8a90-e57cd30bcf79" />

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

### Azure OpenAI Quota Limitations

As the project was developed using an Azure student subscription, Azure OpenAI quota limitations prevented full implementation using Azure OpenAI services.

To overcome this limitation, OpenAI API was integrated while maintaining the rest of the architecture on Microsoft Azure services.

### Azure Container Apps Revision Management

Understanding revision deployment and traffic routing.

### Container Image Updates

Ensuring latest Docker images were successfully deployed.

### Memory Allocation

Background removal required increasing container memory allocation from 1 Gi to 2 Gi.

### Prompt Engineering

Designing prompts that generate effective marketplace listings suitable for e-commerce platforms.

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
* Prompt Engineering
* Computer Vision Solutions
* Generative AI Applications

Most importantly, this project allowed me to transform theoretical knowledge gained from Microsoft AI certifications into a practical real-world solution that solves a genuine business problem for online sellers.

---

## Future Improvements

Potential enhancements include:

* Azure OpenAI Integration
* AI Category Detection
* Automatic Product Name Generation
* Listing History Tracking
* Database Integration
* User Authentication
* Multi-language Listing Generation
* SEO Optimisation Suggestions
* Marketplace-Specific Templates
* Product Recommendation Features

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
