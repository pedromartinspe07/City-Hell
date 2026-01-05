Player player;
Camera camera;

void game_init() {
    player = {0, 0, 0};
    camera = {6, 4, -8};
}

void game_update(float dt) {
    player_update(player, dt, forward, left, right);
}