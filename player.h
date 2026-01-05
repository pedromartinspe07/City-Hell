pragma once

struct Player {
    float x, z;
    float angle;
};

void player_update(Player& p, float dt, bool forward, bool left, bool right);