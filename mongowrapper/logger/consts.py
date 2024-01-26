from enum import Enum


class T(Enum):
    MSG = "msg/сообщение"
    TYPE = "type/тип"
    DEBUG = "debug/отладка"
    INFO = "info/инфо"
    SUCCESS = "success/успешно"
    WARNING = "warning/предупреждение"
    ERROR = "error/ошибка"
    CRITICAL = "critical/критическая ошибка"
