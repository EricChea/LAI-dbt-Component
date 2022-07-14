import logging
import os
from subprocess import PIPE, STDOUT, Popen

import lightning as L


class DBT(L.LightningWork):
    def __init__(self, profile_name: str = None, env: dict = {}, log_level=30):
        super().__init__()

        self.profile_name = profile_name
        self.env = env
        self.log_level = log_level

    def execute_command(self, command, *args, **kwargs):
        self.run(action="execute_command", command=command, *args, **kwargs)

    def _execute_command(self, command):

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
