#version 330 core

in vec2 fragTex;
out vec4 fragColor;

uniform sampler2D texture1;
uniform float time;

void main()
{
    float alpha = (sin(time) + 1.0) / 2.0; // oscille entre 0 et 1
    vec3 color = mix(vec3(0.0, 0.0, 1.0), vec3(1.0, 0.0, 0.0), alpha); // bleu -> rouge

    vec4 texColor = texture(texture1, fragTex);
    fragColor = vec4(texColor.rgb * color, texColor.a);
}
