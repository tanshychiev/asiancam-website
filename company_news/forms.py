from django import forms
from .models import CompanyNews


class CompanyNewsForm(forms.ModelForm):
    class Meta:
        model = CompanyNews
        fields = [
            "title_en", "title_kh", "title_cn",
            "short_en", "short_kh", "short_cn",
            "content_en", "content_kh", "content_cn",
            "image", "detail_image", "video",
            "sort_order",
            "is_published",
        ]

        widgets = {
            "title_en": forms.TextInput(attrs={"placeholder": "English title"}),
            "title_kh": forms.TextInput(attrs={"placeholder": "Khmer title"}),
            "title_cn": forms.TextInput(attrs={"placeholder": "Chinese title"}),

            "short_en": forms.Textarea(attrs={"rows": 4, "placeholder": "English short info"}),
            "short_kh": forms.Textarea(attrs={"rows": 4, "placeholder": "Khmer short info"}),
            "short_cn": forms.Textarea(attrs={"rows": 4, "placeholder": "Chinese short info"}),

            "content_en": forms.Textarea(attrs={"rows": 12, "placeholder": "English full content"}),
            "content_kh": forms.Textarea(attrs={"rows": 12, "placeholder": "Khmer full content"}),
            "content_cn": forms.Textarea(attrs={"rows": 12, "placeholder": "Chinese full content"}),

            "sort_order": forms.NumberInput(attrs={
                "placeholder": "Higher number shows first, e.g. 100",
                "min": "0"
            }),
        }