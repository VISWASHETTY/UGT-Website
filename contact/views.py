from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF for simplicity (not recommended for production)
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save data to the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('thank_you')  # Redirect to a thank you page

    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

# def quote(request):
#     return render(request, 'quote.html')

def ourteam(request):
    return render(request, 'team.html')

def career(request):
    return render(request, 'career.html')

from django.shortcuts import render
from .models import Contact

def contact_list(request):
    # Retrieve all contact entries from the database
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def thank_you_view(request):
    return render(request, 'thankyou.html')



from django.shortcuts import render, redirect
from .models import QuoteRequest

def quote_request_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')

        if name and email and service and message:  # Ensure all fields are filled
            QuoteRequest.objects.create(name=name, email=email, service=service, message=message)
            return redirect('quote')  # Refresh the page after submission

    return render(request, 'quote.html')
