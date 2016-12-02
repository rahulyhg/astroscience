import math
import calendar as cal
"""
    Copyright (c) 2016 Danny Van Geyte
    Version 0.1
    Date created : 23/November/2016
    LM : 24/11/2016    Functions added
         25/11/2016    First stable version
    Destination Python version 3.x

    Functions in this library might vary slightly from the ones in the
    spreadsheet Standard->Astromodule.  This is only because of the way
    variables and their types are declared in Python.
    See https://docs.python.org/3/tutorial/introduction.html for more
    information about variable declaration in Python.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    Library containing manipulations on dates for astronomical purposes.

    Source of the original mathematical equations:
    'Practical Astronomy with Your Calculator or Spreadseet'
    by (Peter Duffett-Smith, Cambridge University Press)
"""

def calceaster(year):
    """
    Function to calculate the date of easter for a given year
    :param year: The year to calculate easter from
    :return: string containing easter date
    Status : calculation ok
    """
    # C3 = int(input("Give the year to calculate easter :"))
    a = year % 19
    b = math.trunc(year / 100)
    c = year % 100
    d = b / 4
    e = b % 4
    f = math.trunc((b + 8) / 25)
    g = math.trunc((b - f + 1) / 3)
    h = ((19 * a) + b - d - g + 15) % 30
    i = c / 4
    k = c % 4
    l = (32 + 2 * (e + i) - h - k) % 7
    m = math.trunc((a + (11 * h) + (22 * l)) / 451)
    n = math.trunc((h + l - (7 * m) + 114) / 31)
    p = (h + l - (7 * m) + 114) % 31
    easter_day = p + 1
    easter_month = n
    # print (a, b, c, d, e, f, g, h, i, k, l, m, n, p, easter_day, easter_month)
    return easter_day, easter_month


def cdjd(day, month, year):
    """
    Calculate the Julian date for a given calendar date
    :param jday: Greenwich Day
    :param jmonth: Greenwhich Month
    :param jyear: Greenwhich Year
    :return: the Julian date
    Status : Calculation ok
    """
    if month < 3:
        y = year - 1
        m = month + 12
    else:
        y = year
        m = month
    if year > 1582:
        a = math.trunc(y / 100)
        b = 2 - a + math.trunc(a / 4)
    elif year == 1582 and month > 10:
        a = math.trunc(y / 100)
        b = 2 - a + math.trunc(a / 4)
    elif year == 1582 and month == 10 and day >= 15:
        a = math.trunc(y / 100)
        b = 2 - a + math.trunc(a / 4)
    else:
        b = 0
    if y < 0:
        c = math.trunc((365.25 * y) - 0.75)
    else:
        c = math.trunc(365.25 * y)
    d = math.trunc(30.6001 * (m + 1))
    cdjd = b + c + d + day + 1720994.5
    return cdjd


def jdcday(jd):
    """
    Calculate the day for a given julian date
    Note : The day is not truncated when returned, this
    is needed for other calculations in this library.
    (See lct_ut function)
    :param jd:
    :return: the day of julian date
    Status : Calculation ok
    """
    i = math.trunc(jd + 0.5)
    f = (jd + 0.5) - i
    a = math.trunc((i - 1867216.25) / 36524.25)
    if i > 2299160:
        b = i + 1 + a - math.trunc(a / 4)
    else:
        b = i
    c = b + 1524
    d = math.trunc((c - 122.1) / 365.25)
    e = math.trunc(365.25 * d)
    g = math.trunc((c - e) / 30.6001)
    jdcday =c - e + f - math.trunc(30.6001 * g)
    return jdcday


def jdcmonth(jd):
    """
    Calculate the month for a given julian date
    :param jd: julian date
    :return: the month of the julian date
    Status : Calculation ok
    """
    i = math.trunc(jd + 0.5)
    f = jd + 0.5 - i
    a = math.trunc((i - 1867216.25) / 36524.25)
    if i > 2299160:
        b = i + 1 + a - math.trunc(a / 4)
    else:
        b = i
    c = b + 1524
    d = math.trunc((c - 122.1) / 365.25)
    e = math.trunc(365.25 * d)
    g = math.trunc((c - e) / 30.6001)

    if g < 13.5:
        jdcmonth = g - 1
    else:
        jdcmonth = g - 13
    return jdcmonth


