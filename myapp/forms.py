from django import forms
from .models import IpExterno


class TestePortaForm(forms.ModelForm):
    class Meta:
        model = IpExterno
        fields = '__all__'
        widgets = {
            'ip': forms.TextInput(attrs={'placeholder': 'IP Extero'}),
            'porta': forms.TextInput(attrs={'placeholder': 'Porta'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ip'].widget.attrs.update({'class': 'ip-address'})
        self.fields['porta'].widget.attrs.update({'class': 'porta'})

