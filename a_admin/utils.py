from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import redirect

def is_validated_user(request):
    token = request.COOKIES.get("access_token")
    if not token:
        return redirect("login")  # Not logged in
    
    auth = JWTAuthentication()
    try:
        validated_token = auth.get_validated_token(token)
        user = auth.get_user(validated_token)
        return user
    except AuthenticationFailed:
        return None