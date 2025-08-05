cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)

project(modular_motor_firmware C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_executable(modular_motor_firmware
    main.c
    udp_server.c
    spi_driver.c
)

target_include_directories(modular_motor_firmware PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}
    wiznet/ioLibrary/Ethernet
)

target_link_libraries(modular_motor_firmware pico_stdlib)

pico_add_extra_outputs(modular_motor_firmware)
