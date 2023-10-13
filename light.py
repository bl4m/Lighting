from ursina import *
 
class Light(Entity):
    def __init__(self,**kwargs):
        super().__init__(
            model='quad',
            texture='default/light',
            double_sided=True,
            **kwargs
        )
        self.ambient = Vec3(0.1,0.1,0.1)
        self.diffuse = Vec3(0.7,0.7,0.7)
        self.specular = Vec3(0.7,0.7,0.7)
        self._shader = None
    def setShader(self,shader):
        for entity in scene.entities:
            if entity.shader == shader:
                entity.set_shader_input("light.specular",self.specular)
                entity.set_shader_input("light.diffuse",self.diffuse)
                entity.set_shader_input("light.ambient",self.ambient)
                entity.set_shader_input("lightPos",self.position)
        self._shader = shader
    def update(self):
        for entity in scene.entities:
            if entity.shader == self.shader:
                self.set_shader_input("lightPos",self.position)
    def update_values(self):
        for entity in scene.entities:
            if entity.shader == self._shader:
                entity.set_shader_input("light.specular",self.specular)
                entity.set_shader_input("light.diffuse",self.diffuse)
                entity.set_shader_input("light.ambient",self.ambient)
                entity.set_shader_input("lightPos",self.position)