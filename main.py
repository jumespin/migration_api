from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, status
from pydantic import BaseModel
import boto3
import json
from typing import Annotated, List
import models
from database import engine, SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

AWS_KEY_ID = "aws-access-id"
AWS_SECRET_ACCESS_KEY = "aws-access-key"
REGION_NAME = "us-east-2"


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class hiredBase(BaseModel):
    name: str
    datetime: str
    department_id: int
    job_id: int

class departmentBase(BaseModel):
    department: str

class jobBase(BaseModel):
    job: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated(Session, Depends(get_db))

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    s3.upload_fileobj(file.file, "employees-bronze", 'file_stage/{}'.format(file.filename))
    return {"filename": file.filename} 

@app.post("/hired/", status_code=status.HTTP_201_CREATED)
async def create_hired(hired: List[hiredBase], db: db_dependency):
    for items in hired:
        if len(hired) > 1000:
            return{"status": status.HTTP_406_NOT_ACCEPTABLE}
        else: 
            db_hired = models.hired_employees(**items.model_dump())
            db.add(db_hired)
            db.commit()
            return {"hired": "Loaded"}

s3 = boto3.client(
    "s3",
    aws_access_key_id= AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

