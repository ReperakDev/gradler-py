# Copyright (c) Reperak 2021
#
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
# software and associated documentation files (the "Software"), either in source
# code form or as a compiled binary, for any purpose, commercial or
# non-commercial, and by any means.
#
# The copyright notices in the Software and this entire statement, including the
# above license grant, this restriction and the following disclaimer, must be
# included in all copies of the Software, in whole or in part, and all derivative
# works of the Software, unless such copies or derivative works are solely in the
# form of machine-executable object code generated by a source language processor.
#
# THE SOFTWARE DISTRIBUTED UNDER THIS LICENSE IS DISTRIBUTED ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os
import argparse
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(description='Arguments for mass-building Gradle projects')
    parser.add_argument('directory', metavar='D', type=str, help='directory containing projects')
    return parser.parse_args()


def main():
    if sys.platform == 'win32':
        sys.exit('This program must be run on a UNIX-like operating system (e.g. macOS, Linux, BSD)')

    args = parse_arguments()

    os.chdir(args.directory)
    master_directory = os.path.abspath(os.getcwd())

    valid_projects = [f for f in os.listdir() if os.path.isdir(f) and 'gradlew' in os.listdir(f)]

    for x in valid_projects:
        os.chdir(x)
        os.system('chmod +x gradlew')
        os.system('./gradlew build')
        os.system('./gradlew --stop')
        os.chdir(master_directory)


if __name__ == '__main__':
    main()