def jdcyear(jd):
    """
    Calculate the year for a given julian date
    :param jd: julian date
    :return: the year of the julian date
    Status : Calculation ok
    """
    i = math.trunc(jd + 0.5)
    f = jd + 0.5 - i
    a = math.trunc((i - 1867216.25) / 36524.25)
    if i > 2299160:
        b = i + 1 + a - math.trunc(a / 4)
    else:
        b = i
    c = b + 1524
    d = math.trunc((c - 122.1) / 365.25)
    e = math.trunc(365.25 * d)
    g = math.trunc((c - e) / 30.6001)
    if g < 13.5:
        h = g - 1
    else:
        h = g - 13
    if h > 2.5:
        jdcyear = d - 4716
    else:
        jdcyear = d - 4715
    return jdcyear


def getweekday_nr_and_name(year, month, day):
    """
    Wrapper round the calendar functionality
    :param year:
    :param month:
    :param day:
    :return: the nr and the name of the day of the week
    """
    daynr = cal.weekday(year, month, day)
    dayname = cal.day_name[cal.weekday(year, month, day)]
    return daynr, dayname


def conv_dec_time_to_time(decimalhours):
    """
    Convert decimal time to normal time
    :param decimalhours : time in decimal format
    :return: Normal time
    Status : Calculation Ok
    """
    C3 = decimalhours
    C7 = abs(C3)
    C8 = C7 * 3600
    C9 = round((C8 % 60), 2)
    seconds = math.trunc(0 if C9 == 60 else C9)
    C11 = C8 + 60 if C9 == 60 else C8
    minutes = (math.trunc(C11 / 60) % 60)
    C13 = math.trunc(C11 / 3600)
    if C3 < 0:
        hour = -1 * C13
    else:
        hour = C13
    return hour, minutes, seconds


def dhhour(dh):
    """
    Decimal hours
    :param dh:
    :return:
    """
    a = abs(dh)
    b = a * 3600
    c = round(b-60 * math.trunc(b/60), 2)
    if c == 60:
        d = 0
        e = b + 60
    else:
        d = c
        e = b
    if d < 0:
        Dhhour = -math.trunc(e / 3600)
    else:
        Dhhour = math.trunc(e / 3600)
    return Dhhour


def dhmin(dh):
    """
    Decimal minutes
    :param dh:
    :return:
    """
    a = abs(dh)
    b = a * 3600
    c = round(b - 60 * math.trunc(b / 60), 2)
    if c == 60:
        d = 0
        e = b + 60
    else:
        d = c
        e = b
    return math.trunc((e / 60) % 60)


def dhsecs(dh):
    """
    Decimal seconds
    :param dh:
    :return:
    """
    a = abs(dh)
    b = a * 3600
    c = round(b - 60 * math.trunc(b / 60), 2)
    if c == 60:
        d = 0
    else:
        d = c
    return d


def dddh(dd):
    return dd / 15.0


def dhdd(dh):
    return dh * 15.0


def dmsdd(d, m, s):
    """
    Convert hour minute second to decimal hour
    :param d: degrees
    :param m: minutes
    :param s: seconds
    :return: decimal hour
    """
    a = abs(s) / 60
    b = (abs(m) + a) / 60
    c = abs(h) + b
    if h < 0 or m < 0 or s < 0:
        Hmsdh = -c
    else:
        Hmsdh = c
    return Hmsdh


def lctut(lch, lcm, lcs, ds, zc, ld, lm, ly):
    """
    lc abrev is local civil time
    Convert local time to universal time
    :param lch: local civil hours
    :param lcm: local civil minutes
    :param lcs: local civil seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :return: Universal time
    Status : Calculation ok
    """
    a = hmsdh(lch, lcm, lcs)
    b = a - ds - zc
    c = ld + (b / 24)
    d = cdjd(c, lm, ly)
    e = jdcday(d)
    e1 = math.trunc(e)
    LctUT = 24.0 * (c - math.trunc(c))
    return LctUT


def lctgday(lch, lcm, lcs, ds, zc, ld, lm, ly):
    """
    Convert local civil day to universal day
    :param lch: local civil hour
    :param lcm: local civil minutes
    :param lcs: local civil seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :return: universal day
    """
    a = hmsdh(lch, lcm, lcs)
    b = a - ds - zc
    c = ld + (b / 24)
    d = cdjd(c, lm, ly)
    e = jdcday(d)
    LctGDay = math.trunc(e)
    return LctGDay


def lctgmonth(lch, lcm, lcs, ds, zc, ld, lm, ly):
    """
    Convert local civil month to universal month
    :param lch: local civil hour
    :param lcm: local civil minutes
    :param lcs: local civil seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :return: universal month
    """
    a = hmsdh(lch, lcm, lcs)
    b = a - ds - zc
    c = ld + (b / 24)
    d = cdjd(c, lm, ly)
    LctGMonth = jdcmonth(d)
    return LctGMonth


