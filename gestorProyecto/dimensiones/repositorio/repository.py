from repositorio.repository_interface import DimensionRepositoryI

class DimensionRepository(DimensionRepositoryI):
    
    def create_dimensions(self):
        return super().create_dimensions()
    
    def get_dimensions(self):
        return super().get_dimensions()
    
    def update_dimensions(self, id):
        return super().update_dimensions(id)
    
    def delete_dimensions(self, id):
        return super().delete_dimensions(id)