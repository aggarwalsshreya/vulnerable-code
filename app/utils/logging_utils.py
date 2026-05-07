import logging

logger = logging.getLogger("audit")


def audit(action, username):
    logger.warning("action=%s user=%s" % (action, username))  # CWE-117
