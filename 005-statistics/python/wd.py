import logging
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
responder = LoggingEventHandler()
observer = Observer()

observer.schedule(responder, '.')
observer.start()
observer.join()
