# Stress Testing Application

This repository contains a Python application designed to perform various stress tests on system resources such as memory, disk, CPU, network, and MySQL database. It is equipped with logging features, suggestions for performance optimization, and integration with WhatsApp for notification purposes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Components](#components)
- [Continuous Integration](#continuous-integration)
- [Dockerization](#dockerization)
- [Logging and Monitoring](#logging-and-monitoring)

## Features

- Memory, Disk, CPU, Network, and MySQL stress testing.
- Logging of stress test results.
- Suggestions for performance optimization based on the test results.
- Notifications sent to WhatsApp using Twilio.
- CI/CD integration with Jenkins.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11 or higher
- MySQL server (for MySQL stress testing)
- Twilio account (for WhatsApp notifications)
- Docker and Docker Compose (for containerization)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sweety19chowdhary/Stress_Testing.git
   cd Stress_Testing
   
2. **Install dependencies:**
   
- Create a virtual environment and install the required packages:
   
3. **Configure MySQL**:

- Ensure you have a MySQL server running and create a database named cinema_booking_system.
- Update the DB_CONFIG in app.py with your MySQL credentials.

4. **Set up Twilio for WhatsApp**:
   
- Sign up for a Twilio account.
- Get your Twilio Account SID and Auth Token.
- Update the send_to_whatsapp.py file with your Twilio credentials.

## Usage
- Run the application using: - python app.py
- Follow the prompts to select a stress test to run. The results will be logged in stress_test.log, and suggestions will be saved in suggestions.txt.
- To send suggestions to WhatsApp, run: - python send_to_whatsapp.py

## Components
**app.py**: The main application script that conducts stress tests and logs the results.
**ai_suggestions.py**: A script that analyzes the logs and fetches suggestions from an AI service.
**send_to_whatsapp.py**: Sends suggestions via WhatsApp using the Twilio API.
**Dockerfile**: Defines the Docker image for the application.
**requirements.txt**: Lists the required Python packages for the application.
**Jenkinsfile**: Configures the CI/CD pipeline in Jenkins to automate builds on code changes.
**stress_test.log**: Log file containing results of the stress tests.
**suggestions.txt**: File storing suggestions generated from the stress test analysis.

## Continuous Integration
- The project uses Jenkins for CI/CD. A Jenkins pipeline is defined in the Jenkinsfile, which triggers builds on every push to the GitHub repository.

## Dockerization
- The application can be containerized using the provided Dockerfile.
- To build and run the Docker image, use the following commands:
    docker build -t stress-app .
    docker run -it stress-app
- You can also find the containerized application on my Docker Hub account https://hub.docker.com/r/sannapavithra/stress-app-testingggg

## Logging and Monitoring
- Logging is implemented using Python's logging module.
- All stress test results are logged in stress_test.log, which helps in monitoring application performance.
