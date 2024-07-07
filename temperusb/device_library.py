# encoding: utf-8
#
# TEMPer USB temperature/humidty sensor device driver settings.
# Handles devices reporting themselves as USB VID/PID 0C45:7401 (mine also says
# RDing TEMPerV1.2).
#
# Copyright 2012-2020 Philipp Adelt <info@philipp.adelt.net> and contributors.
#
# This code is licensed under the GNU public license (GPL). See LICENSE.md for
# details.

from enum import Enum

class TemperType(Enum):
    FM75 = 0
    SI7021 = 1

class TemperConfig:
    def __init__(
        self,
        temp_sens_offsets: list,
        hum_sens_offsets: list = None,
        type: TemperType = TemperType.FM75,
    ):
        self.temp_sens_offsets = temp_sens_offsets
        self.hum_sens_offsets = hum_sens_offsets
        self.type = type


DEVICE_LIBRARY = {
    "TEMPer2V1.3": TemperConfig(
        temp_sens_offsets=[2, 4],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPerV1.2": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPerV1.4": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPer1F_V1.3": TemperConfig(
        # Has only 1 sensor at offset 4
        temp_sens_offsets=[4],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPERHUM1V1.2": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=[4],
        type=TemperType.SI7021,
    ),
    "TEMPERHUM1V1.3": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=[4],
        type=TemperType.SI7021,
    ),
    "TEMPerHumiV1.0": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=[4],
        type=TemperType.FM75,
    ),
    "TEMPerHumiV1.1": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=[4],
        type=TemperType.FM75,
    ),
    "TEMPer1F_H1_V1.4": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=[4],
        type=TemperType.FM75,
    ),
    "TEMPerNTC1.O": TemperConfig(
        temp_sens_offsets=[2, 4, 6],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPer1V1.4": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPer2_V3.7": TemperConfig(
        temp_sens_offsets=[2, 10],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPer2V1.4": TemperConfig(
        temp_sens_offsets=[2],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    "TEMPer2": TemperConfig(
        temp_sens_offsets=[2, 10],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
    # idVendor           0x3553 
    # idProduct          0xa001 
    # iManufacturer      1 PCsensor
    # iProduct           2 TEMPer2
    #
    # Output samples (behind '## '):
    #
    ## www.pcsensor.com
    ## temper2 v4.1
    ## caps lock:on/off/++
    ## num lock:off/on/-- 
    ## type:inner-tx;outer-tx
    ## inner-temp	outer-temp	interval
    ## 34.06 [c]	25.56 [c]	1s
    ##
    ## $ sudo temper --verbose
    ## Firmware query: b'0186ff0100000000'
    ## Firmware value: b'54454d506572325f56342e3100000000' TEMPer2_V4.1
    ## Data value: b'80800b544e200000800109ca4e200000'
    ## Converted value: b'09ca'
    ## Bus 003 Dev 002 3553:a001 TEMPer2_V4.1 29.00C 84.20F - 25.06C 77.11F -

    # The config used if the sensor type is not recognised.
    # If your sensor is working but showing as unrecognised, please
    # add a new entry above based on "generic_fm75" below, and submit 
    # a PR to https://github.com/padelt/temper-python/pulls
    "generic_fm75": TemperConfig(
        temp_sens_offsets=[2, 4],
        hum_sens_offsets=None,
        type=TemperType.FM75,
    ),
}
