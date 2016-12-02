import dvgscience.astromodule as e
import math
"""
    POC for the dvgscience python package
    Copyright(c) Danny Van Geyte
"""
year = 1961
print("Testing easter:")
neweaster = e.calceaster(year)
eastermonth = 'March' if neweaster[1] == 3 else 'April'
print('Easter date : {0}/{1}/{2}'.format(neweaster[0], eastermonth, year))
juliandate = e.cdjd(23, 11, 2016)
print("Testing Juliand date conversions:")
print("Julian Date {0} (original date = 23/11/2016)".format(juliandate))
print("Reversed day: {0}".format(math.trunc(e.jdcday(2457715.5))))
print("Reversed month: {0}".format(e.jdcmonth(2457715.5)))
print("Reversed year: {0}".format(e.jdcday(2457715.5)))
print("Testing weekdays:")
print(e.getweekday_nr_and_name(1967,8,21))
print(e.getweekday_nr_and_name(1961,7,29))
print(e.getweekday_nr_and_name(2005,8,5))
print(e.getweekday_nr_and_name(2014,7,8))
print("Testing decimal time:")
print(e.hmsdh(20, 34, 27))
print("Testing decimal to time")
print(e.conv_dec_time_to_time(20.5741666667))
print("Testing conversion to UT")
zen = e.lctut(3, 37, 0, 1, 4, 1, 7, 2013)
print (zen)
utgstime = e.utgst(14, 36, 51.67, 22, 4, 1980)
print(utgstime)
gstutt = e.gstut(4, 40, 5.23, 22, 4, 1980)
print (gstutt)
gstlst = e.gstlst(4,40,5.23,-64)
print(gstlst)