def lctgyear(lch, lcm, lcs, ds, zc, ld, lm, ly):
    """
    Convert local civil year to universal year
    :param lch: local civil hour
    :param lcm: local civil minutes
    :param lcs: local civil seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :return: universal year
    """
    a = hmsdh(lch, lcm, lcs)
    b = a - ds - zc
    c = ld + (b / 24)
    d = cdjd(c, lm, ly)
    LctGYear = jdcyear(d)
    return LctGYear


def utgst(uh, um, us, gd, gm, gy):
    """
    Convert Universal time to siderial time (GST)
    :param uh: hour
    :param um: minute
    :param us: seconds
    :param gd: day
    :param gm: month
    :param gy: year
    :return: siderial time
    """
    a = cdjd(gd, gm, gy)
    b = a - 2451545
    c = b / 36525
    d = 6.697374558 + (2400.051336 *c) + (0.000025862 * c * c)
    e = d - (24.0 * int(d / 24.0))
    f = hmsdh(uh, um, us)
    g = f * 1.002737909
    h = e + g
    UTGST = h -(24.0 * int(h / 24.0))
    return UTGST


def gstut(gsh, gsm, gss, gd, gm, gy):
    """
    Convert siderial time to universal time
    :param gsh: hour
    :param gsm: minutes
    :param gss: seconds
    :param gd: day
    :param gm: month
    :param gy: year
    :return: universal time
    """
    a = cdjd(gd, gm, gy)
    b = a - 2451545
    c = b / 36525
    d = 6.697374558 + (2400.051336 * c)
    e = d - (24 * int (d / 24))
    f = hmsdh(gsh, gsm, gss)
    g = f - e
    h = g - (24 * int(g /24))
    i = h * 0.9972695663
    warnflag = "Warning" if i < 0.065574 else "Ok"
    return dhhour(i), dhmin(i), dhsecs(i), warnflag


def gstlst(gh, gm, gs, l):
    """
    Convert Greenwich Siderial time to local siderial time
    :param gh: hour
    :param gm: minute
    :param gs: second
    :param l: longitude
    :return: Local siderial time
    """
    c8 = hmsdh(gh, gm, gs)
    # Important, value 15 is double in formula,
    # so it is required to make it 15.0 in python
    c9 = l / 15.0
    c10 = c8 + c9
    c11 = c10 - (24.0 * int(c10 / 24))
    c12 = dhhour(c11)
    c13 = dhmin(c11)
    c14 = dhsecs(c11)

    return c12, c13, c14


def hmsdh(h, m, s):
    """
    Convert hour minute second to decimal hour
    :param h: hour
    :param m: minutes
    :param s: seconds
    :return: decimal hour
    """
    a = abs(s) / 60.0
    b = (abs(m) + a) / 60.0
    c = abs(h) + b
    if h < 0 or m < 0 or s < 0:
        Hmsdh = -c
    else:
        Hmsdh = c
    return Hmsdh


def dmsdd(degrees, minutes, seconds):
    """
    Convert degrees minutes and seconds to decimal degrees
    This
    :param degrees: degrees
    :param minutes: minutes
    :param seconds: seconds
    :return: decimal degrees
    Status : Calculation ok
    """
    a = abs(seconds) / 60.0
    b = abs(minutes + a) / 60.0
    c = abs(degrees) + b
    if degrees < 0 or minutes < 0 or seconds < 0:
        e = -c
    else:
        e = c
    return e


def dddeg(dd):
    """
    Convert decimal degrees to degrees, minutes and seconds
    :param dd: decimal date
    :return: degrees, minutes and seconds
    Status : Calculation ok
    """
    a = abs(dd)
    b = a * 3600
    c = round(b - 60 * math.trunc(b / 60), 2)
    if c == 60:
        d = 0
        e = b + 60
    else:
        d = c
        e = b
    if dd < 0:
        hour = -math.trunc(e / 3600)
    else:
        hour = math.trunc(e / 3600)
    return hour


def ddmin(dd):
    a = abs(dd)
    b = a * 3600
    c = round(b - 60 * math.trunc(b / 60), 2)
    if c == 60:
        d = 0
        e = b + 60
    else:
        d = c
        e = b
    DDMin = math.trunc(e / 60) % 60
    return DDMin


