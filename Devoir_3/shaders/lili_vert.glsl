#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texCoords;

out vec2 fragTex;

uniform vec2 offset;

void main()
{
    gl_Position = vec4(position.xy + offset, position.z, 1.0);
    fragTex = texCoords;
}

