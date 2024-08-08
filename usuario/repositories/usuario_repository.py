from typing import List
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Usuario_Repository:
    def get_all(self)->List[User]:
        return User.objects.all()
        
    def delete(self, usuario: User):
        usuario.delete()
    
    def get_by_id(self, id:int) -> User.objects:
        return User.objects.get(id=id)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError("El email ya se encuetra registrado")
        return email
    
    def update(self,
        usuario: User,
        username:str, 
        first_name:str,
        last_name:str, 
        email:str, 
        password: str
        ) -> User.objects:
        usuario.username = username
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.set_password(password)
        usuario.save()
        
        