from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from a_accounts.models import Register, AcademicQualification
from .serializers import RegistersListSerializer, AcademicQualificationSerializer
from .utils import is_validated_user
def login_form(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            response = redirect("profile")
            
            response.set_cookie(
                key="access_token",
                value = access_token, 
                httponly=True,
                secure=False,
                samesite="Lax"
            )
            
            response.set_cookie(
                key="refresh_token",
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite="Lax"
            )
            return response
        else:
            return redirect("login")
    return render(request, "a_admin/login.html")

def profile(request):
    user = is_validated_user(request)
    if not user:
        return redirect("login")
    return render(request, "a_admin/profile.html", {"user":user})
    
            
def logout_view(request):
    response = redirect("login")
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response

def registers_list_view(request):
    user = is_validated_user(request)
    if not user :
        return redirect("login")
    
    if not user.is_staff:
        return HttpResponse("Unauthorized: Admins only", status=403)
    users = Register.objects.all()
    serializer = RegistersListSerializer(users, many=True)
    return render(request, "a_admin/registers_list.html", {"registers":serializer.data})

def generate_register_pdf(request):
    registers = Register.objects.all()
    template_path = 'a_admin/registers_list_pdf.html'
    context = {'registers': registers}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="register_list.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF <pre>' + html + '</pre>')
    return response

def delete_register_list(request):
    if not request.user.is_staff:
        return redirect('login')

    Register.objects.all().delete()
    return redirect('registers_list')
def delete_single_register(request, pk):
    if not request.user.is_staff:
        return redirect('login')

    Register.objects.get(id=pk).delete()
    return redirect('registers_list')