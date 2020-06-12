try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract 
import requests

def grammar(text):
	url = "https://grammarbot.p.rapidapi.com/check"

	payload = {
    	"text" : text,
    	"language" : "en-US",
		}
	headers = {
    'x-rapidapi-host': "grammarbot.p.rapidapi.com",
    'x-rapidapi-key': "428525cbbdmsh8b1afc706504d8bp18a80fjsn1fdef651d751",
    'content-type': "application/x-www-form-urlencoded"
    }

	response = requests.request("POST", url, data=payload, headers=headers)
	return response.json()

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    r = grammar(text)
    return r['matches'][0]

print(ocr_core('images/ocr_example_8.jpeg'))
