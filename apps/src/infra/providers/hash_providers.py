from passlib.context import CryptContext

pdw_context = CryptContext(schemes=['bcrypt'])

def generate_hash(text):
    return pdw_context.hash(text)

def verify_hash(text, hash):
    return pdw_context.verify(text, hash)