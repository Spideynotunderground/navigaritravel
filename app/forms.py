from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .models import Form

# Translating the choices with gettext_lazy
CITIES = [
    ('U', _('UAE')),
    ('EU', _('Europe')),
    ('T', _('Turkey')),
    ('E', _('Egypt')),
    ('M', _('Maldives')),
    ('TH', _('Thailand')),
]

class TourForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('name', 'surname', 'phone', 'country', 'event_date')
        widgets = {
            'country': forms.Select(choices=CITIES),
            'event_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.now().strftime('%Y-%m-%d'),  # Minimum date is today
                }
            ),
        }
