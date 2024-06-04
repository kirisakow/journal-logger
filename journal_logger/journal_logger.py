import logging
from cysystemd import journal
from jl_utils.utils import caller_func_name


class JournalLogger(logging.Logger):
    """An object that enables logging to `journalctl`"""

    def __init__(self, program_name=None):
        super().__init__(program_name)
        self.program_name = program_name

    def print(self, *args, **kwargs):
        if (caller := caller_func_name()) is str:
            print(f"{self.program_name}: {caller}: {str(*args)}", **kwargs, file=journal)
        else:
            print(f"{self.program_name}: {str(*args)}", **kwargs, file=journal)
