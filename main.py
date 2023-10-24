from ursina import *
from material import Material
from entity import cEntity
from light import DirectionalLight,Light,PointLight,SpotLight


app = Ursina()
#change the fragment shader according to the light used
shader = Shader.load(Shader.GLSL,'shaders/vertex.vert','shaders/DirectionalFragment.frag')
light = DirectionalLight(y=3,x=2)
light.setShader(shader)
material1 = Material()

material1.color = color.red
material1.diffuse = Vec3(0.7,0.7,0.7)
material1.shininess = 128
sphere = cEntity(model='cube')
sphere.shader = shader
sphere.set_material(material1)

material2 = Material()
material2.texture = load_texture('textures/container')
material2.specular_map = load_texture('textures/container_specular')
cube = cEntity(model='cube',z=2)
cube.shader = shader
cube.set_material(material2)

material3 = Material()
material3.color = rgb(200,200,50,255)
flore = cEntity(model='quad',y=-2,rotation_x=90,scale=100)
flore.shader = shader
flore.set_material(material3)

light.update_values()
EditorCamera()
app.run()
