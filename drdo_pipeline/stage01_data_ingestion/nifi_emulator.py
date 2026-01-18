# DRDO Stage 1 – Data Ingestion
# Tool: Apache NiFi (Emulated)
# Multi-rate, flow-based ingestion controller

import time
from .sensor_emulator import FighterAircraftSensorEmulator
from .baseline_buffer import BaselineBuffer
from .special_event_buffer import SpecialEventBuffer
from .audio_stub import AudioDataStub



class NiFiEmulator:
    """
    Emulates Apache NiFi flow with MIL-STD timing guarantees
    """

    def __init__(self):
        self.sensor = FighterAircraftSensorEmulator()
        self.baseline = BaselineBuffer()
        self.events = SpecialEventBuffer()
        self.audio = AudioDataStub()

        # Highest required rate = 8 Hz (125 ms)
        self.base_period_sec = 0.125

    def run_once(self):
        sensor_frame = self.sensor.read_sensors()

        if len(sensor_frame) > 1:
            self.baseline.capture(sensor_frame)
            self.events.check_and_store(sensor_frame)

            return {
                "sensor_data": sensor_frame,
                "baseline": self.baseline.get(),
                "special_events": self.events.get_events(),
                "audio": self.audio.read_audio_frame()
            }

        return None

    def run(self, cycles=50):
        outputs = []
        for _ in range(cycles):
            result = self.run_once()
            if result:
                outputs.append(result)
            time.sleep(self.base_period_sec)
        return outputs
