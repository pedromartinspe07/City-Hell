include "player.h"
include <math.h>

void player_update(Player& p, float dt, bool forward, bool left, bool right) {
    if (left)  p.angle += 1.8f * dt;
    if (right) p.angle -= 1.8f * dt;

    if (forward) {
        p.x += cosf(p.angle) * dt * 2.0f;
        p.z += sinf(p.angle) * dt * 2.0f;
    }
}