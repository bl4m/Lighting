from ursina import *
from material import Material
from entity import cEntity
from light import Light as myLight


app = Ursina()

shader = Shader.load(Shader.GLSL,'shaders/vertex.vert','shaders/fragment.frag')
light = myLight(x=2)
light.setShader(shader)
material1 = Material()

material1.color = color.red
material1.diffuse = Vec3(0.7*0.7*0.7)
material1.shininess = 16
sphere = cEntity(model='sphere')
sphere.shader = shader
sphere.set_material(material1)

material2 = Material()
material2.texture = load_texture('textures/container')
material2.specular_map = load_texture('textures/container_specular')
cube = cEntity(model='cube',z=2)
cube.shader = shader
cube.set_material(material2)

light.update_values()
EditorCamera()
app.run()