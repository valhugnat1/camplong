# Camplong Event Platform

A full-stack application for managing and displaying events, built with a Vue.js frontend and a Python (FastAPI) backend, served via Nginx and containerized with Docker.
Expose html website at root for static site.

## Tech Stack

  - **Frontend:** Vue.js 3 (with Vite), Vue Router, Tailwind CSS
  - **Backend:** Python 3, FastAPI
  - **Web Server:** Nginx
  - **Containerization:** Docker

-----

## Project Structure

```
.
├── Dockerfile          # Defines the multi-stage Docker build
├── README.md           # This file
├── backend/            # The Python FastAPI application
├── docker/             # Nginx configuration and start script
├── frontend/           # The Vue.js single-page application
└── static-site/        # A simple static site served at the root
```

-----

## Getting Started

You can run this project in two ways: as a single Docker container (for production or easy setup) or by running the frontend and backend separately (for local development).

### Prerequisites

  - [Docker](https://www.docker.com/get-started)
  - [Node.js](https://nodejs.org/) (v18 or later)
  - [Python](https://www.python.org/downloads/) (v3.11 or later)

-----

## Option 1: Run with Docker (Recommended)

This method packages the entire application—frontend, backend, and web server—into a single container.

1.  **Build the Docker image:**
    Open your terminal in the project's root directory and run:

    ```bash
    docker build -t camplong_event:latest .
    ```

2.  **Run the Docker container:**
    This command starts the container and maps port `8001` on your local machine to port `80` inside the container.

    ```bash
    docker run -p 8001:80 camplong_event
    ```

3.  **Access the Application:**

      - Vue.js Event App: **[http://localhost:8001/app/](https://www.google.com/search?q=http://localhost:8001/app/)**
      - Static Site: **[http://localhost:8001/](https://www.google.com/search?q=http://localhost:8001/)**

-----

## Option 2: Run for Local Development

This method is ideal for active development, allowing for features like hot-reloading. You will need to run the backend and frontend in two separate terminals.

### Terminal 1: Launch the Backend API (Python)

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
    The `--reload` flag will automatically restart the server when you make changes to the code.

    ```bash
    uvicorn main:app --reload
    ```

    Your backend API is now running and listening at `http://localhost:8000`.

### Terminal 2: Launch the Frontend App (Vue.js)

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
    The terminal will show you the URL for the development server, which is usually **[http://localhost:5173](https://www.google.com/search?q=http://localhost:5173)**. Open this URL in your browser.

    > The frontend dev server is configured to automatically proxy API requests to your backend at `http://localhost:8000`, so everything will work together seamlessly.