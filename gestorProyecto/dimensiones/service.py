from repositorio.repository_interface import DimensionRepositoryI
from repositorio.repository import DimensionRepository

class DimensionService:
   def __init__(self, repository: DimensionRepositoryI):
      self.repository = repository
  
   def get_dimensions(self):
       self.repository.get_dimensions


dimension_service = DimensionService(DimensionRepository)