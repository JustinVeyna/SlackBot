from collections import defaultdict
from .constants import WARNING_THRESHOLD

def _get_flags(handler):
    flags = defaultdict(list)
    for data in handler:
        if data["status"] == "unconfirmed":
            flags["employee_name"].append(data)
    return flags

def _get_messages(flags):
    messages = []
    for name, entries in flags.items():
        num_flags = len(entries)
        if num_flags >= WARNING_THRESHOLD:
            messages.append((name, num_flags))

def decorate_message(msg):
    name, num_flags = msg
    eng_msg = "You have {} unconfirmed workdays on Zac: \
    please confirm them PROMPTLY.".format(num_flags)
    jp_msg = "未確定業務報告書日数は{}つあります。素早く確定してください。".format(
                                                                    num_flags)
    msg = eng_msg + "\n" + jp_msg
    return name, msg

def get_messages(handler):
    flags = _get_flags(handler)
    msgs = _get_flags(flags)
    msgs = [decorate_message(msg) for msg in msgs]
    return messenges
