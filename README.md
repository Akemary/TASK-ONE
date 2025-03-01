# Flask App with Docker

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

This command will use the `Dockerfile` to create a Docker image with the name `flask-app`.

### 3. Run the Docker Container

Once the image is built, run the Flask app container:

```bash
docker run -p 5000:5000 task_one
```

This will map port 5000 from your local machine to port 5000 inside the Docker container. The Flask app will be accessible on your local machine at `http://localhost:5000`.

### 4. Verify the Flask App

Open a browser and go to `http://localhost:5000`. 


## Project Structure

```
task_one/
├── Dockerfile            # Docker configuration for the app
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
└── README.md             # This file
```


