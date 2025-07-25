import time
import random

class StopAndWaitProtocol:
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.sent_frames = 0
        self.timeout = 2  # seconds

    def send_frame(self, frame_id):
        print(f"Sender: Sending frame {frame_id}")
        # Simulate delay in sending
        time.sleep(1)
        # Randomly decide if the frame is acknowledged or lost
        if random.choice([True, False]):
            self.receive_ack(frame_id)
        else:
            print(f"Sender: Timeout! No ACK for frame {frame_id}. Resending...")
            self.send_frame(frame_id)  # Retransmit frame

    def receive_ack(self, frame_id):
        print(f"Receiver: Frame {frame_id} received. Sending ACK.")
        time.sleep(0.5)
        print(f"Sender: ACK received for frame {frame_id}")
        print()
        self.sent_frames += 1

    def start(self):
        print("---- Stop-and-Wait Protocol Simulation ----")
        while self.sent_frames < self.total_frames:
            self.send_frame(self.sent_frames)
        print("All frames sent and acknowledged.")

# Simulate sending 5 frames
protocol = StopAndWaitProtocol(total_frames=5)
protocol.start()
