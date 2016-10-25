import logging
import os

from cliff.show import ShowOne

class File(ShowOne):
    "show details about a file"

    log = logger.getLogger(__name__)

    def get_parser(self,prog_name):
        parser = super(File,self).get_parser(prog_name)
        parser.add_argument("filename", nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):
        stat_data = os.stat(parsed_args.filename)
        columns = ('Name','size','UID','Gid','modified time',)
        data = (parsed_args.filename,
                stat_data.st_size,
                stat_data.st_uid,
                stat_data.st_gid,
                stat_data.st_mtime,
                )
        return (columns, data)
