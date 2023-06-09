from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def read_root():
#     response = {"hello": "world"}
#     return response

@app.get("/api")
async def getRecords():
    response = {"id": "recordID"}
    return response

@app.post("/api")
async def addRecord():
    response = {"name": "johnny appleseed"}
    return response

@app.get("/api/{id}")
async def getRecords(id):
    response = {f"{id}": "recordID_getRecords"}
    return response

@app.put("/api/{id}")
async def updateRecord(id):
    response = {f"{id}": "recordID_updateRecords"}
    return response

@app.delete("/api/{id}")
async def deleteRecord(id):
    response = {f"{id}": "recordID_deleteRecord"}
    return response
