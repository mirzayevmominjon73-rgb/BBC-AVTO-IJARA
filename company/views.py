from django.views.generic import TemplateView
from .models import About, Contact, Employee

class AboutView(TemplateView):
    template_name = 'company/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['employees'] = Employee.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'company/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context
