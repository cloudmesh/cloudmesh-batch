from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
# from cloudmesh.batch.api.manager import Manager

class BatchCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_batch(self, args, arguments):
       """
        ::

            Usage:
                batch queue [--job=NAME][--cluster=CLUSTER][--format=FORMAT]
                batch info [--cluster=CLUSTER][--format=FORMAT]
                batch run list [ID] [--cluster=CLUSTER]
                batch run output [ID] [--cluster=CLUSTER]
                batch run rm [ID] [--cluster=CLUSTER]
                batch run SCRIPT [--queue=QUEUE] [--t=TIME] [--N=nodes] [--name=NAME] [--cluster=CLUSTER][--dir=DIR][--group=GROUP][--format=FORMAT]
                batch delete --job=NAME [--cluster=CLUSTER][--group=GROUP]
                batch delete all [--cluster=CLUSTER][--group=GROUP][--format=FORMAT]
                batch status [--job=name] [--cluster=CLUSTER] [--group=GROUP]
                batch test --cluster=CLUSTER [--time=SECONDS]

            Options:
               --format=FORMAT  the output format [default: table]

            Examples:

                Special notes

                   if the group is specified only jobs from that group are
                   considered. Otherwise the default group is used. If the
                   group is set to None, all groups are used.

                cms batch queue
                    lists the details of the queues of the hpc cluster

                cms batch queue --job=NAME
                    lists the details of the job in the queue of the batch cluster

                cms batch info
                    lists the details of the batch cluster

                cms batch run SCRIPT
                    submits the script to the cluster. The script will be
                    copied prior to execution into the home directory on the
                    remote machine. If a DIR is specified it will be copied
                    into that dir.
                    The name of the script is either specified in the script
                    itself, or if not the default naming scheme of
                    cloudmesh is used using the same index incremented name
                    as in vms fro clouds: cloudmes husername-index

                cms batch delete all
                    kills all jobs on the default batch group

                cms batch delete --job=NAME
                    kills a job with a given name or job id

                cms default cluster=NAME
                    sets the default batch cluster

                cms batch status
                    returns the status of all jobs

                cms batch status job=ID
                    returns the status of the named job

                cms batch test --cluster=CLUSTER --time=SECONDS
                    submits a simple test job to the named cluster and returns
                    if the job could be successfully executed. This is a
                    blocking call and may take a long time to complete
                    dependent on if the queuing system of that cluster is
                    busy. It will only use one node/core and print the message

                    #CLOUDMESH: Test ok

                    in that is being looked for to identify if the test is
                    successful. If time is used, the job is terminated
                    after the time is elapsed.

            Examples:
                cms batch queue
                cms batch queue --job=xxx
                cms batch info
                cms batch delete --job=6
                cms batch delete all
                cms batch status
                cms batch status --job=6
                cms batch run uname
                cms batch run ~/test.sh --cluster=india
        """







