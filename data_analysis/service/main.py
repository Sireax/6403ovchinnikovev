import time
from threading import Thread
from queue import Queue


class RealtimeDataProcessor:
    def __init__(self, interval, coords, config_path):
        self.interval = interval
        self.coords_queue = Queue()
        self.config_path = config_path
        self.running = False

    def start(self):
        self.running = True
        Thread(target=self.process_coords).start()

    def stop(self):
        self.running = False

    def set_coords(self, coords):
        self.coords_queue.put(coords)

    def process_coords(self):
        while self.running:
            if not self.coords_queue.empty():
                coords = self.coords_queue.get()
                # Здесь должна быть логика обработки координат
                print(f"Обработка координат: {coords}")
            time.sleep(self.interval)


def main():
    cities = {
        'vancouver': [49.2497, -123.1193],
        'chicago': [41.85, 87.65],
        'argentina': [3.1412, 101.687]
    }

    processor = RealtimeDataProcessor(1, [], '../configs/logging.conf')
    processor.start()

    print("Введите сообщение (для выхода введите 'exit' или 'quit'):")

    while True:
        message = input().lower()
        if message in ['exit', 'quit']:
            print("Спасибо за использование программы. До свидания!")
            processor.stop()
            break

        if message in cities:
            processor.set_coords(cities[message])

        print(f"Получено сообщение: {message}")


if __name__ == "__main__":
    main()
