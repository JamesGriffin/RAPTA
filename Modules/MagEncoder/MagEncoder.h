/*
* Based on code by RobinL and Linarism.
* https://forum.arduino.cc/index.php?topic=164353.0
*/

#ifndef RAPTA_MAGENCODER_H
#define RAPTA_MAGENCODER_H

#include <Arduino.h>

class MagEncoder {
public:
    MagEncoder();

    MagEncoder(uint8_t chipSelect, uint8_t clock, uint8_t data);

    MagEncoder(uint8_t chipSelect, uint8_t clock, uint8_t data, float offset);

    unsigned int getRawData();

    float getAngle();

    void resetOffset();

protected:
    float offset;

private:
    uint8_t chipSelect;
    uint8_t clock;
    uint8_t data;
};

#endif //RAPTA_MAGENCODER_H
