from django import forms
from . import models, parser_rari

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('raritet', 'raritet'),
        ('foliant', 'foliant'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'raritet':
            file_raritet = parser_rari.parsing()
            for i in file_raritet:
                models.RaritetParser.objects.create(**i)