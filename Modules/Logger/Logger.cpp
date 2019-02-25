//
// Created by Elijah on 14/02/2017.
//

#include "Logger.h"

/**
 * Initializes Logger object.
 * @param sdChipSelect The SD chipSelect value, 10 for an UNO.
 */
Logger::Logger(int sdChipSelect) {
    bytesWritten = 0;
    lastFlushed = 0;
    SD.begin(sdChipSelect);
    String logName = getNextName();
    Serial.println("Logging to: " + logName + ".LOG");
    logFile = SD.open("/logs/" + logName + ".log", O_CREAT | O_WRITE);
}

/**
 * Allows for creation of a Logger variable without initialization.
 */
Logger::Logger() {};

/**
 * Prepares data for logging and writes to an SD card when buffer is full.
 * Use this for event based logging rather than data logging.
 *
 * @param tag The name of the module calling the function.
 * @param data The data to be logged.
 */
void Logger::log(String tag, String data) {
    String logLine = "[" + parseMillis(millis()) + "][" + tag + "] " + data;
    log(logLine);
}

/**
 * Writes to an SD card when buffer is full.
 * @param logLine The string to be written.
 */
void Logger::log(String logLine) {
    checkFlush(logLine.length());
    logFile.println(logLine);
    bytesWritten += logLine.length();
}

/**
 * Checks if the SD buffer needs to be flushed, and flushes it.
 */
void Logger::checkFlush(uint16_t logLineLength) {
    if (bytesWritten + logLineLength > 512 || millis() - lastFlushed > 3000) {
        logFile.flush();
        bytesWritten = 0;
        lastFlushed = millis();
    }
}

void Logger::checkFlush() {
    if (millis() - lastFlushed > 3000) {
        logFile.flush();
        bytesWritten = 0;
        lastFlushed = millis();
    }
}

/**
 * Parses the given millis into a human-readable format.
 * @param millis The millis to be parsed. e.g. millis()
 * @return String with the format [mm:ss.ss]. e.g. [01:32.11]
 */
String Logger::parseMillis(uint32_t millis) {
    uint8_t mins = floor(millis / 60000);
    String sMins;
    if (mins < 10) {
        sMins = "0" + String(mins);
    } else {
        sMins = String(mins);
    }
    uint8_t secs = floor(millis % 60000) / 1000;
    String sSecs;
    if (secs < 10) {
        sSecs = "0" + String(secs);
    } else {
        sSecs = String(secs);
    }
    uint8_t decimalSecs = floor(millis % 1000) / 10;
    String sDecimalSecs;
    if (decimalSecs < 10) {
        sDecimalSecs = "0" + String(decimalSecs);
    } else {
        sDecimalSecs = String(decimalSecs);
    }
    return sMins + ":" + sSecs + "." + sDecimalSecs;
}

/**
 * Gets the next log file name in directory logDir.
 * @return Log file name. e.g. "FLIGHT9"
 */
String Logger::getNextName() {
    File dir = SD.open(F("/LOGS/"));
    if (!dir) {
        if (SD.mkdir(F("LOGS"))) {
            dir = SD.open(F("/LOGS/"));
        } else {
            Serial.println(F("FAILED TO CREATE /LOGS/ DIRECTORY"));
        }
    }
    int maxFlightN = 0;
    while (true) {
        File file = dir.openNextFile();
        if (!file) {
            // No more files
            break;
        }
        String name = file.name();
        int len = name.length();
        if (name.substring(len - 3, len) == F("LOG")) {
            name.replace(F("FLIGHT"), F(""));
            name.replace(F(".LOG"), F(""));
            int flightN = name.toInt();
            if (flightN > maxFlightN) {
                maxFlightN = flightN;
            }
        }
    }
    return "FLIGHT" + String(maxFlightN + 1);
}