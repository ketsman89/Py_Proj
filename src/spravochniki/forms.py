from django import forms
from . import models
from django.core.exceptions import ValidationError

def if_microsoft(data):
    if data[-14:] != "@microsoft.com":
        raise ValidationError(
            "The adress must be like this **@microsoft.com"
        )



# CHOISES_AUTOR = [(aut.pk, aut.name) for aut in models.Autor.objects.all()]
# CHOISES_GENRE = [(gen.pk, gen.name) for gen in models.Genre.objects.all()]
# CHOISES_SERIE = [(ser.pk, ser.name) for ser in models.Serie.objects.all()]
# CHOISES_PUBLISHER = [(pub.pk, pub.name) for pub in models.Publisher.objects.all()]
# class AddBookForm(forms.Form):    
#     name = forms.CharField(
#         required=True,
#         max_length=255,
#         label="Pls add a name"
#     )
#     autor = forms.ChoiceField(
#         choices=CHOISES_AUTOR, 
#         required=True,
#         label="Pls select an Autor",
#         help_text="help text<"
#     )
#     genre = forms.ChoiceField(
#         choices=CHOISES_GENRE,
#         required=True,
#         label="Pls select a genre",
#         help_text="help text<"
#     )
#     serie = forms.ChoiceField(
#         choices=CHOISES_SERIE,
#         required=True,
#         label="Pls select a serie",
#         help_text="help text<"
#     )
#     publisher = forms.ChoiceField(
#         choices=CHOISES_PUBLISHER,
#         required=True,
#         label="Pls select a publisher",
#         help_text="help text<"
#     )


#     def save(self):
#         autor = models.Autor.objects.get(
#             pk=self.cleaned_data["autor"],        
#         )
#         genre = models.Genre.objects.get(
#             pk=self.cleaned_data["genre"],        
#         )
#         serie = models.Serie.objects.get(
#             pk=self.cleaned_data["serie"],        
#         )
#         publisher = models.Publisher.objects.get(
#             pk=self.cleaned_data["publisher"],        
#         )
#         return models.Book.objects.create(
#             autor=autor, 
#             name=self.cleaned_data["name"],
#             genre=genre,
#             serie=serie,
#             publisher=publisher
#         )
    
class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            "name", "autor", "genre", "serie", "publisher"
        ]



class ContactForm(forms.Form):
    contact_email = forms.EmailField(
        required=True,
        label="Pls enter your email",
        validators=[
            if_microsoft
        ]        
    )
    message = forms.CharField(
        required=True,
        label="Pls enter your message",
        widget=forms.Textarea()
    )

    # def send_email(self):
    #     contact_email=self.cleaned_data["contact_email"]
    #     message=self.cleaned_data["message"]
    #     send_mail(
    #         to,
    #         subject,
    #         html
    #     )