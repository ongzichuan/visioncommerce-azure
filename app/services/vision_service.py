import os
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()

def analyse_image(image_bytes):
    endpoint = os.getenv("AZURE_VISION_ENDPOINT")
    key = os.getenv("AZURE_VISION_KEY")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    result = client.analyze(
        image_data=image_bytes,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS
        ]
    )

    caption = result.caption.text if result.caption else "No caption detected"
    tags = [tag.name for tag in result.tags.list] if result.tags else []

    return {
        "caption": caption,
        "tags": tags
    }