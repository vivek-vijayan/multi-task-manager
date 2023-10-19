import psutil
from ..mtm_decor.mtm_decorator import check_if_process_terminated


# Decorator

class Process:
    __doc__ = '''
    This process class contains the detail information of the list of all
    application that is currently being considered into the MTM application
    '''

    def __init__(self, pid: int, pname: str, pdesc: str):
        self.pid = pid
        self.pname = pname
        self.pdesc = pdesc
        self.process = psutil.Process(self.pid)

    def process_termination(self, pid: int) -> bool:
        try:
            self.process.terminate()
            return True
        except ChildProcessError:
            print(f"Process Termination failed for sub class process")
            return False
