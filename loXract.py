#!/usr/bin/env python3

from naryal2580.style import good, info, coolExit, fetchFormattedTime
from scapy.all import rdpcap, Raw
from sys import argv

banner = '''
      \ /
 |  _  X  __ _  _ _|_
 | (_)/ \ | (_|(_  |_

    </> with {}<3{}  {}--naryal2580{}
'''.format('\033[31m',
           '\033[0m',
           '\033[1m',
            '\033[0m')
banner = banner.replace('X', '\033[1m\033[32mX\033[0m')
banner = banner.replace('|', '\033[34m|\033[0m')
banner = banner.replace('_', '\033[34m_\033[0m')
banner = banner.replace('(', '\033[35m(\033[0m')
banner = banner.replace(')', '\033[33m)\033[0m')
banner = banner.replace('/', '\033[32m/\033[0m')
banner = banner.replace('\\', '\033[32m\\\033[0m')
print(banner)
print(info('Started [at] {}\n'.format(fetchFormattedTime())))

if len(argv) > 1:
    pcapFileNames = argv[1:]
else:
    pcapFileNames = coolInput('Filename(s) Separated by double <space>').split(' ')


for pcapFileName in pcapFileNames:
    print(info('Opening File -> {}'.format(pcapFileName)))
    packets = rdpcap(pcapFileName)
    print(good('File read sequence compleated.'))
    data = b''
    print(info('Reading and, merging data obtained from sniffed packets of the mentioned file.'))
    for packet in packets[Raw]:
        data += packet.load
    print(good('Data Successfully Extracted -> {} bytes'.format(len(data))))
    print(info('Now, writing the Data to -> {}'.format(pcapFileName+'.out')))
    with open(pcapFileName+'.out', 'wb') as outFile:
        outFile.write(data)
        outFile.close()
    print(good('Done!\n'))

coolExit(0)
