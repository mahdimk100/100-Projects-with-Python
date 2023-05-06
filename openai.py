import openai
import requests
from requests.structures import CaseInsensitiveDict

openai.api_key = "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"

def generate_image(prompt):
    url = "https://api.openai.com/v1/images/generations"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {openai.api_key}"

    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """

    resp = requests.post(url, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image "+resp.text)

    response_text = resp.text
    response_text = response_text.replace("\\","")
    response_text = response_text.strip("\"")

    return response_text

url = generate_image("a yellow banana on a blue plate")
