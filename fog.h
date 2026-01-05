pragma once

inline float fog_factor(float dist) {
    const float fog_start = 3.0f;
    const float fog_end   = 16.0f;

    if (dist < fog_start) return 0.0f;
    if (dist > fog_end)   return 1.0f;

    return (dist - fog_start) / (fog_end - fog_start);
}