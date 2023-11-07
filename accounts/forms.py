from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",) #<- add the custom field called name from the CustomUser model we created type=(tuple)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model =  CustomUser
        fields = UserChangeForm.Meta.fields #<- UserChangeForm already includes all the fields from the model used