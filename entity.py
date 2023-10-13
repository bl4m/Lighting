from ursina import Entity,Shader
from material import Material

class cEntity(Entity):
    def __init__(self,**kwargs):
        self.shader = Shader.load(Shader.GLSL,'shaders/vertex.vert','shaders/fragment.frag')
        self.material = Material()
        super().__init__(**kwargs)
        self.update_params()
    def set_material(self,material):
        self.material = material
        self.update_params()
    def update_params(self):
        self.set_shader_input("material.color",self.material.color)
        self.set_shader_input("material.texture",self.material.texture)
        self.set_shader_input("material.specular_map",self.material.specular_map)
        self.set_shader_input("material.shininess",self.material.shininess)
        self.set_shader_input("material.diffuse",self.material.diffuse)
        self.set_shader_input("material.specular",self.material.specular)