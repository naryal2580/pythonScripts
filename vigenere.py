#!/usr/bin/env python3

"""
 _  _  /                \\
)o||o(  .___,.___ \___ .___ \___ .___
 \||/ | | . )|___)|   )|___)|   )|___)
  \/  | |__/ |___.|  / |___.|    |___.
      \___/

Usage:
    vigenere.py
    vigenere.py -c | -C | --cipher
    vigenere.py -D | -d | --decipher
    vigenere.py -h | -H | --help
    vigenere.py -V | --version

Options:
    -c -C --cipher    Open on Cipher Mode.
    -d -D --decipher  Initiate with Decipher mode!
    -h -H --help      Displays this help.
    -V --version      Ouputs the version of the script.

Examples:
    vigenere.py
    vigenere.py -c
    vigenere.py -D
    vigenere.py -h
    vigenere.py -V
"""

__author__ = 'naryal2580'
__version__ = 'v0.4'

from naryal2580.style import bold, purple_l, rst, italic, green_l, red_l, \
 bad, good, info, coolInput
from getch import getch
from string import ascii_uppercase
from random import uniform as randFloat
from time import sleep
from docopt import docopt


def banner():
    logo = '''
 _  _  /                \\
)o||o(  .___,.___ \___ .___ \___ .___
 \||/ | | . )|___)|   )|___)|   )|___)
  \/  | |__/ |___.|  / |___.|    |___.
      \___/                             __{}__'''.format(__version__)
    # I have escaped one back-slash, becuase seublimeText was automatically \
    # removing the traling spaces after the back-slash @ the 1st line.
    logo = bold+logo[1:]+rst
    logo = logo.replace('.', bold+green_l+'.'+rst+bold)
    logo = logo.replace('o', bold+red_l+'o'+rst+bold)
    logo += '\n'+' '*4+'</> with {}<3{}  {}--naryal2580{}'.format(red_l, rst,
                                                                  bold, rst). \
            replace('/', green_l+'/'+rst)
    print(logo)


def caps_input(prompt='Caps. Input'):
    prompt = '['+bold+purple_l+'<'+rst+'] '+purple_l+str(prompt)+':'+rst+' ' +\
                italic
    print(prompt, end='', flush=True)
    validChars = ascii_uppercase
    inp_str = ''
    while 1:
        char = getch().upper()
        if 'decode' in dir(char):
            char = char.decode()
        if char == '\r':
            print('')
            break
        elif char == '\x03':
            print(rst+'\n'+bad('SIGINT recvd., Terminating.'))
            exit(0)
        elif char == '\x04':
            print(rst+'\n'+bad('EOF recvd., Termination sequence initiated!'))
            exit(0)
        elif char == '\x12':
            print('{}\r'.format('\b'*len(inp_str)+' '*len(inp_str)), end='')
            print('\r{}'.format(rst+prompt), end='')
            inp_str = ''
            continue
        elif char == '\x7f' or char == '\x08':
            print('{}\r'.format('\b'*len(inp_str)+' '*len(inp_str)), end='',
                  flush=True)
            print('\r{}'.format(rst+prompt), end='', flush=True)
            inp_str = inp_str[:-1]
            print(inp_str, end='', flush=True)
            continue
        elif char not in list(validChars):
            continue
        inp_str += char.upper()
        print(char.upper(), end='', flush=True)
    print(rst, end='')
    return inp_str


def cipher(plainTxt, key):
    cipherTxt = ""
    keyPos = []
    for k in key:
        keyPos.append(ascii_uppercase.find(k))
    i = 0
    for x in plainTxt:
        if i == len(keyPos):
            i = 0
        pos = ascii_uppercase.find(x) + keyPos[i]
        if pos > 25:
            pos = pos - 26
        for z in range(pos+1):
            q = ascii_uppercase[z]
            print('\b'+q, end='', flush=True)
            sleep(randFloat(0, 0.01))
        cipherTxt += q
        print('\b'*(len(cipherTxt))+cipherTxt, end='', flush=True)
        i += 1
    print('\b'*len(cipherTxt), end='')
    return cipherTxt


def decipher(cipherTxt, key):
    plainTxt = ""
    keyPos = []
    for k in key:
        keyPos.append(ascii_uppercase.find(k))
    i = 0
    for x in cipherTxt:
        if i == len(keyPos):
            i = 0
        pos = ascii_uppercase.find(x) - keyPos[i]
        if pos < 0:
            pos += 26
        for z in range(pos+1):
            q = ascii_uppercase[z]
            print('\b'+q, end='', flush=True)
            sleep(randFloat(0, 0.01))
        plainTxt += q
        i += 1
        print('\b'*(len(plainTxt))+plainTxt, end='', flush=True)
    print('\b'*len(plainTxt), end='')
    return plainTxt


def main(mode):
    if mode == 'cipher':
        plainTxt = caps_input('Plain Text')
        key = caps_input('Key')
        print(good("Cipher Text -> {}".format(cipher(plainTxt, key))))
    elif mode == 'decipher':
        cipherTxt = caps_input('Cipher Text')
        key = caps_input('Key')
        print(good('Plain Text -> {}'.format(decipher(cipherTxt, key))))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='vigenère_{} by {}'.format(__version__,
                                                                   __author__))
    if not arguments['--help']:
        banner()
    if arguments['-c'] or arguments['--cipher']:
        main('cipher')
    elif arguments['-d'] or arguments['--decipher']:
        main('decipher')
    else:
        print(info('Mode 1 -> Cipher'))
        print(info('Mode 2 -> Decipher'))
        choice = coolInput('Choice')

        if choice == '1':
            main('cipher')
        elif choice == '2':
            main('decipher')
        else:
            print(bad('Invalid Choice!'))
            exit(0)
