include "lua.h"
include "lualib.h"
include "lauxlib.h"

lua_State* L;

void lua_init() {
    L = luaL_newstate();
    luaL_openlibs(L);
}
void lua_run(const char* file) {
    if (luaL_dofile(L, file)) {
        printf("Lua error: %s\n", lua_tostring(L, -1));
    }
}
int lua_move_player(lua_State* L) {
    float dx = lua_tonumber(L, 1);
    float dz = lua_tonumber(L, 2);

    player.x += dx;
    player.z += dz;
    return 0;
}
