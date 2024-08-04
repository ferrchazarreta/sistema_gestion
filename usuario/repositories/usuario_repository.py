from typing import List
from django.contrib.auth.models import User

class Usuario_Repository:
    def get_all(self)->List[User]:
        return User.objects.all()
    def create(
        self, 
        username:str, 
        email:str, 
        password:str, 
        first_name:str,
        last_name:str,
        ) -> User.objects:
        return User.objects.create(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name)
        
    def delete(self, usuario: User):
        usuario.delete()
        
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
        usuario.password = password
        usuario.save()
    
    def get_by_id(self, id:int) -> User.objects:
        return User.objects.get(id=id)
    
    