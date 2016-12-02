import astromodule as e
import math
x = e.dmsdd(182,31,27)
print ("Degrees, minutes and seconds to decimal degrees: ",x)
z = e.dddeg(x)
print(z)
# Conversion of angles expressed in degrees and angles expressed in hours
# 1 decimal degrees to decimal hours
print("Hour %02d" % e.dddeg(e.dhdd(e.hmsdh(9,36,10.2))))
print("Minute %02d" % e.ddmin(e.dhdd(e.hmsdh(9,36,10.2))))
print("Seconds %02d" % e.ddsec(e.dhdd(e.hmsdh(9,36,10.2))))


hour = e.dhhour(e.raha(18, 32, 21, 14, 36, 51.67, 0, -4, 22, 4, 1980, -64))
minute = e.dhmin(e.raha(18, 32, 21, 14, 36, 51.67, 0, -4, 22, 4, 1980, -64))
seconds = e.dhsecs(e.raha(18, 32, 21, 14, 36, 51.67, 0, -4, 22, 4, 1980, -64))
print (hour,minute,seconds)
hourra = e.dhhour(e.hara(9, 52, 23.66, 14, 36, 51.67, 0, -4, 22, 4, 1980,-64))
minutera = e.dhmin(e.hara(9, 52, 23.66, 14, 36, 51.67, 0, -4, 22, 4, 1980,-64))
secondra = e.dhsecs(e.hara(9, 52, 23.66, 14, 36, 51.67, 0, -4, 22, 4, 1980,-64))
print(hourra, minutera, math.trunc(secondra))

print ("Equatorial to Horizon coordinate system calculations")
m = e.eqaz(11, 52, 44, 23, 13, 10, 52)

print("-=" * 60)

#C20 = -0.55425853
#C21 = 0.133359148

zen = math.atan2(m['C21'], m['C20'])
print(m['C22'])
print (zen)

for i, p in enumerate(m):
    print(i, p, m[p])

print("Az Degs ", e.dddeg(m['C24']))
print("DDmin ", e.ddmin(m['C24']))
print("DDsec ", e.ddsec(m['C24']))
print("alt degs ", e.dddeg(m['C19']))
print("alt mins ", e.ddmin(m['C19']))
print("alt secs ", e.ddsec(m['C19']))