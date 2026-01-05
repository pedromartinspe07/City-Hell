#include <metal_stdlib>
using namespace metal;

struct VertexOut {
    float4 position [[position]];
    float fog;
};

vertex VertexOut vertex_main(uint id [[vertex_id]]) {
    float2 pos[3] = {
        float2(-0.5, -0.5),
        float2( 0.5, -0.5),
        float2( 0.0,  0.5)
    };

    VertexOut out;
    out.position = float4(pos[id], 0.0, 1.0);
    out.fog = length(pos[id]);
    return out;
}

fragment float4 fragment_main(VertexOut in [[stage_in]]) {
    float fogFactor = clamp(in.fog, 0.0, 1.0);
    float3 color = mix(float3(0.6,0.6,0.6), float3(0.2,0.2,0.2), fogFactor);
    return float4(color, 1.0);
}