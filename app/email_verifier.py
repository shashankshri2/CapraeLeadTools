# app/email_verifier.py
import re
import socket
import requests

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

def is_domain_active(domain):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f"http://{domain}", timeout=3)
        return response.status_code == 200
    except:
        return False

def verify_email_and_domain(email):
    if not is_valid_email(email):
        return "❌ Invalid format", "❌"
    
    domain = email.split("@")[-1]
    domain_status = "✅ Active" if is_domain_active(domain) else "❌ Inactive"
    return "✅ Valid format", domain_status
