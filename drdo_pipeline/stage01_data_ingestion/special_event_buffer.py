# DRDO Stage 1 – Data Ingestion
# MIL-STD-2124A §3.8 Special Event Data

class SpecialEventBuffer:
    def __init__(self):
        self.events = []

    def check_and_store(self, sensor_frame):
        if "accel_vertical_g" in sensor_frame and abs(sensor_frame["accel_vertical_g"]) > 9:
            self.events.append({
                "type": "OVER_G_EVENT",
                "data": sensor_frame
            })

        if "exhaust_gas_temp_c" in sensor_frame and sensor_frame["exhaust_gas_temp_c"] > 850:
            self.events.append({
                "type": "ENGINE_OVERHEAT",
                "data": sensor_frame
            })

    def get_events(self):
        return self.events
