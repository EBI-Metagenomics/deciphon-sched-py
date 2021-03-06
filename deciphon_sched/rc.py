from __future__ import annotations

from enum import Enum

__all__ = ["RC"]


class RC(int, Enum):
    SCHED_OK = 0
    SCHED_END = 1
    SCHED_HMM_NOT_FOUND = 2
    SCHED_SCAN_NOT_FOUND = 3
    SCHED_DB_NOT_FOUND = 4
    SCHED_JOB_NOT_FOUND = 5
    SCHED_PROD_NOT_FOUND = 6
    SCHED_SEQ_NOT_FOUND = 7
    SCHED_NOT_ENOUGH_MEMORY = 8
    SCHED_FAIL_PARSE_FILE = 9
    SCHED_FAIL_OPEN_FILE = 10
    SCHED_FAIL_CLOSE_FILE = 11
    SCHED_FAIL_WRITE_FILE = 12
    SCHED_FAIL_READ_FILE = 13
    SCHED_FAIL_REMOVE_FILE = 14
    SCHED_INVALID_FILE_NAME = 15
    SCHED_INVALID_FILE_NAME_EXT = 16
    SCHED_TOO_SHORT_FILE_NAME = 17
    SCHED_TOO_LONG_FILE_NAME = 18
    SCHED_TOO_LONG_FILE_PATH = 19
    SCHED_FILE_NAME_NOT_SET = 20
    SCHED_HMM_ALREADY_EXISTS = 21
    SCHED_DB_ALREADY_EXISTS = 22
    SCHED_ASSOC_HMM_NOT_FOUND = 23
    SCHED_FAIL_BIND_STMT = 24
    SCHED_FAIL_EVAL_STMT = 25
    SCHED_FAIL_GET_FRESH_STMT = 26
    SCHED_FAIL_GET_COLUMN_TEXT = 27
    SCHED_FAIL_EXEC_STMT = 28
    SCHED_FAIL_PREPARE_STMT = 29
    SCHED_FAIL_RESET_STMT = 30
    SCHED_FAIL_OPEN_SCHED_FILE = 31
    SCHED_FAIL_CLOSE_SCHED_FILE = 32
    SCHED_SQLITE8_NOT_THREAD_SAFE = 33
    SCHED_SQLITE8_TOO_OLD = 34
    SCHED_FAIL_BEGIN_TRANSACTION = 35
    SCHED_FAIL_END_TRANSACTION = 36
    SCHED_FAIL_ROLLBACK_TRANSACTION = 37

    def raise_for_status(self):
        from deciphon_sched.error import SchedError

        if self.value != RC.SCHED_OK and self.value != RC.SCHED_END:
            raise SchedError(self)
