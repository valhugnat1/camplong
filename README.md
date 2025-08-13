# Camplong  

A full-stack application for managing and displaying events, built with a Vue.js frontend and a Python (FastAPI) backend. The entire application is served by Nginx and containerized with Docker for easy deployment.

It also serves a simple static HTML website at the root URL, while the main Vue.js application is available at the `/app/` path.

## ✨ Tech Stack

  * **Frontend:** Vue.js 3 (with Vite), Vue Router
  * **Backend:** Python 3, FastAPI
  * **Web Server:** Nginx
  * **Containerization:** Docker

-----

## 📂 Project Structure

The project is organized into distinct modules, each with a specific role.

```
.
├── Dockerfile          # Defines the multi-stage Docker build for production.
├── README.md           # This file.
├── backend/            # The Python FastAPI application (API).
├── docker/             # Nginx configuration and startup script.
├── frontend/           # The Vue.js single-page application (SPA).
└── static-site/        # Static HTML files served at the root URL.
```

-----

## 🌐 Serving the Static Site

The Nginx web server is configured to **expose the entire `static-site/` folder** at the root of the domain. This is perfect for landing pages, an "about" page, or any simple HTML content.

**How it works:**

  * Any file you place in the `static-site/` directory is directly accessible in the browser.
  * For example, if you create a file named `contact.html` inside `static-site/`, it will be available at `http://localhost:8001/contact.html`.
  * The `index.html` file in this folder will serve as the homepage at `http://localhost:8001/`.

-----

## 🚀 Getting Started

You can run this project in two ways: as a single Docker container (recommended for production or easy setup) or by running the frontend and backend separately (ideal for local development).

### Prerequisites

  * [Docker](https://www.docker.com/get-started)
  * [Node.js](https://nodejs.org/) (v22 or later)
  * [Python](https://www.python.org/downloads/) (v3.11 or later)

-----

## Option 1: Run with Docker (Recommended)

This method packages the entire application—frontend, backend, and web server—into a single, portable container.

1.  **Build the Docker image:**
    Open your terminal in the project's root directory and run:

    ```bash
    docker build -t camplong_event:latest .
    ```

2.  **Run the Docker container:**
    This command starts the container and maps port `8001` on your host machine to port `80` inside the container.

    ```bash
    docker run -p 8001:80 camplong_event
    ```

3.  **Access the Application:**

      * **Static Site:** [http://localhost:8001/](https://www.google.com/search?q=http://localhost:8001/)
      * **Vue.js Event App:** [http://localhost:8001/app/](https://www.google.com/search?q=http://localhost:8001/app/)

-----

## Option 2: Run for Local Development

This method is best for active development as it provides features like hot-reloading. You'll need to run the backend and frontend in two separate terminals.

### Terminal 1: Launch the Backend API (Python) 🐍

1.  **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the environment
    python -m venv venv

    # Activate it (macOS/Linux)
    source venv/bin/activate

    # Or activate it (Windows)
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the backend server:**
    The `--reload` flag automatically restarts the server when you change the code.

    ```bash
    uvicorn main:app --reload
    ```

    Your backend API is now running at `http://localhost:8000`.

### Terminal 2: Launch the Frontend App (Vue.js) 🎨

1.  **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2.  **Install dependencies:**

    ```bash
    npm install
    ```

3.  **Start the development server:**

    ```bash
    npm run dev
    ```

4.  **Access the Application:**
    Open the URL shown in your terminal, which is usually **[http://localhost:5173](https://www.google.com/search?q=http://localhost:5173)**. The dev server is pre-configured to proxy API requests to your backend at `http://localhost:8000`.

-----

## 📦 Deploying: Pushing the Image to Scaleway Registry

Once your image is built and tested, you can push it to a private container registry like Scaleway.

1.  **Log in to the Scaleway Registry:**
    This command uses a Scaleway Secret Key to log in securely without exposing it in your shell history. Make sure the `SCW_SECRET_KEY` environment variable is set.

    ```bash
    docker login rg.fr-par.scw.cloud/camplong -u nologin --password-stdin <<< "$SCW_SECRET_KEY"
    ```

2.  **Build the Docker image (if not already built):**
    Ensure you have the latest version of your application built.

    ```bash
    docker build -t camplong_event:latest .
    ```

3.  **Tag the image for the registry:**
    You need to tag your local image with the full registry path. The tag name (e.g., `latest` or a version number) helps you manage different versions.

    ```bash
    docker tag camplong_event:latest rg.fr-par.scw.cloud/camplong/camplong_event_mac:latest
    ```

    > **Note:** The `camplong_event_mac` part is your image name in the registry. You can change it to match your project's naming conventions.

4.  **Push the image:**
    This uploads your tagged image to the Scaleway container registry.

    ```bash
    docker push rg.fr-par.scw.cloud/camplong/camplong_event_mac:latest
    ```

    Your container image is now available in your private registry and ready for deployment\!