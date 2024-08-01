from typing import List
from django.contrib.auth.models import User

class Usuario_Repository:
    def get_all(self)->List[User]:
        return User.objects.all()
    def create(
        self, 
        username:str, 
        email:str, 
        password1:str, 
        password2:str, 
        first_name:str,
        last_name:str,
        ) -> User.objects:
        return User.objects.create(
            username = username,
            email = email,
            password1 = password1,
            password2 = password2,
            first_name = first_name,
            last_name = last_name)
        
    def delete(self, usuario: User):
        usuario.delete()
        
    def update(self,
        usuario: User,
        username:str, 
        email:str, 
        first_name:str,
        last_name:str, ) -> User.objects:
        usuario.username = username
        usuario.email = email
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.save()
    
    def get_by_id(self, id:int) -> User.objects:
        return User.objects.get(id=id)
    
    