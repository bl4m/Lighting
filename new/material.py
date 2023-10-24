from ursina import *

class Material:
    def __init__(self):
        self.texture = load_texture('default_texture')
        self.specular_map = load_texture('default_texture')
        self.color = Vec3(1,1,1)
        self.diffuse = Vec3(1,1,1)
        self.specular = Vec3(1,1,1)
        self.shininess = 16