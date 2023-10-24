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
        self._shader = shader
        self.update_values()
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

class DirectionalLight(Entity):
    def __init__(self,**kwargs):
        super().__init__(
            model='quad',
            texture='default/light',
            double_sided=True,
            **kwargs
        )
        self.ambient = Vec3(0.1,0.1,0.1)
        self.diffuse = Vec3(0.7,0.7,0.7)
        self.direction = Vec3(-1,-1,-1)
        self.specular = Vec3(0.7,0.7,0.7)
        self._shader = None
        self.look_at(-self.position+self.direction)
    def setShader(self,shader):
        self._shader = shader
        self.update_values()
        
    def update(self):
        for entity in scene.entities:
            if entity.shader == self.shader:
                entity.set_shader_input("light.direction",self.direction)
                entity.set_shader_input("lightPos",self.position)
    def update_values(self):
        for entity in scene.entities:
            if entity.shader == self._shader:
                entity.set_shader_input("light.specular",self.specular)
                entity.set_shader_input("light.diffuse",self.diffuse)
                entity.set_shader_input("light.ambient",self.ambient)
                entity.set_shader_input("lightPos",self.position)
                entity.set_shader_input("light.direction",self.direction)

class PointLight(Entity):
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
        self.constant = 1.0
        self.linear = 0.09
        self.quadratic = 0.032
        self._shader = None
    def setShader(self,shader):
        self._shader = shader
        self.update_values()
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
                entity.set_shader_input("light.constant",self.constant)
                entity.set_shader_input("light.linear",self.linear)
                entity.set_shader_input("light.quadratic",self.quadratic)
                entity.set_shader_input("lightPos",self.position)

class SpotLight(Entity):
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
        self.innerCutOff = cos(math.radians(12.5))
        self.outerCutOff = cos(math.radians(17.5))
        self.direction = Vec3(-0.5,-1,0)
        self._shader = None
    def setShader(self,shader):
        self._shader = shader
        self.update_values()
    def update(self):
        for entity in scene.entities:
            if entity.shader == self.shader:
                self.set_shader_input("lightPos",self.position)
                entity.set_shader_input("light.direction",self.direction)
    def update_values(self):
        for entity in scene.entities:
            if entity.shader == self._shader:
                entity.set_shader_input("light.specular",self.specular)
                entity.set_shader_input("light.diffuse",self.diffuse)
                entity.set_shader_input("light.ambient",self.ambient)
                entity.set_shader_input("lightPos",self.position)
                entity.set_shader_input("light.direction",self.direction)
                entity.set_shader_input("light.innerCutOff",self.innerCutOff)
                entity.set_shader_input("light.outerCutOff",self.outerCutOff)
