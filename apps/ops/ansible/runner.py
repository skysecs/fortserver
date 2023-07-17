import os
import uuid

import ansible_runner
from django.conf import settings

from .callback import DefaultCallback
from ..utils import get_ansible_log_verbosity


class CommandInBlackListException(Exception):
    pass


class AdHocRunner:
    cmd_modules_choices = ('shell', 'raw', 'command', 'script', 'win_shell')

    def __init__(self, inventory, module, module_args='', pattern='*', project_dir='/tmp/', extra_vars={},
                 dry_run=False, timeout=-1):
        self.id = uuid.uuid4()
        self.inventory = inventory
        self.pattern = pattern
        self.module = module
        self.module_args = module_args
        self.project_dir = project_dir
        self.cb = DefaultCallback()
        self.runner = None
        self.extra_vars = extra_vars
        self.dry_run = dry_run
        self.timeout = timeout

    def check_module(self):
        if self.module not in self.cmd_modules_choices:
            return
        if self.module_args and self.module_args.split()[0] in settings.SECURITY_COMMAND_BLACKLIST:
            raise CommandInBlackListException(
                "Command is rejected by black list: {}".format(self.module_args.split()[0]))

    def run(self, verbosity=0, **kwargs):
        self.check_module()
        verbosity = get_ansible_log_verbosity(verbosity)

        if not os.path.exists(self.project_dir):
            os.mkdir(self.project_dir, 0o755)

        ansible_runner.run(
            timeout=self.timeout if self.timeout > 0 else None,
            extravars=self.extra_vars,
            host_pattern=self.pattern,
            private_data_dir=self.project_dir,
            inventory=self.inventory,
            module=self.module,
            module_args=self.module_args,
            verbosity=verbosity,
            event_handler=self.cb.event_handler,
            status_handler=self.cb.status_handler,
            **kwargs
        )
        return self.cb


class PlaybookRunner:
    def __init__(self, inventory, playbook, project_dir='/tmp/', callback=None):
        self.id = uuid.uuid4()
        self.inventory = inventory
        self.playbook = playbook
        self.project_dir = project_dir
        if not callback:
            callback = DefaultCallback()
        self.cb = callback

    def run(self, verbosity=0, **kwargs):
        verbosity = get_ansible_log_verbosity(verbosity)

        ansible_runner.run(
            private_data_dir=self.project_dir,
            inventory=self.inventory,
            playbook=self.playbook,
            verbosity=verbosity,
            event_handler=self.cb.event_handler,
            status_handler=self.cb.status_handler,
            host_cwd=self.project_dir,
            **kwargs
        )
        return self.cb


class CommandRunner(AdHocRunner):
    def __init__(self, inventory, command, pattern='*', project_dir='/tmp/'):
        super().__init__(inventory, 'shell', command, pattern, project_dir)

    def run(self, verbosity=0, **kwargs):
        return super().run(verbosity, **kwargs)
