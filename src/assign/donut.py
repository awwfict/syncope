import logging
import threading
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


lockdown = threading.Lock()
unresponse = set()
