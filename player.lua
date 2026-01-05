function update(dt)
    if input.forward then
        move_player(0.0, dt * 2.0)
    end
end
void game_update(float dt) {
    lua_getglobal(L, "update");
    lua_pushnumber(L, dt);
    lua_pcall(L, 1, 0, 0);
}
local world = require("openmw.world")

local fog = 0.02

return {
    engineHandlers = {
        onUpdate = function(dt)
            fog = math.min(0.08, fog + dt * 0.001)
            world.setFogDensity(fog)
        end
    }
}