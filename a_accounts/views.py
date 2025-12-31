from django.shortcuts import render, redirect
from .forms import RegisterForm, AcademicFormSet

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        formset = AcademicFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            user = form.save()
            qualification = formset.save(commit=False)
            
            for qual in qualification:
                qual.register = user
                qual.save()
            return redirect('success_view') 
    else:
        form = RegisterForm()
        formset = AcademicFormSet()
    return render(request, 'a_accounts/register.html', {'form': form, 'formset': formset})

    
def success_view(request):
    return render(request, 'a_accounts/success.html')