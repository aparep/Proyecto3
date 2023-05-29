from django import forms
from . import models

class TareaForm(forms.ModelForm):
    class Meta:
        model = models.Tarea
        fields = "__all__"

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = models.Responsable
        fields = "__all__"


class LocalForm(forms.ModelForm):
    class Meta:
        model = models.Local
        fields = "__all__"