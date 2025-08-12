# main.py
import json
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

# --- Database Simulation ---
# In a real application, you would use a proper database.
# For this example, we'll use a simple JSON file as a data store.

DB_FILE = "db.json"

def load_db():
    """Loads the database from the JSON file."""
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, return a default structure
        return {"events": [
            {
                "id": 1,
                "title": "Tech All Night Long",
                "date": "2025-09-09T22:00:00",
                "location": "Le Glazart",
                "description": "An unforgettable night of tech house and deep tech with the best local DJs.",
                "artists": ["Theo Morin", "Emile Rey"],
                "price": 15.50,
                "image": "https://placehold.co/600x400/000000/FFFFFF?text=Tech+Night"
            },
            {
                "id": 2,
                "title": "Techno-Cooking",
                "date": "2025-09-11T16:00:00",
                "location": "La Rotonde",
                "description": "A unique experience combining a cooking workshop with a live techno set. Learn to cook amazing food while dancing.",
                "artists": ["DJ Cook", "MC Spice"],
                "price": 25.00,
                "image": "https://placehold.co/600x400/FF6347/FFFFFF?text=Techno-Cooking"
            }
        ], "registrations": []}

def save_db(data):
    """Saves the database to the JSON file."""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Initialize the database file
db_data = load_db()
save_db(db_data)


# --- Pydantic Models ---
# These models define the structure of the data for request and response validation.

class Event(BaseModel):
    id: int
    title: str
    date: str
    location: str
    description: str
    artists: List[str]
    price: float
    image: str

class Registration(BaseModel):
    event_id: int
    name: str
    email: str

class RegistrationInput(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@example.com")


# --- FastAPI Application ---

app = FastAPI(title="Camplong API")

# --- CORS Middleware ---
# This allows your Vue.js frontend (running on a different domain/port)
# to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# --- API Routes ---

@app.get("/")
def root():
    """Root endpoint for the API."""
    return {"message": "Camplong backend running"}

@app.get("/api/events", response_model=List[Event])
def get_all_events():
    """
    Retrieve all upcoming events.
    """
    db = load_db()
    return db.get("events", [])

@app.get("/api/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    """
    Retrieve a single event by its ID.
    """
    db = load_db()
    for event in db.get("events", []):
        if event["id"] == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@app.post("/api/events/{event_id}/register", response_model=Registration)
def set_registration(event_id: int, registration_input: RegistrationInput):
    """
    Register a user for a specific event.
    """
    db = load_db()
    
    # Check if the event exists
    event_exists = any(event["id"] == event_id for event in db.get("events", []))
    if not event_exists:
        raise HTTPException(status_code=404, detail="Event not found")

    new_registration = Registration(
        event_id=event_id,
        name=registration_input.name,
        email=registration_input.email
    )

    db["registrations"].append(new_registration.dict())
    save_db(db)
    
    return new_registration

# --- How to run the server ---
# 1. Save this code as `main.py`.
# 2. Make sure you have the necessary libraries:
#    pip install fastapi "uvicorn[standard]" pydantic
# 3. Run the server from your terminal:
#    uvicorn main:app --reload
#
# The API will be available at http://127.0.0.1:8000
