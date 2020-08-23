import threading
import time

from app.config.secure import LOCK_TIMEOUT


class QuestionLockThread(threading.Thread):
    def __init__(self, qid, gid, on_timeout):
        super().__init__()
        self.qid = qid
        self.last_time = time.time()
        self.gid = gid
        self.on_timeout = on_timeout

    def run(self):
        while time.time() < self.last_time + LOCK_TIMEOUT:
            time.sleep(1)
        self.on_timeout()

    def update(self):
        self.last_time = time.time()


class QuestionLock:
    __lock_threads = {}

    def __init__(self):
        self.__lock_threads = {}

    def lock(self, qid, gid):
        if qid in self.__lock_threads:
            self.__lock_threads[qid].update()
        else:
            self.__lock_threads[qid] = QuestionLockThread(qid=qid, gid=gid, on_timeout=lambda: self.__lock_threads.pop(
                qid) if qid in self.__lock_threads else None)
            self.__lock_threads[qid].start()

    def unlock(self, qid):
        self.__lock_threads.pop(qid)

    def is_locked(self, qid):
        return qid in self.__lock_threads

    def user(self, qid):
        return self.__lock_threads[qid].gid if qid in self.__lock_threads else None


question_lock = QuestionLock()
