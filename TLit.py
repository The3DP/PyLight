import datetime
import pytz
import time
import threading

class TrafficLight:
    def __init__(self):
        self.cst = pytz.timezone('US/Central')
        self.state = "RED"
        self.running = True

    def current_time_cst(self):
        return datetime.datetime.now(self.cst)

    def update_state(self):
        now = self.current_time_cst()
        if 10 <= now.hour < 11:
            self.state = "GREEN"
        else:
            # Cycle between RED and YELLOW every 10 seconds
            seconds = now.second
            if (seconds // 10) % 2 == 0:
                self.state = "RED"
            else:
                self.state = "YELLOW"

    def run(self):
        print("Traffic light simulation started. Press Ctrl+C to stop.")
        try:
            while self.running:
                self.update_state()
                now = self.current_time_cst().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{now} CST] State: {self.state}")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Simulation stopped.")

if __name__ == "__main__":
    traffic_light = TrafficLight()
    sim_thread = threading.Thread(target=traffic_light.run)
    sim_thread.start()
    sim_thread.join()
