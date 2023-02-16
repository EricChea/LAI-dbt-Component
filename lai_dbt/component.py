import logging
import os
import time
from subprocess import PIPE, STDOUT, Popen

import lightning as L


class DBT(L.LightningWork):
    def __init__(self, profile_name: str = None, env: dict = {}, log_level=30, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.profile_name = profile_name
        self.env = env
        self.log_level = log_level

    def execute_command(self, command, start_ts=time.time()):
        self.run(action="execute_command", command=command, start_ts=start_ts)

    def _execute_command(self, command, start_ts):
        logging.log(self.log_level, f"Started at {start_ts}")

        env = os.environ.copy()
        env.update(self.env)

        with Popen(
            command,
            env=env,
            stdout=PIPE,
            stderr=STDOUT,
        ) as sub_process:

            for line in iter(sub_process.stdout.readline, b""):
                logging.log(self.log_level, line.decode("utf-8").rstrip())
            sub_process.wait()
            if sub_process.returncode:
                logging.error(sub_process.returncode)

    def run(self, action, *args, **kwargs):
        if action == "execute_command":
            self._execute_command(*args, **kwargs)
