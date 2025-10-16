import pytesseract
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from io import BytesIO
from PIL import Image

app = FastAPI()

class ImageURLRequest(BaseModel):
    file: str  # URL of the image

@app.post("/ocr/")
async def ocr_from_url(request: ImageURLRequest):
    # Download the image
    response = requests.get(request.file)
    if response.status_code != 200:
        return {"error": "Failed to download image"}
    
    # Convert image for OCR
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # Run OCR with Tesseract
    extracted_text = pytesseract.image_to_string(img, config="--psm 6")

    return {"detected_text": extracted_text.strip()}
