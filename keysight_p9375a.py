#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2024 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import logging

from pymeasure.instruments import Channel, Instrument
from pymeasure.instruments.generic_types import SCPIMixin
from pymeasure.instruments.validators import strict_range, strict_discrete_set, strict_discrete_range

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class KeysightP9375A_Channels(Channel):
    """
    Channel implimentation for the Keysight P9375A VNA
    """

    scan_points = Instrument.control(
        "SENS{ch}:SWE:POIN?",
        "SENS{ch}:SWE:POIN %d",
        """
        Number of frequency points measured per sweep (int).
        """,
        cast=int,
    )




class KeysightP9375A(SCPIMixin, Instrument):
    """
    Minimum viable code to perform TDR Measurement
    """

    def __init__(self, adapter, name="VNA", **kwargs):
        super().__init__(adapter, name, **kwargs)
        self.reset()


    channels = Insturment.MultiChannelCreator(KeysightP9375A_Channels, [1])

    # Get / Set RF Power
    # SOURce<cnum>:POWer<port>[:LEVel][:IMMediate][:AMPLitude] <num>, [src]
    

    # Get / Set IFBW
    IFBW = Instrument.control(
        "SENS1:BAND?",
        "SENS1:BAND %d",
        """
        Number of frequency points measured per sweep (int).
        """,
        cast=float,
    )

    # sweep time

    # Get / Set Averaging Count
    # SENSe<cnum>:AVERage:COUNt <num>
    averaging_count = Instrument.control(
        "SENS1:AVER:COUN?",
        "SENS1:AVER:COUN %d",
        """
        Number of averages (int).
        """,
        cast=int,
    )

    # Get / Set Averaging Enabled
    # SENSe<cnum>:AVERage[:STATe] <ON | OFF>
    averaging_enabled = Instrument.control(
        "SENS1:AVER:STAT?",
        "SENS1:AVER:STAT %d",
        """
        Averaging enabled state (bool).
        """,
        cast=bool,
    )

    # SENSe<cnum>:AVERage:MODE <char>
    averaging_mode = Instrument.control(
        "SENS1:AVER:MODE?",
        "SENS1:AVER:MODE %s",
        """
        Averaging mode to be used (str).
        """,
        cast=str,
    )

    # Get / Set Start and Stop Frequency
    # SENSe<cnum>:FREQuency:STARt <num>

    # Get / Set Measurement Dwell time
    # SENSe<cnum>:SWEep:DWELl <num>
    dwell_time = Instrument.control(
        "SENS1:SWE:DWELL?",
        "SENS1:SWE:DWELL %d",
        """
        Dwell time per point measurement (float).
        """,
        cast=float,
    )

    # Get S-Parameter Array
    # CALCulate<cnum>:DATA:SNP:PORTs? <"x,y,z".>[, FAST]
    # better CALCulate<cnum>:MEASure<mnum>:DATA:RAW <string>,<dataBlock>

    # Correction state
    # SENSe<cnum>:CORRection[:STATe] <ON | OFF>
    correction_enabled = Instrument.control(
        "SENS1:CORR:STAT?",
        "SENS1:CORR:STAT %d",
        """
        Correction enabled state (bool).
        """,
        cast=bool,
    )

    pass
