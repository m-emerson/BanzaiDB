# Copyright 2013 Mitchell Stanton-Cook Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
# http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.


import os
import sys

class BanzaiDBConfig():
    """
    BanzaiDB configuration class 
    """

    def __init__(self):
        self.config = self.read_config()

    def __getitem__(self, key):
        try:
            return self.config[key]
        except KeyError:
            msg = "Trying to get config option that does not exist.\n"
            sys.stderr.write(msg)
            return None

    def __setitem__(self, key, item):
        self.config[key] = item

    def read_config(self):
        """
        Read a BanzaiDB configuration file

        Currently only supports:
            * db_host =  [def = localhost]
            * port    =  [def = 28015]
            * db_name =  [def = Banzai]
        """
        cfg = {}
        cfg['db_host'] = 'localhost'
        cfg['port']    = 28015
        cfg['db_name'] = 'Banzai'
        try:
            with open(os.path.expanduser('~/')+'.BanzaiDB.cfg') as fin:
                #sys.stderr.write("Using a BanzaiDB config file\n")
                colors = []
                for line in fin:
                    if (line.startswith('db_host')  or 
                            line.startswith('port') or
                            line.startswith('db_name')):
                        option, val = line.split('=')
                        cfg[option.strip()] = val.strip()
        except IOError:
            #sys.stderr.write("Using RethinkDB defaults\n")
            pass
            #for k, v in cfg.items():
            #    print "\t%s = %s" % (k, str(v))
            #print 40*'-'
        return cfg

    def dump_items(self):
        """
        Prints all set configuration options to STDOUT
        """
        config = ''
        for key, value in self.config.items():
            print str(key)+" = "+str(value)+"\n"