def ddsec(dd):
    a = abs(dd)
    b = a * 3600
    c = round(b - 60 * math.trunc(b / 60), 2)
    if c == 60:
        d = 0
    else:
        d = c
    return d


def raha(rh, rm, rs, lch, lcm, lcs, ds, zc, ld, lm, ly, l):
    """
    Conversion of right ascension to hour angle
    :param rh: RA hours
    :param rm: RA minutes
    :param rs: RA seconds
    :param lch: LCT hours
    :param lcm: LCT minutes
    :param lcs: LCT seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :param l: geographic longitude
    :return: hour angle
    """
    a = lctut(lch, lcm, lcs, ds, zc, ld, lm, ly)
    b = lctgday(lch, lcm, lcs, ds, zc, ld, lm, ly)
    c = lctgmonth(lch, lcm, lcs, ds, zc, ld, lm, ly)
    d = lctgyear(lch, lcm, lcs, ds, zc, ld, lm, ly)
    e = utgst(a, 0, 0, b, c, d)
    f = gstlst(e, 0, 0, l)
    g = hmsdh(rh, rm, rs)
    h = f - g
    if h < 0:
        RAHA = 24 + h
    else:
        RAHA = h
    return RAHA


def hara(hh, hm, hs, lch, lcm, lcs, ds, zc, ld, lm, ly, l):
    """
    Conversion of hour angle to right ascension
    :param hh: ra hours
    :param hm: ra minutes
    :param hs: ra second
    :param lch: LCT hours
    :param lcm: LCT minutes
    :param lcs: LCT seconds
    :param ds: daylight saving
    :param zc: zone correction
    :param ld: local day
    :param lm: local month
    :param ly: local year
    :param l: geographic longitude
    :return: right ascension
    """
    a = lctut(lch, lcm, lcs, ds, zc, ld, lm, ly)
    b = lctgday(lch, lcm, lcs, ds, zc, ld, lm, ly)
    c = lctgmonth(lch, lcm, lcs, ds, zc, ld, lm, ly)
    d = lctgyear(lch, lcm, lcs, ds, zc, ld, lm, ly)
    e = utgst(a, 0, 0, b, c, d)
    f = gstlst(e, 0, 0, l)
    g = hmsdh(hh, hm, hs)
    h = f - g
    if h < 0:
        HARA = 24 + h
    else:
        HARA = h
    return HARA


def eqaz(hh, hm, hs, dd, dm, ds, p):
    """
    Equatorial to Horizon coordinate conversion
    :param hh: hours
    :param hm: minutes
    :param hs: seconds
    :param dd: dec degrees
    :param dm: dec minutes
    :param ds: dec seconds
    :param p: geographic latitude
    :return: Equatorial azimuth
    """
    a = hmsdh(hh, hm, hs)                          # C11
    b = a * 15                                     # C12
    c = math.radians(b)                            # C13
    d = dmsdd(dd, dm, ds)                          # C14
    e = math.radians(d)                            # C15
    f = math.radians(p)                            # C16
    g = math.sin(e) * math.sin(f) + math.cos(e) * math.cos(f) * math.cos(c)  #C17
    gg = math.asin(g)                              # C18
    adegs = math.degrees(gg)                       # C19
    y = -math.cos(e) * math.cos(f) * math.sin(c)   # C20
    x = math.sin(e) - math.sin(f) * g              # C21
    A = math.atan2(y, x)                           # C22
    B = math.degrees(A)                            # C23
    Az = 360 + B
    print("-"*20, "AZ ", B)
    EQAz = x - (360 * int(A / 360))
    return {'C11':a, 'C12':b, 'C13':c, 'C14':d, 'C15':e, 'C16':f, 'C17':g, 'C18':gg, 'C19':adegs, 'C21':y, 'C20':x, 'C22':A, 'C23':B, 'C24':Az}


def horeq(azdegs, azmins, azsecs, altdegs, altmins, altsecs, geoglat):
    """
    Horizontal to equatorial coordinate conversion
    :param azdegs: Az degrees
    :param azmins: Az minutes
    :param azsecs: Az seconds
    :param altdegs: alt degrees
    :param altmins: alt mins
    :param altsecs: alt secs
    :param geoglat: geog lat
    :return: ha hours, ha mins, ha secs, dec degs, dec mins, dec secs
    """
    c11 = dmsdd(azdegs, azmins, azsecs)
    c12 = dmsdd(altdegs, altmins, altsecs)
    c13 = math.radians(c12)
    c14 = math.radians(geoglat)

