# DRDO Stage 8 – Streaming / Real-Time Processing
# Tool: Apache Kafka (Emulated)
# Responsibility: Publish / Subscribe semantics only

from collections import deque
from .stream_topics import FLIGHT_SENSOR_TOPIC, ANOMALY_SCORE_TOPIC


class KafkaTopic:
    """
    Represents a Kafka topic with ordered messages
    """

    def __init__(self, name):
        self.name = name
        self.queue = deque()

    def publish(self, message):
        self.queue.append(message)

    def consume(self):
        if self.queue:
            return self.queue.popleft()
        return None


class KafkaEmulator:
    """
    Emulates a Kafka broker
    """

    def __init__(self):
        self.topics = {
            FLIGHT_SENSOR_TOPIC: KafkaTopic(FLIGHT_SENSOR_TOPIC),
            ANOMALY_SCORE_TOPIC: KafkaTopic(ANOMALY_SCORE_TOPIC),
        }

    def publish(self, topic_name, message):
        if topic_name not in self.topics:
            raise ValueError(f"Unknown topic: {topic_name}")
        self.topics[topic_name].publish(message)

    def consume(self, topic_name):
        if topic_name not in self.topics:
            raise ValueError(f"Unknown topic: {topic_name}")
        return self.topics[topic_name].consume()
