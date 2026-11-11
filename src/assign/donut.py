import logging
import threading
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

lockdown = threading.Lock()
unresponsed = set()
