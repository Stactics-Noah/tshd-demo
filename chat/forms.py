from django import forms

class ChatForm(forms.Form):
    """
    Single textbox for the user’s message.
    """
    message = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Type your message and press Enter",
            "autocomplete": "off",
        })
    )
