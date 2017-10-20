"""
    FFM by @JusticeRage

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from model.driver.input_api import *
import os

class RunPyScript:
    def __init__(self, *args, **kwargs):
        if len(args) != 2:
            write_str(" ".join(args))
            raise RuntimeError("Received %d arguments, expected 2." % len(args))
        if not os.path.exists(args[1]):
            raise RuntimeError("%s not found!" % args[1])
        self.script = args[1]


    @staticmethod
    def regexp():
        return r"^\!py"

    @staticmethod
    def usage():
        write_str("Usage: !py [script on the local machine] [script arguments]\r\n")

    @staticmethod
    def name():
        return "py"

    def execute(self):
        with open(self.script, 'r') as f:
            contents = f.read()
            shell_exec("python <<'__EOF__'\r\n%s\r\n__EOF__" % contents, print_output=True)
