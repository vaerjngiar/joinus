from django.views.generic import FormView, TemplateView
from .forms import JoinForm
from .mixins import AjaxFormMixin


class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = "contact/contact.html"
    success_url = "/form-success/"


class SuccessView(TemplateView):
    template_name = "contact/success.html"




