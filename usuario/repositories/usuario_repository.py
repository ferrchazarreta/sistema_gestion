from typing import List
from django.contrib.auth.models import User

class Usuario_Repository:
    def get_all(self)->List[User]:
        return User.objects.all()
        
    def delete(self, usuario: User):
        usuario.delete()
    
    def get_by_id(self, id:int) -> User.objects:
        return User.objects.get(id=id)
    
    