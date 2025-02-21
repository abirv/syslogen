"""
    SYSLOGEN
    Simple Log Generator
    Copyright (C) 2021 Bengart Zakhar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Description:
        Main module for SYSLOGEN

    Author:
        Bengart Zakhar
"""

import os
import random
import socket
import datetime
from time import sleep

class Syslogen():
    """
    Main class for Syslogen
    Read lines from file example
    Use random line and send it to server
    Generate count per 1 second messages
    """
    def __init__(self, server_ip, port, input_file, count):
        self.server_ip = server_ip
        self.port = port
        self.input_file = input_file
        self.count = count

    def start(self):
        """
        Create sockets
        Read file and send to server
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
        while True:
            message = lines[random.randrange(0, len(lines) - 1)]
            timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
            hostname = socket.gethostname()
            syslog_msg = f"<14>{timestamp} {hostname} {message}"
            sock.sendto(syslog_msg.encode('utf-8'), (self.server_ip, self.port))
            sleep(1/self.count)