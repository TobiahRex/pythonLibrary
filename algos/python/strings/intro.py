import base64

multiLine = """This
is a
multi-line string"""

embedControlChars = 'this is\n a multiline\nstring.'

bothTypes = 'this is appears :\' & this also appears: \"'

rawStrings = r'\usr\local\bin:' #\usr\local\bin:

sCap = 'toby'.capitalize(); #Toby

sCenter = 'toby'.center(100); #   toby

sCount = 'aaabbbccc'.count('a', 2); # 1

sEncode = base64.b64encode(b'tobiah rex') #{byte} prefix (b) is required for python 3.6 | python 2 does not require the (b) prefix.

print(sEncode)
