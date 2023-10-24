#version 430

uniform mat4 p3d_ViewMatrix;

in vertex_data {
    vec2 uv;
    vec3 normal;
    vec3 FragPos;
    vec3 lightPos;
} data;

struct Material{
    vec4 color;
    vec3 specular;
    vec3 diffuse;
    sampler2D texture;
    sampler2D specular_map;
    int shininess;
};

uniform Material material;

struct Light{
    vec3 direction;
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
};

uniform Light light;


out vec4 color;

void main() {

    vec3 ambient = light.ambient * vec3(texture(material.texture, data.uv)) * normalize(material.color.xyz);

    vec3 norm = normalize(data.normal);
    vec3 lightDir = -normalize(vec3(mat3(p3d_ViewMatrix) * light.direction));
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = light.diffuse * material.diffuse * diff * vec3(texture(material.texture, data.uv)) * normalize(material.color.xyz);

    vec3 viewDir = normalize(- data.FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
    vec3 specular = light.specular * material.specular * spec * vec3(texture(material.specular_map, data.uv)) * normalize(material.color.xyz);

    vec3 result = ambient + diffuse + specular;

    color = vec4(result, 1.0);

}
