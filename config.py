
#
#
# configuration file - contains customization for exact system
# JCS 11/8/2013
#

mailUser = "yourusename"
mailPassword = "yourmailpassword"

notifyAddress ="you@example.com"

fromAddress = "yourfromaddress@example.com"

textnotifyAddress = "yourphonenumber@yourprovider"

#MySQL Logging and Password Information

enable_MySQL_Logging = True
MySQL_Password = "root"

# modify this IP to enable WLAN operating detection  - search for WLAN_check in GroveWeatherPi.py
enable_WLAN_Detection = True
PingableRouterAddress = "192.168.1.1"

# WeatherUnderground Station

WeatherUnderground_Present = False
WeatherUnderground_StationID = "ISAADELA8"
WeatherUnderground_StationKey = "16438606"



# for barometeric pressure - needed to calculate sealevel equivalent - set your weatherstation elevation here

BMP280_Altitude_Meters = 320.0

# device present global variables

Lightning_Mode = False
SolarPower_Mode = True

TCA9545_I2CMux_Present = False
SunAirPlus_Present = True
AS3935_Present = False
DS3231_Present = False
BMP280_Present = False
FRAM_Present = False
HTU21DF_Present = False
AM2315_Present = True
ADS1015_Present = False
ADS1115_Present = False
OLED_Present = False
WXLink_Present = True
Sunlight_Preset = True

# if the WXLink has stopped transmitting, == False
WXLink_Data_Fresh = False
WXLInk_LastMessageID = 0
