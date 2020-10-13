import argparse
from pre_commit_hooks.runner import *
from colorama import init as colorama_init, Fore

MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: Scalafix SBT plugin not present! See {Fore.BLUE}https://github.com/scalacenter/sbt-scalafix{Fore.RED} for installation instructions.'


def main(argv=None):
    colorama_init()

    return run_sbt_command(f'; clean ; scalafix ; test:scalafix', missing_plugin_error_msg=MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
