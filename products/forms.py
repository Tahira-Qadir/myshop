from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, label="Full Name", max_length= 20, error_messages={"required":"You forgot to add your name", "max_length":"This is name is too long , make it shorter"})
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=300)
