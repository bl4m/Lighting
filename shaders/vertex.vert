#version 430

uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewMatrix;
uniform vec3 lightPos;
uniform mat4 p3d_ViewMatrix;

in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;
in vec3 p3d_Normal;
out vec2 uv;

out vertex_data {
    vec2 uv;
    vec3 normal;
    vec3 FragPos;
    vec3 lightPos;
} data;

void main() {

    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
    uv = p3d_MultiTexCoord0;
    data.uv = p3d_MultiTexCoord0;
    data.FragPos = vec3(p3d_ModelViewMatrix * p3d_Vertex);
    data.normal = mat3(transpose(inverse(p3d_ModelViewMatrix))) * p3d_Normal;
    data.lightPos = vec3(p3d_ViewMatrix * vec4(lightPos, 1.0));
}