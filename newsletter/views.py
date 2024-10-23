from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import OpportunityModelForm
from .forms import ContactForm
from django.contrib import messages

def index(request):
    form = OpportunityModelForm()
    context = {
        "form": form
    }
    if request.POST:
        form = OpportunityModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            print(form.cleaned_data)
            name = form.cleaned_data.get("name")
            print(name)
            if not instance.name:
                name = "New Opportunity"
                instance.name = name
            instance.save()
            messages.add_message(request, messages.SUCCESS, f'Thanks, {name}')
        else:
            for key, value in form.errors.items():
                print(value)
                messages.add_message(request, messages.ERROR, f'For {key}: {value}')
    return render(request, "newsletter/index.html", context)

def contact(request):
    form = ContactForm()
    context = {
        "form": form
    }
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data.get("name")
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            subject = "¡¡ New Contact !!" if not form_name else f"¡¡ New Contact - {form_name}!!"
            send_mail(
                subject=subject,
                message=f"{form_email}: {form_message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["gustavo.ortega.palacios@gmail.com"],
                fail_silently=False,
            )
        else:
            for key, value in form.errors.items():
                print(value)
                messages.add_message(request, messages.ERROR, f'For {key}: {value}')

    return render(request, "newsletter/contact.html", context)
