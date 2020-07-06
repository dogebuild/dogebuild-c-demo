#include <stdio.h>

#include "helloworlder.h"

int main() {
    char buf[1024];
    writeHello("World", buf, sizeof(buf));
    printf(buf);
    return 0;
}
