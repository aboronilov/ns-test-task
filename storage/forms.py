from django import forms
from .models import Document

class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["name", "content", "is_deleted"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'w-full rounded-md shadow-md mb-2'}),
            "content": forms.Textarea(attrs={'class': 'w-full rounded-md shadow-md mt-2'})
        }

class UpdateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["name", "content"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'w-full rounded-md shadow-md mb-2'}),
            "content": forms.Textarea(attrs={'class': 'w-full rounded-md shadow-md mt-2'})
        }