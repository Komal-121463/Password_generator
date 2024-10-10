import random
import string
from django.shortcuts import render

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lower + upper + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def password_view(request):
    password = None
    if request.method == 'POST':
        try:
            length = int(request.POST.get('length'))
            if length < 8:
                raise ValueError("Length must be at least 8")
            password = generate_password(length)
        except ValueError:
            password = "Please enter a valid length (minimum 8)."

    return render(request, 'password_generator/password.html', {'password': password})
