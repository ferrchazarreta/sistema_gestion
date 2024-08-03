from typing import (
    List,
    Optional,
)

from noticias.models import (
  News,
  Category,
)

#logger = logging.getLogger(__name__)

class NewRepository:
  def create(
    self,
    title: str,
    short_description: str,
    long_description: str,
    category: Category,
    created_at: int, 
    image: str,
    ) -> News.objects:
    
    return News.objects.create(
      title = title,
      short_description = short_description,
      long_description = long_description,
      category = category,
      created_at = created_at,
      image = image,
    )
  
  def update(self,
            noticia: News,
            title: str,
            short_description: str,
            long_description: str,
            category: Category,
            image: str,            
            ) -> None:
    noticia.category = category
    noticia.title = title
    noticia.short_description = short_description
    noticia.long_description = long_description
    # Solo actualiza la imagen si se ha proporcionado una nueva
    if image:
      noticia.image = image
        
    noticia.save()

  def get_all(self) -> List[News]:
    return News.objects.all()
  
  def filter_by_id(self, noticia_id,) -> Optional[News]:
    return News.objects.filter(id=noticia_id).first()
  
  def get_by_id(self, id: int,) -> Optional[News]:
    try:
      noticia = News.objects.get(id=id)
    except:
      noticia = None
    return noticia
  
  def filter_by_category(
    self,
    category = Category,
  ) -> List[News]:
    return News.objects.filter(category = category)

  def delete(self, noticia: News):
      noticia.delete()