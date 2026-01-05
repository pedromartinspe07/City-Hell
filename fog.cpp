fogFactor = clamp(in.fog, 0.0, 1.0);
mix(color, fogColor, fogFactor);
float fog_factor(float dist) {
    const float fog_start = 5.0f;
    const float fog_end   = 25.0f;

    if (dist < fog_start) return 0.0f;
    if (dist > fog_end)   return 1.0f;

    return (dist - fog_start) / (fog_end - fog_start);
}