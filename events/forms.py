from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "start_time",
            "end_time",
        ]
    def clean(self):
        cleaned_data = super().clean()

        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and end_time<=start_time:
            self.add_error(
                    "end_time",
                    "The end time must be after the start time.",
                    )
        return cleaned_data
