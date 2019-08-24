#!/usr/bin/env python3
'''
Created on 20190822
Update on 20190823
@author: Eduardo Pagotto
'''

import logging
import time

import sys
sys.path.append('../Zero')

import common_rpc as rpc

from Zero.subsys.GracefulKiller import GracefulKiller
from Zero.ServiceObject import ServiceObject

class ServerRPC(ServiceObject):
    def __init__(self):
        device_bus = ''
        self.vivo = True

        super().__init__(device_bus, rpc.BUS_PATH)

    # ref: https://stackoverflow.com/questions/44819707/call-a-base-class-method-using-a-derived-class-object-outside-the-derived-class
    @ServiceObject.rpc_call(rpc.IS_ALIVE_INTERFACE, input=(), output=('b',))
    def is_alive_bitch(self):
        return self.vivo  


def main():

    log = logging.getLogger('Server')
    #logging.getLogger('Zero').setLevel(logging.INFO)

    try:

        killer = GracefulKiller()

        server = ServerRPC()

        while True:
            time.sleep(1)
            if killer.kill_now is True:
                server.stop()  
                break

        server.join()

    except Exception as exp:
        log.Exception('falha %s', str(exp))

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(threadName)-16s %(funcName)-20s %(message)s',
        datefmt='%H:%M:%S',
    )

    main()
