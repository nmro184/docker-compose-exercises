# Flask Docker Container Manager

## Overview

This project is a Flask application that provides a simple web interface for managing Docker containers on a server. Users can create, view, and delete containers through the application. Additionally, it allows accessing the containers via their URLs.

## Mission

The mission of this project is to create a user-friendly tool for managing Docker containers. The key features include:

- **Container Management:**
  - Create new Docker containers with specified parameters.
  - View a list of existing containers with their details.
  - Delete containers that are no longer needed.

- **Container Access:**
  - Access containers through their URLs directly from the application.

## Setup

Follow these steps to set up and run the Flask Docker Container Manager:

1. **Install Dependencies:**
    - Ensure Python and Docker are installed on your server.
    - Install required Python packages:
        ```bash
        pip install Flask docker
        ```

2. **Run the Application:**
    - Execute the Flask application:
        ```bash
        python app.py
        ```
    - The application will be accessible at `http://127.0.0.1:5000/` by default.

## Usage

### Home Page:

- Visit the home page to view a list of existing Docker containers.
- Click "Create Container" to initiate the container creation process.

### Create Container:

- Enter the container details (name, image, host port, container port) and submit the form.
- The application will redirect you to the container's URL automatically.

### Access Containers:

- Each container entry on the home page has a link labeled "Open Container."
- Clicking this link redirects you to the container's URL.

### Delete Container:

- Click "Delete" next to a container on the home page to stop and remove the container.

## Notes

- Ensure that your Docker setup allows the application to create and manage containers.
- This is a basic example, and you may need to enhance security measures for a production environment.

