from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from crypto_sandbox.classical.affine import encrypt as aff_enc, decrypt as aff_dec
from crypto_sandbox.classical.caesar import encrypt as cae_enc, decrypt as cae_dec
from crypto_sandbox.classical.rail_fence import encrypt as rail_enc, decrypt as rail_dec
from crypto_sandbox.classical.vigenere import encrypt as vig_enc, decrypt as vig_dec

app = FastAPI(title="Crypto-Sandbox API")

class Job(BaseModel):
    text: str
    cipher: str
    mode: str


    key: Optional[str] = None
    a: Optional[int] = None
    b: Optional[int] = None
    rails: Optional[int] = None
    shift: Optional[int] = None

@app.post("/run")
def run(job: Job):
    cip = job.cipher.lower()
    mode = job.mode.lower()
    
    if cip == "affine":
        fn = aff_enc if mode=="encrypt" else aff_dec
        return {"result": fn(job.text, job.a, job.b)}

    if cip == "caesar":
        fn = cae_enc if mode=="encrypt" else cae_dec
        return {"result": fn(job.text, job.shift)}
    
    if cip == "rail":
        fn = rail_enc if mode=="encrypt" else rail_dec
        return {"result": fn(job.text, job.rails)}
    
    if cip == "vigenere":
        fn = vig_enc if mode=="encrypt" else vig_dec
        return {"result": fn(job.text, job.key)}
    
    return {"error": f"Unknown cipher '{job.cipher}'"}

frontend_dir = Path(__file__).parent.parent / "webapp"
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")