#!/usr/bin/env python3

import sys


def test(did_pass):
	"""Prints the results of a test"""
	linenum = sys._getframe(1).f_lineno
	if did_pass:
		msg = "Test at line number {} ok".format(linenum)
	else:
		msg = "Test at line number {} FAILED".format(linenum)
		print(msg)


def calc_net(vat, total):
	if vat <= 0 or total <= 0:
		return "Values appear incorrect, please check and re-enter"
	elif vat > 0 and total > 0:
		vat_decimal = vat/100
		net_amount = total / (1 + vat_decimal)
		vat_amount = total - net_amount
		return  f'Total:\t{total}\nVat:\t{round(vat_amount, 2)}\nNet:\t{round(net_amount, 2)}'


def test_suite():
	test(calc_net(23, 170) == 138.21)
	test(calc_net(13.5, 1100) == 969.16)
	test(calc_net(9, 10527) == 9657.80)
	test(calc_net(23, 10.87) == 8.84)
	test(calc_net(23, 95.60) == 77.72)


vat = float(input("What is the VAT rate? (exclude % sign): " ))
total = float(input("What is the total amount (format: 10000.00)? : "))

print(calc_net(vat, total))

input("Press ENTER to exit")
