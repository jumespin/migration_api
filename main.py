from fastapi import FastAPI, UploadFile, File
import boto3

app = FastAPI(root_path="/dev")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    s3.upload_fileobj(file.file, "employees-bronze", file.filename)
    return {"filename": file.filename} 

s3 = boto3.client(
    "s3",
    aws_access_key_id="aws-access-id",
    aws_secret_access_key="aws-access-key",
    region_name="us-east-2"
)

