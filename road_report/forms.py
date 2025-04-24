from django import forms
from .models import RoadReport

class RoadReportForm(forms.ModelForm):
    class Meta:
        model = RoadReport
        fields = [
            'location_type',
            'latitude', 'longitude',
            'location_url',
            'street', 'city', 'state', 'country',
            'condition', 'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        location_type = cleaned_data.get('location_type')
        if location_type == 'coordinates':
            if not cleaned_data.get('latitude') or not cleaned_data.get('longitude'):
                raise forms.ValidationError('Please provide both latitude and longitude.')
        elif location_type == 'url':
            if not cleaned_data.get('location_url'):
                raise forms.ValidationError('Please provide a location URL.')
        elif location_type == 'manual':
            if not (cleaned_data.get('street') and cleaned_data.get('city') and cleaned_data.get('state') and cleaned_data.get('country')):
                raise forms.ValidationError('Please provide street, city, state, and country for manual location.')
        return cleaned_data
