from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class SlurmCommand(PluginCommand):

    @command
    def do_slurm(self, args, arguments):
        """
        ::

          Usage:
                command -f FILE
                command FILE
                command list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



