from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/jobs")
def get_jobs():
    return [
        {"title": "Meen pidikkal", "company": "KULAM PVT LTD"},
        {"title": "KOKKINE ODIKKAL", "company": "PADDY FIELD LLC"},
        {"title": "SOFTWARE DESTRUCTION", "company": ""},
    ]
