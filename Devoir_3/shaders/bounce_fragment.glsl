#version 330 core

in vec2 fragTex;
out vec4 outColor;

uniform sampler2D texture1;

void main() {
    vec4 texColor = texture(texture1, fragTex);
    if (texColor.a < 0.1) discard;
    outColor = texColor;
}
