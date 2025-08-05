#include "udp_server.h"
#include "wizchip_conf.h"
#include "socket.h"
#include <stdio.h>
#include <string.h>

// Example MAC/IP
static uint8_t mac[6]  = {0x00, 0x08, 0xdc, 0xab, 0xcd, 0xef};
static uint8_t ip[4]   = {192, 168, 1, 123};
static uint8_t gw[4]   = {192, 168, 1, 1};
static uint8_t mask[4] = {255, 255, 255, 0};

#define LISTEN_PORT 5000
#define BUF_SIZE 2048

static uint8_t rx_buf[BUF_SIZE];

void ethernet_init() {
    uint8_t tmp;
    wizchip_conf wizConf = {
        .phy_conf = PHY_CONFBY_SW,
    };

    // SPI and W5500 init happens elsewhere (stubbed here)
    // Assume SPI already initialized

    wizchip_init(NULL, NULL);  // Buffers assigned internally
    wizphy_setphyconf(&wizConf);
    ctlnetwork(CN_SET_MAC, mac);
    ctlnetwork(CN_SET_IP, ip);
    ctlnetwork(CN_SET_GW, gw);
    ctlnetwork(CN_SET_NETMASK, mask);

    printf("Ethernet initialized with IP: %d.%d.%d.%d\n", ip[0], ip[1], ip[2], ip[3]);

    socket(0, Sn_MR_UDP, LISTEN_PORT, 0);
}

void udp_server_poll() {
    int len, sender_len;
    uint8_t sender_ip[4];
    uint16_t sender_port;

    len = recvfrom(0, rx_buf, BUF_SIZE, sender_ip, &sender_port);
    if (len > 0) {
        printf("Received %d bytes from %d.%d.%d.%d:%d\n",
               len, sender_ip[0], sender_ip[1], sender_ip[2], sender_ip[3], sender_port);

        // Echo back the received data
        sendto(0, rx_buf, len, sender_ip, sender_port);
    }
}
