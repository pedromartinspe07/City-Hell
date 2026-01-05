struct Player {
    float x, z;
    float rot;
};

void player_update(Player* p, float dt) {
    p->x += 0.5f * dt;
}
struct Camera {
    float x, y, z;
    float targetX, targetY, targetZ;
};

void camera_set(Camera* c, float x, float y, float z) {
    c->x = x;
    c->y = y;
    c->z = z;
}