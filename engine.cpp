include "engine.h"
include <stdio.h>

static float time_acc = 0.0f;

void engine_init() {
    printf("Engine init\n");
}

void engine_update(float dt) {
    time_acc += dt;
}

void engine_render() {
    // Render será chamado pelo Metal
}

void engine_shutdown() {
    printf("Engine shutdown\n");
}