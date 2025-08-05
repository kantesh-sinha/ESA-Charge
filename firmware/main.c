#include "udp_server.h"
#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_init_all(); // UART output
    printf("Starting Modular Motor Control Firmware...\n");

    // Initialize Ethernet (W5500 via SPI)
    ethernet_init();

    // Start listening for UDP commands
    while (true) {
        udp_server_poll(); // receive + respond to packets
        sleep_ms(10);
    }

    return 0;
}
