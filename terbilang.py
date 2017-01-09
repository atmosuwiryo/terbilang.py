#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 atmo <atmo@atmo-X201EP>
#
# Distributed under terms of the MIT license.

"""
Menampilkan kalimat terbilang dari bilangan bulat positif

"""

SERATUS       = 100
SERIBU        = 1000
SEJUTA        = 1000000
SEMILYAR      = 1000000000
SETRILIUN     = 1000000000000
SEKUADRILIUN  = 1000000000000000
SEKUANTILIUN = 1000000000000000000
SEKSTILIUN    = 1000000000000000000000

def _terbilang(numb):

    kalimat = ""
    num=[
        " ",
        "Satu ",
        "Dua ",
        "Tiga ",
        "Empat ",
        "Lima ",
        "Enam ",
        "Tujuh ",
        "Delapan ",
        "Sembilan ",
        "Sepuluh ",
        "Sebelas "
    ]
    if numb < 12:
        kalimat = num[numb]
    elif numb < 20:
        kalimat = num[numb-10] + "Belas "
    elif numb < 100:
        puluhan = num[numb/10] + "Puluh "
        satuan = num[numb%10]
        kalimat = puluhan + satuan
    elif numb < 200:
        kalimat = "Seratus " + _terbilang(numb%SERATUS)
    elif numb < SERIBU:
        ratusan = num[numb/SERATUS] + "Ratus "
        kalimat = ratusan + _terbilang(numb%SERATUS)
    elif numb < 2000:
        kalimat = "Seribu " + _terbilang(numb%SERIBU)
    elif numb < SEJUTA:
        ribuan = _terbilang(numb/SERIBU) + "Ribu "
        kalimat = ribuan + _terbilang(numb%SERIBU)
    elif numb < SEMILYAR:
        jutaan = _terbilang(numb/SEJUTA) + "Juta "
        kalimat = jutaan + _terbilang(numb%SEJUTA)
    elif numb < SETRILIUN:
        milyaran = _terbilang(numb/SEMILYAR) + "Milyar "
        kalimat = milyaran + _terbilang(numb%SEMILYAR)
    elif numb < SEKUADRILIUN:
        triliun = _terbilang(numb/SETRILIUN) + "Triliun "
        kalimat = triliun + _terbilang(numb%SETRILIUN)
    elif numb < SEKUANTILIUN:
        kuadriliun = _terbilang(numb/SEKUADRILIUN) + "Kuadriliun "
        kalimat = kuadriliun + _terbilang(numb%SEKUADRILIUN)
    elif numb < SEKSTILIUN:
        kuantiliun = _terbilang(numb/SEKUANTILIUN) + "Kuantiliun "
        kalimat = kuantiliun + _terbilang(numb%SEKUANTILIUN)
    else:
        kalimat = "Bilangan Terlalu Besar, Hitung saja sendiri!"
    return kalimat

def terbilang(numb):
    if numb == 0:
        kalimat = "Nol"
    else:
        kalimat = _terbilang(numb)
    return kalimat.strip()

if __name__ == "__main__":
    kalimat = terbilang(12345678901234567890)
    print kalimat
