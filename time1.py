from typing import Dict

class DataStream:
    def __init__(self):
        # Dictionary to store the last printed timestamp for each string
        self.last_seen: Dict[str, int] = {}

    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        # Check if the string can be printed
        if data_str not in self.last_seen or timestamp >= self.last_seen[data_str] + 5:
            self.last_seen[data_str] = timestamp  # Update the last printed timestamp
            return True
        return False

# Example Usage:
data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_str="hello"))  # true
print(data_stream.should_output_data_str(timestamp=1, data_str="world"))  # true
print(data_stream.should_output_data_str(timestamp=6, data_str="hello"))  # true
print(data_stream.should_output_data_str(timestamp=7, data_str="hello"))  # false
print(data_stream.should_output_data_str(timestamp=8, data_str="world"))  # true
