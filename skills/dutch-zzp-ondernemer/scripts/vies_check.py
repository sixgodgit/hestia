#!/usr/bin/env python3
"""VIES check for a btw-id / EU VAT number. Stdlib only, no keys.

Usage:
    python3 vies_check.py NL123456789B01 [NL123456789B01 ...]

The VIES REST service is occasionally unavailable and answers with an HTML
error page; this script falls back to the SOAP endpoint before giving up.

Read the output as two things at once: `isValid` (is the registration live) and
`handelsnaam` (what the Belastingdienst has registered for that number -- the
cheap check that the name on your letterhead matches).

For 0%-btw intracommunautaire levering, keep the printed 'bewijsregel' line with
the invoice as the dated evidence for the zero rate.
"""
import json
import re
import sys
import urllib.request

REST = "https://ec.europa.eu/taxation_customs/vies/rest-api/ms/{cc}/vat/{nr}"
SOAP = "https://ec.europa.eu/taxation_customs/vies/services/checkVatService"
UA = {"Accept": "application/json", "User-Agent": "curl/8.5.0"}


def _split(number):
    nr = number.replace(" ", "").replace("-", "").upper()
    return nr[:2], nr[2:]


def via_rest(cc, nr):
    req = urllib.request.Request(REST.format(cc=cc, nr=nr), headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def via_soap(cc, nr):
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"'
        ' xmlns:urn="urn:ec.europa.eu:taxud:vies:services:checkVat:types">'
        "<soapenv:Body><urn:checkVat>"
        f"<urn:countryCode>{cc}</urn:countryCode>"
        f"<urn:vatNumber>{nr}</urn:vatNumber>"
        "</urn:checkVat></soapenv:Body></soapenv:Envelope>"
    ).encode()
    req = urllib.request.Request(
        SOAP,
        data=body,
        headers={"Content-Type": "text/xml;charset=UTF-8", "SOAPAction": '""'},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        xml = r.read().decode("utf-8", "replace")
    return {
        "isValid": "<ns2:valid>true</ns2:valid>" in xml or "<valid>true</valid>" in xml,
        "name": (re.search(r"<ns2:name>(.*?)</ns2:name>", xml, re.S) or [None, ""])[1].strip(),
        "address": (re.search(r"<ns2:address>(.*?)</ns2:address>", xml, re.S) or [None, ""])[1].strip(),
        "requestDate": (re.search(r"<ns2:requestDate>(.*?)</ns2:requestDate>", xml, re.S) or [None, ""])[1].strip(),
        "userError": "VALID" if "<ns2:valid>true</ns2:valid>" in xml else "(SOAP)",
    }


def report(number):
    cc, nr = _split(number)
    try:
        d = via_rest(cc, nr)
        if "isValid" not in d:
            raise ValueError(f"unexpected REST payload: {str(d)[:120]}")
    except Exception as first:
        try:
            d = via_soap(cc, nr)
        except Exception as second:
            print(f"{number}: FAILED  rest={first}  soap={second}")
            return 1
    print(f"{number}: {'VALID' if d.get('isValid') else 'INVALID'}")
    name = (d.get("name") or "").strip()
    addr = " / ".join(x.strip() for x in (d.get("address") or "").splitlines() if x.strip())
    if name:
        print(f"  handelsnaam : {name}")
    if addr:
        print(f"  adres       : {addr}")
    print(f"  requestDate : {d.get('requestDate')}  userError={d.get('userError')}")
    print(
        "  bewijsregel : VIES "
        f"{d.get('requestDate')} {number} -> {d.get('userError')}"
        "  (bewaar bij 0%-btw facturen)"
    )
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    return max(report(a) for a in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
