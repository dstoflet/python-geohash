"""
Test:
    import geohash
    geohash.geoencode(57.64911,10.40744)
    geohash.geodecode('u4pruydqqvj')
"""

base32 = ['0','1','2','3','4','5','6','7','8','9','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']
lookup = {}
for x in range(len(base32)):
  lookup[base32[x]] =  x 
     
def geodecode(geohash):
  bits = base32_to_bits(geohash)
  return __decode(bits)
     
def geoencode(lat, lng):
  bits = __encode(lat,lng)
  return bits_to_base32(bits)
   
def bits_to_base32(bits):
  b32 = ""
  for x in range(0, len(bits), 5):
    b32 = b32 + base32[int(bits[x:x+5],2)]
  return b32


def base32_to_bits(b32):
  bits=""
  for x in range(len(b32)):
    bits = bits + bin(lookup[b32[x]])[2:].zfill(5)
  return bits
   
def __decode(bits):
  maxLng, minLng = 180, -180
  maxLat, minLat = 90, -90
  lngBits = [bits[x] for x in range(len(bits)) if not x % 2]
  latBits = [bits[x] for x in range(len(bits)) if x % 2]
  for bit in lngBits:
    if int(bit) == 0:
      maxLng = (maxLng + minLng) / 2.0
    else:
      minLng = (maxLng + minLng) / 2.0
  for bit in latBits:
    if int(bit) == 0:
      maxLat = (maxLat + minLat) / 2.0
    else:
      minLat = (maxLat + minLat) / 2.0
  lng = (maxLng + minLng) / 2.0
  lat = (maxLat + minLat) / 2.0
  return (lat, lng)
   
def __encode(lat, lng):
  maxLng, minLng = 180, -180
  maxLat, minLat = 90, -90
  geoBits = []
  for i in range(1, 60, 2):
    if(lng) >= (maxLng + minLng)/2.0:
      geoBits.append("1")
      minLng = (maxLng + minLng)/2.0
    else:
      geoBits.append("0")
      maxLng = (maxLng + minLng)/2.0
    if(lat) >= (maxLat + minLat)/2.0:
      geoBits.append("1")
      minLat = (maxLat + minLat)/2.0
    else:
      geoBits.append("0")
      maxLat = (maxLat + minLat)/2.0
  return "".join(geoBits)
