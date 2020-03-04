#!/usr/bin/env python3

"""
      \ /
 |  _  X  __ _  _ _|_
 | (_)/ \ | (_|(_  |_

Usage:
    loXract.py
    loXract.py <pcapFile>...
    loXract.py -h | -H | --help
    loXract.py -V | --version

Options:
    -h -H --help  Displays this help.
    -V --version  Ouputs the version of the script.
    <pcapFile>    Filename(s) of the .pcap file to extract data from.

Examples:
    loXract.py
    loXract.py sniffs.pacp
    loXract.py sniffs0.pacp sniffs2.pacp sniffs4.pacp sniffsN.pcap
    loXract.py -h
    loXract.py -V
"""

__author__ = 'naryal2580'
__version__ = 'v0.7'

from stoyled import good, info, coolInput, coolExit, \
  fetchFormatedTime, bad
from scapy.all import rdpcap, Raw
from docopt import docopt


def banner():
    logo = '''
          \ /
     |  _  X  __ _  _ _|_
     | (_)/ \ | (_|(_  |_  {{{}}}

        </> with {}<3{}  {}--naryal2580{}
    '''.format(__version__,
               '\033[31m',
               '\033[0m',
               '\033[1m',
               '\033[0m')
    logo = logo.replace('X', '\033[1m\033[32mX\033[0m')
    logo = logo.replace('|', '\033[34m|\033[0m')
    logo = logo.replace('_', '\033[34m_\033[0m')
    logo = logo.replace('(', '\033[35m(\033[0m')
    logo = logo.replace(')', '\033[33m)\033[0m')
    logo = logo.replace('/', '\033[32m/\033[0m')
    logo = logo.replace('\\', '\033[32m\\\033[0m')
    print(logo)


def main(pcapFileNames):
    print(info('Started [at] {}\n'.format(fetchFormattedTime())))
    try:
        for pcapFileName in pcapFileNames:
            print(info('Opening File -> {}'.format(pcapFileName)))
            packets = rdpcap(pcapFileName)
            print(good('File read sequence compleated.'))
            data = b''
            print(
                  info(
                    'Reading and, merging data from provided sniffed packets .'
                      )
                  )
            for packet in packets[Raw]:
                data += packet.load
            print(
                  good(
                    'Data Successfully Extracted -> {} bytes'.format(len(data))
                      )
                  )
            print(
                info(
                    'Now, writing the Data to -> {}'.format(
                                                            pcapFileName+'.out'
                                                            )
                     )
                  )
            with open(pcapFileName+'.out', 'wb') as outFile:
                outFile.write(data)
                outFile.close()
            print(good('Done!\n'))
    except KeyboardInterrupt:
        print(bad('SIGINT recieved, terminating.'))
        coolExit(0)
    except Exception as exception:
        print(bad('Ugh! Error -> {}'.format(exception)))
        coolExit(1)
    coolExit(0)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='loXract_{} by {}'.format(__version__,
                                                                  __author__))
    if not arguments['--help']:
        banner()
    if arguments['<pcapFile>']:
        pcapFileNames = arguments['<pcapFile>']
    else:
        pcapFileNames = coolInput('Filename(s) Separated by double <space>').\
                                    split(' ')
    main(pcapFileNames)
