from django import forms
from creative.models import Creative


class CreativeForm(forms.ModelForm):
    class Meta:
        model = Creative
        fields = [
            "title",
            "brand",
            "image",
            "posting_date",
            "status",
            "rejection_reason",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
            "posting_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rejection_reason": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
        }
