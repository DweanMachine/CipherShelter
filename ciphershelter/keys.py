from pathlib import Path
import base64
from cryptography.fernet import Fernet 
from core import CipherShelterError 

#Key management functions:
def generate_key() -> bytes:
  return Fernet.generate_key()

def save_key(key: bytes, path: Path) -> Path:
  path = Path(path)
  if path.exists():
    raise FileExistsError(f"Key file already exists: {path}. Will not overwrite.")
  path.write_bytes(key)
  return path

def validate_key(key: bytes) -> bool:
  try:
    if len(key) != 44:
      return False
    decoded = base64.urlsafe_b64decode(key)
    return len(decoded) == 32
  except Exception:
    return False

def load_key(path: Path) -> bytes:
  path == Path(path)

  if not path.exists():
    raise FileNotFoundError(f"Key file not found: {path}")
  
  if path.is_dir():
    raise IsADirectoryError("load_key expects a file, not a directory.")
  
  key = path.read_bytes()
  if not validate_key(key):
    raise CipherShelterError(f"Invalid key in file: {path}")


  return key


#print(validate_key(b"invalid_key"))