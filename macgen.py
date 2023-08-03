#!/usr/bin/env python3
import re

from argparse import ArgumentParser, ArgumentTypeError
from itertools import product, islice
from secrets import token_hex


def parse_args():
    """Parse user arguments."""
    parser = ArgumentParser(description="Simple MAC addresses generator")
    
    parser.add_argument(
        "number", nargs="?", type=int, default=1,
        help="number of mac addresses to generate")
    parser.add_argument(
        "-p", "--prefix", type=mac_prefix,
        help="mac address first bytes (ex: e5:48:92:44)")
    parser.add_argument(
        "-i", "--inc", "--increment", action="store_true",
        help="generate incrementally a list of MAC addresses")
    parser.add_argument(
        "-u", "--upper", "--uppercase",
        action="store_true", help="uppercase MAC addresses")
    
    return parser.parse_args()


def mac_prefix(prefix):
    """Return MAC address prefix if valid."""
    match = re.match(
        r"^(?:[\dabcdef]{2}:?){0,6}$", prefix, re.IGNORECASE)
    
    if not match:
        raise ArgumentTypeError(f"invalid MAC address prefix: {prefix}")
    
    return match.group(0)


def hex_to_mac(hex_number):
    """Transform hexadecimal number to MAC address format."""
    inc = 2
    return ":".join((
        hex_number[i: i + inc]
        for i in range(0, len(hex_number), inc)))


def main():
    """Program entry point."""
    #: User arguments.
    args = parse_args() 
    #: MAC addresses prefix.
    prefix = (args.prefix or "").replace(":", "").lower()
    #: Number of MAC address to generate.
    nb_mac = args.number
    #: Enable incremental generation.
    is_inc = args.inc
    #: Hexadecimal charset.
    charset = "0123456789abcdef"
    #: Number of characters to generate.
    suffix_length = 12 - len(prefix)
    #: Generated MAC addresses suffixes.
    suffixes = None
    #: Uppercase MAC addresses.
    uppercase = args.upper

    # Generate MAC addresses list by iterration.
    if is_inc:
        suffixes = map(
            "".join, islice(product(charset, repeat=suffix_length), nb_mac))
    # Generate random MAC addresses list.
    else:
        suffixes = (token_hex(int(suffix_length / 2)) for _ in range(nb_mac))
    
    for suffix in suffixes:
        mac = hex_to_mac(prefix + suffix)
        if uppercase:
            mac = mac.upper()
        print(mac)
        
        
main()