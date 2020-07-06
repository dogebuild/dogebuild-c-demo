#include <stdio.h>

void writeHello(const char* whom, char* buf, int bufSize) {
    snprintf(buf, bufSize, "Hello %s!\n", whom);
}
