# Flask App Containerised with Docker

This repository contains a simple flask application that has the HTML content directly inside the application.<br>
The HTML content is a student registration form that can be filled and saved<br>

### app.py
This contains code for the main Flask application.

### Dockerfile
It contains docker configarations for the application.

### requirement.txt
This contains the python dependencies

### README.md
This has all the description for the directory.

### Steps for Accessing the Application

### 1. Clone the Repository (if you haven't already)

```bash
git clone https://github.com/Akemary/task_one.git
cd task_one
```

### 2. Build the Docker Image

In the project directory, run the following command to build the Docker image:

```bash
docker build -t task_one .
```

This command will use the `Dockerfile` to create a Docker image with the name `task_one`.

### 3. Run the Docker Container

Once the image is built, run the Flask app container:

```bash
docker run -p 5000:5000 task_one
```

This will map port 5000 from your local machine to port 5000 inside the Docker container. The Flask app will be accessible on your local machine at `http://localhost:5000`.

### 4. Verify the Flask App

Open a browser and go to `http://localhost:5000`. 