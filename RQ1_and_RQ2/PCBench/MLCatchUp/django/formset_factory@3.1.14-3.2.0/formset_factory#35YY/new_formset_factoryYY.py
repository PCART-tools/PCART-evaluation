from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
from django.forms import formset_factory
ExampleFormSet = formset_factory(form=ExampleForm, formset=ExampleForm, extra=1, can_order=False, can_delete=False, max_num=None, validate_max=False, absolute_max=None, can_delete_extra=True)
