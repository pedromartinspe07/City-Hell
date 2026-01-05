#pragma once

void platform_init();
void platform_shutdown();
float platform_time();
void platform_log(const char* msg);
// ios.mm
#include "platform.h"
#include <Foundation/Foundation.h>

float platform_time() {
    return CACurrentMediaTime();
}

void platform_log(const char* msg) {
    NSLog(@"%s", msg);
}
// 3ds.c
#include "platform.h"
#include <stdio.h>

float platform_time() {
    return osGetTime() / 1000.0f;
}

void platform_log(const char* msg) {
    printf("%s\n", msg);
}