#ifndef SPI_DRIVER_H
#define SPI_DRIVER_H

#include <stdint.h>

uint8_t spi_read_byte();
void spi_write_byte(uint8_t data);

#endif
