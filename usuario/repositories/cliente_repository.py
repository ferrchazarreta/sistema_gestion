from typing import List
from django.contrib.auth.models import User
from usuario.models import Cliente

class Cliente_Repository:
    def get_all(self)->List[Cliente]:
        return Cliente.objects.all()
    def create(
        self, 
        user:User,
        address:str,
        phone:int
        ) -> Cliente.objects:
        return Cliente.objects.create(
            user=user, 
            address=address, 
            phone=phone)
    def delete(self, cliente: Cliente):
        cliente.delete()
        
    def update(self,
               cliente: Cliente,
               address: str,
               phone: int ) -> Cliente.objects:
        cliente.address = address
        cliente.phone = phone
        cliente.save()
    
    def get_by_id(self, id:int) -> Cliente.objects:
        return Cliente.objects.get(id=id)
    
    