from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil

# This object must be named 'app' to match the run command
app = FastAPI(title="Model Uploader API")

@app.post("/upload/")
async def upload_model_file(model_file: UploadFile = File(...)):
    """
    Receives and saves a .h5 model file.
    """
    destination_path = f"uploads_{model_file.filename}"
    
    try:
        print(f"Receiving file: {model_file.filename}...")
        
        with open(destination_path, "wb") as buffer:
            shutil.copyfileobj(model_file.file, buffer)
            
        print(f"File '{model_file.filename}' saved successfully.")
        
        return {
            "message": "File uploaded successfully",
            "filename": model_file.filename,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was an error: {e}")

@app.get("/")
async def root():
    return {"message": "Server is running. Send a POST request to /upload/."}
