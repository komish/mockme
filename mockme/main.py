#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os


def help_text():
    help_text = """
MoCk YoUr FrIeNdS, YoUr WiFe, AnD YoUr KiDs, ThIs Is A UtIlItY To
AnNoY ThE MaSsEs! JuSt TyPe A PhRaSe AnD SeE WhAt HaPpEnS!
"""
    usage = "usage: {} phrase goes here, just type away and hit enter!\n"
    print(usage.format(os.path.basename(sys.argv[0])), help_text)


def main():
    image_url = 'https://goo.gl/g54u4V'
    if len(sys.argv) < 2 or '--help' in sys.argv:
        help_text()
        sys.exit(1)

    else:
        print(image_url, end=": ")
        for word in sys.argv[1:]:
            word = list(word.lower())
            for index in range(0, len(word)):
                if index == 0 or index % 2 == 0:
                    word[index] = word[index].upper()
            new_word = str()
            for i in word:
                new_word += str(i)
            print(new_word, end=" ")
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
