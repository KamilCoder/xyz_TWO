from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse
import secrets
import string

app = FastAPI()


security = HTTPBasic()
key=5
cipher_in = string.printable
cipher_out = string.printable[key:]+string.printable[:key]
#encoded = str()
#decoded = str()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "admin")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def encoder(text):
    text = text.encode('unicode_escape').decode()
    encoded = (text.translate(text.maketrans(cipher_in,cipher_out)))
    return(encoded)


def decoder(encoded):
    encoded = encoded.encode().decode('unicode_escape')
    decoded = (encoded.translate(encoded.maketrans(cipher_out,cipher_in)))
    return(decoded)

@app.get("/")
def home(username: str = Depends(get_current_username)):
    html_content="""
    <HTML>
    <H1><CENTER>TO USE FAST CEZAR GO TO:<br>address:8000/ENCODER/YOUR_TEXT or<br>address:8000/DECODER/YOUR_ENCODED_TEXT</CENTER></H1>
    <H2><CENTER>FOR MORE GO TO FAST CEZAR DOCS<CENTER></H2>
    </HTML>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/encoder/{plaintext}")
def api_encoder(plaintext: str, username: str = Depends(get_current_username)):
    p_text = encoder(plaintext)
    return{"cypher": (p_text)}


@app.get("/decoder/{ciphertext}")
def api_decoder(ciphertext: str, username: str = Depends(get_current_username)):
    c_text = decoder(ciphertext)
    return {"decoded": (c_text)}