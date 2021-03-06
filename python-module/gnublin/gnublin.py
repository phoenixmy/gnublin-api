# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gnublin', [dirname(__file__)])
        except ImportError:
            import _gnublin
            return _gnublin
        if fp is not None:
            try:
                _mod = imp.load_module('_gnublin', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gnublin = swig_import_helper()
    del swig_import_helper
else:
    import _gnublin
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


GNUBLIN = _gnublin.GNUBLIN
RASPBERRY_PI = _gnublin.RASPBERRY_PI
BEAGLEBONE_BLACK = _gnublin.BEAGLEBONE_BLACK
OUTPUT = _gnublin.OUTPUT
INPUT = _gnublin.INPUT
LOW = _gnublin.LOW
HIGH = _gnublin.HIGH
ON = _gnublin.ON
OFF = _gnublin.OFF
IN = _gnublin.IN
OUT = _gnublin.OUT

def stringToNumber(*args):
  return _gnublin.stringToNumber(*args)
stringToNumber = _gnublin.stringToNumber

def numberToString(*args):
  return _gnublin.numberToString(*args)
numberToString = _gnublin.numberToString

def hexstringToNumber(*args):
  return _gnublin.hexstringToNumber(*args)
hexstringToNumber = _gnublin.hexstringToNumber
class gnublin_gpio(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_gpio, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_gpio, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_gpio()
        try: self.this.append(this)
        except: self.this = this
    def fail(self): return _gnublin.gnublin_gpio_fail(self)
    def pinMode(self, *args): return _gnublin.gnublin_gpio_pinMode(self, *args)
    def digitalWrite(self, *args): return _gnublin.gnublin_gpio_digitalWrite(self, *args)
    def digitalRead(self, *args): return _gnublin.gnublin_gpio_digitalRead(self, *args)
    def unexport(self, *args): return _gnublin.gnublin_gpio_unexport(self, *args)
    def getErrorMessage(self): return _gnublin.gnublin_gpio_getErrorMessage(self)
    __swig_destroy__ = _gnublin.delete_gnublin_gpio
    __del__ = lambda self : None;
gnublin_gpio_swigregister = _gnublin.gnublin_gpio_swigregister
gnublin_gpio_swigregister(gnublin_gpio)

class gnublin_i2c(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_i2c, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_i2c, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gnublin.new_gnublin_i2c(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gnublin.delete_gnublin_i2c
    __del__ = lambda self : None;
    def fail(self): return _gnublin.gnublin_i2c_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_i2c_setAddress(self, *args)
    def getAddress(self): return _gnublin.gnublin_i2c_getAddress(self)
    def getErrorMessage(self): return _gnublin.gnublin_i2c_getErrorMessage(self)
    def setDevicefile(self, *args): return _gnublin.gnublin_i2c_setDevicefile(self, *args)
    def receive(self, *args): return _gnublin.gnublin_i2c_receive(self, *args)
    def send(self, *args): return _gnublin.gnublin_i2c_send(self, *args)
gnublin_i2c_swigregister = _gnublin.gnublin_i2c_swigregister
gnublin_i2c_swigregister(gnublin_i2c)

class gnublin_spi(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_spi, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_spi, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_spi()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gnublin.delete_gnublin_spi
    __del__ = lambda self : None;
    def setMode(self, *args): return _gnublin.gnublin_spi_setMode(self, *args)
    def getMode(self): return _gnublin.gnublin_spi_getMode(self)
    def setLSB(self, *args): return _gnublin.gnublin_spi_setLSB(self, *args)
    def getLSB(self): return _gnublin.gnublin_spi_getLSB(self)
    def setLength(self, *args): return _gnublin.gnublin_spi_setLength(self, *args)
    def getLength(self): return _gnublin.gnublin_spi_getLength(self)
    def setSpeed(self, *args): return _gnublin.gnublin_spi_setSpeed(self, *args)
    def getSpeed(self): return _gnublin.gnublin_spi_getSpeed(self)
    def receive(self, *args): return _gnublin.gnublin_spi_receive(self, *args)
    def send(self, *args): return _gnublin.gnublin_spi_send(self, *args)
    def setCS(self, *args): return _gnublin.gnublin_spi_setCS(self, *args)
    def message(self, *args): return _gnublin.gnublin_spi_message(self, *args)
    def getErrorMessage(self): return _gnublin.gnublin_spi_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_spi_fail(self)
gnublin_spi_swigregister = _gnublin.gnublin_spi_swigregister
gnublin_spi_swigregister(gnublin_spi)

class gnublin_adc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_adc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_adc, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_adc()
        try: self.this.append(this)
        except: self.this = this
    def getValue(self, *args): return _gnublin.gnublin_adc_getValue(self, *args)
    def getVoltage(self, *args): return _gnublin.gnublin_adc_getVoltage(self, *args)
    def setReference(self, *args): return _gnublin.gnublin_adc_setReference(self, *args)
    def fail(self): return _gnublin.gnublin_adc_fail(self)
    def getErrorMessage(self): return _gnublin.gnublin_adc_getErrorMessage(self)
    __swig_destroy__ = _gnublin.delete_gnublin_adc
    __del__ = lambda self : None;
gnublin_adc_swigregister = _gnublin.gnublin_adc_swigregister
gnublin_adc_swigregister(gnublin_adc)

class gnublin_serial(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_serial, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_serial, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gnublin.new_gnublin_serial(*args)
        try: self.this.append(this)
        except: self.this = this
    def fail(self): return _gnublin.gnublin_serial_fail(self)
    def send(self, *args): return _gnublin.gnublin_serial_send(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_serial_setDevicefile(self, *args)
    def setBaudrate(self, *args): return _gnublin.gnublin_serial_setBaudrate(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_serial
    __del__ = lambda self : None;
gnublin_serial_swigregister = _gnublin.gnublin_serial_swigregister
gnublin_serial_swigregister(gnublin_serial)

class gnublin_pwm(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_pwm, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_pwm, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_pwm()
        try: self.this.append(this)
        except: self.this = this
    def setValue(self, *args): return _gnublin.gnublin_pwm_setValue(self, *args)
    def setClock(self, *args): return _gnublin.gnublin_pwm_setClock(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_pwm
    __del__ = lambda self : None;
gnublin_pwm_swigregister = _gnublin.gnublin_pwm_swigregister
gnublin_pwm_swigregister(gnublin_pwm)

class gnublin_module_dogm(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_dogm, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_dogm, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_dogm()
        try: self.this.append(this)
        except: self.this = this
    def init(self): return _gnublin.gnublin_module_dogm_init(self)
    def fail(self): return _gnublin.gnublin_module_dogm_fail(self)
    def getErrorMessage(self): return _gnublin.gnublin_module_dogm_getErrorMessage(self)
    def setRsPin(self, *args): return _gnublin.gnublin_module_dogm_setRsPin(self, *args)
    def setCS(self, *args): return _gnublin.gnublin_module_dogm_setCS(self, *args)
    def _print(self, *args): return _gnublin.gnublin_module_dogm__print(self, *args)
    def offset(self, *args): return _gnublin.gnublin_module_dogm_offset(self, *args)
    def clear(self): return _gnublin.gnublin_module_dogm_clear(self)
    def returnHome(self): return _gnublin.gnublin_module_dogm_returnHome(self)
    def shift(self, *args): return _gnublin.gnublin_module_dogm_shift(self, *args)
    def controlDisplay(self, *args): return _gnublin.gnublin_module_dogm_controlDisplay(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_module_dogm
    __del__ = lambda self : None;
gnublin_module_dogm_swigregister = _gnublin.gnublin_module_dogm_swigregister
gnublin_module_dogm_swigregister(gnublin_module_dogm)

class gnublin_module_lm75(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_lm75, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_lm75, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_lm75()
        try: self.this.append(this)
        except: self.this = this
    def getErrorMessage(self): return _gnublin.gnublin_module_lm75_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_module_lm75_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_module_lm75_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_lm75_setDevicefile(self, *args)
    def getTemp(self): return _gnublin.gnublin_module_lm75_getTemp(self)
    def getTempFloat(self): return _gnublin.gnublin_module_lm75_getTempFloat(self)
    def getValue(self): return _gnublin.gnublin_module_lm75_getValue(self)
    __swig_destroy__ = _gnublin.delete_gnublin_module_lm75
    __del__ = lambda self : None;
gnublin_module_lm75_swigregister = _gnublin.gnublin_module_lm75_swigregister
gnublin_module_lm75_swigregister(gnublin_module_lm75)

class gnublin_module_adc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_adc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_adc, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_adc()
        try: self.this.append(this)
        except: self.this = this
    def setAddress(self, *args): return _gnublin.gnublin_module_adc_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_adc_setDevicefile(self, *args)
    def setReference(self, *args): return _gnublin.gnublin_module_adc_setReference(self, *args)
    def getValue(self, *args): return _gnublin.gnublin_module_adc_getValue(self, *args)
    def getVoltage(self, *args): return _gnublin.gnublin_module_adc_getVoltage(self, *args)
    def fail(self): return _gnublin.gnublin_module_adc_fail(self)
    def getErrorMessage(self): return _gnublin.gnublin_module_adc_getErrorMessage(self)
    __swig_destroy__ = _gnublin.delete_gnublin_module_adc
    __del__ = lambda self : None;
gnublin_module_adc_swigregister = _gnublin.gnublin_module_adc_swigregister
gnublin_module_adc_swigregister(gnublin_module_adc)

class gnublin_module_pca9555(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_pca9555, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_pca9555, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_pca9555()
        try: self.this.append(this)
        except: self.this = this
    def getErrorMessage(self): return _gnublin.gnublin_module_pca9555_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_module_pca9555_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_module_pca9555_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_pca9555_setDevicefile(self, *args)
    def pinMode(self, *args): return _gnublin.gnublin_module_pca9555_pinMode(self, *args)
    def portMode(self, *args): return _gnublin.gnublin_module_pca9555_portMode(self, *args)
    def digitalWrite(self, *args): return _gnublin.gnublin_module_pca9555_digitalWrite(self, *args)
    def digitalRead(self, *args): return _gnublin.gnublin_module_pca9555_digitalRead(self, *args)
    def readState(self, *args): return _gnublin.gnublin_module_pca9555_readState(self, *args)
    def writePort(self, *args): return _gnublin.gnublin_module_pca9555_writePort(self, *args)
    def readPort(self, *args): return _gnublin.gnublin_module_pca9555_readPort(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_module_pca9555
    __del__ = lambda self : None;
gnublin_module_pca9555_swigregister = _gnublin.gnublin_module_pca9555_swigregister
gnublin_module_pca9555_swigregister(gnublin_module_pca9555)

class gnublin_module_relay(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_relay, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_relay, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_relay()
        try: self.this.append(this)
        except: self.this = this
    def getErrorMessage(self): return _gnublin.gnublin_module_relay_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_module_relay_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_module_relay_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_relay_setDevicefile(self, *args)
    def switchPin(self, *args): return _gnublin.gnublin_module_relay_switchPin(self, *args)
    def readState(self, *args): return _gnublin.gnublin_module_relay_readState(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_module_relay
    __del__ = lambda self : None;
gnublin_module_relay_swigregister = _gnublin.gnublin_module_relay_swigregister
gnublin_module_relay_swigregister(gnublin_module_relay)

class gnublin_module_step(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_step, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_step, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_step()
        try: self.this.append(this)
        except: self.this = this
    def setAddress(self, *args): return _gnublin.gnublin_module_step_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_step_setDevicefile(self, *args)
    def setIrun(self, *args): return _gnublin.gnublin_module_step_setIrun(self, *args)
    def setIhold(self, *args): return _gnublin.gnublin_module_step_setIhold(self, *args)
    def setVmax(self, *args): return _gnublin.gnublin_module_step_setVmax(self, *args)
    def setVmin(self, *args): return _gnublin.gnublin_module_step_setVmin(self, *args)
    def setStepMode(self, *args): return _gnublin.gnublin_module_step_setStepMode(self, *args)
    def setAccShape(self, *args): return _gnublin.gnublin_module_step_setAccShape(self, *args)
    def writeTMC(self, *args): return _gnublin.gnublin_module_step_writeTMC(self, *args)
    def readTMC(self, *args): return _gnublin.gnublin_module_step_readTMC(self, *args)
    def burnNewAddress(self, *args): return _gnublin.gnublin_module_step_burnNewAddress(self, *args)
    def getFullStatus1(self): return _gnublin.gnublin_module_step_getFullStatus1(self)
    def getFullStatus2(self): return _gnublin.gnublin_module_step_getFullStatus2(self)
    def runInit(self): return _gnublin.gnublin_module_step_runInit(self)
    def setMotorParam(self, *args): return _gnublin.gnublin_module_step_setMotorParam(self, *args)
    def hardStop(self): return _gnublin.gnublin_module_step_hardStop(self)
    def softStop(self): return _gnublin.gnublin_module_step_softStop(self)
    def resetPosition(self): return _gnublin.gnublin_module_step_resetPosition(self)
    def setPosition(self, *args): return _gnublin.gnublin_module_step_setPosition(self, *args)
    def getSwitch(self): return _gnublin.gnublin_module_step_getSwitch(self)
    def getActualPosition(self): return _gnublin.gnublin_module_step_getActualPosition(self)
    def drive(self, *args): return _gnublin.gnublin_module_step_drive(self, *args)
    def getMotionStatus(self): return _gnublin.gnublin_module_step_getMotionStatus(self)
    def getErrorMessage(self): return _gnublin.gnublin_module_step_getErrorMessage(self)
    __swig_destroy__ = _gnublin.delete_gnublin_module_step
    __del__ = lambda self : None;
gnublin_module_step_swigregister = _gnublin.gnublin_module_step_swigregister
gnublin_module_step_swigregister(gnublin_module_step)

LCD_EN = _gnublin.LCD_EN
LCD_RS = _gnublin.LCD_RS
LCD_RW = _gnublin.LCD_RW
LCD_BOOTUP_MS = _gnublin.LCD_BOOTUP_MS
LCD_ENABLE_US = _gnublin.LCD_ENABLE_US
LCD_WRITEDATA_US = _gnublin.LCD_WRITEDATA_US
LCD_COMMAND_US = _gnublin.LCD_COMMAND_US
LCD_SOFT_RESET_MS = _gnublin.LCD_SOFT_RESET_MS
LCD_SET_8BITMODE_MS = _gnublin.LCD_SET_8BITMODE_MS
LCD_CLEAR_DISPLAY_MS = _gnublin.LCD_CLEAR_DISPLAY_MS
LCD_CURSOR_HOME_MS = _gnublin.LCD_CURSOR_HOME_MS
LCD_DDADR_LINE1 = _gnublin.LCD_DDADR_LINE1
LCD_DDADR_LINE2 = _gnublin.LCD_DDADR_LINE2
LCD_DDADR_LINE3 = _gnublin.LCD_DDADR_LINE3
LCD_DDADR_LINE4 = _gnublin.LCD_DDADR_LINE4
LCD_CLEAR_DISPLAY = _gnublin.LCD_CLEAR_DISPLAY
LCD_CURSOR_HOME = _gnublin.LCD_CURSOR_HOME
LCD_SET_ENTRY = _gnublin.LCD_SET_ENTRY
LCD_ENTRY_DECREASE = _gnublin.LCD_ENTRY_DECREASE
LCD_ENTRY_INCREASE = _gnublin.LCD_ENTRY_INCREASE
LCD_ENTRY_NOSHIFT = _gnublin.LCD_ENTRY_NOSHIFT
LCD_ENTRY_SHIFT = _gnublin.LCD_ENTRY_SHIFT
LCD_SET_DISPLAY = _gnublin.LCD_SET_DISPLAY
LCD_DISPLAY_OFF = _gnublin.LCD_DISPLAY_OFF
LCD_DISPLAY_ON = _gnublin.LCD_DISPLAY_ON
LCD_CURSOR_OFF = _gnublin.LCD_CURSOR_OFF
LCD_CURSOR_ON = _gnublin.LCD_CURSOR_ON
LCD_BLINKING_OFF = _gnublin.LCD_BLINKING_OFF
LCD_BLINKING_ON = _gnublin.LCD_BLINKING_ON
LCD_SET_SHIFT = _gnublin.LCD_SET_SHIFT
LCD_CURSOR_MOVE = _gnublin.LCD_CURSOR_MOVE
LCD_DISPLAY_SHIFT = _gnublin.LCD_DISPLAY_SHIFT
LCD_SHIFT_LEFT = _gnublin.LCD_SHIFT_LEFT
LCD_SHIFT_RIGHT = _gnublin.LCD_SHIFT_RIGHT
LCD_SET_FUNCTION = _gnublin.LCD_SET_FUNCTION
LCD_FUNCTION_4BIT = _gnublin.LCD_FUNCTION_4BIT
LCD_FUNCTION_8BIT = _gnublin.LCD_FUNCTION_8BIT
LCD_FUNCTION_1LINE = _gnublin.LCD_FUNCTION_1LINE
LCD_FUNCTION_2LINE = _gnublin.LCD_FUNCTION_2LINE
LCD_FUNCTION_5X7 = _gnublin.LCD_FUNCTION_5X7
LCD_FUNCTION_5X10 = _gnublin.LCD_FUNCTION_5X10
LCD_SOFT_RESET = _gnublin.LCD_SOFT_RESET
LCD_SET_DDADR = _gnublin.LCD_SET_DDADR
class gnublin_module_lcd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_lcd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_lcd, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_lcd()
        try: self.this.append(this)
        except: self.this = this
    def getErrorMessage(self): return _gnublin.gnublin_module_lcd_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_module_lcd_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_module_lcd_setAddress(self, *args)
    def setDevicefile(self, *args): return _gnublin.gnublin_module_lcd_setDevicefile(self, *args)
    def out(self, *args): return _gnublin.gnublin_module_lcd_out(self, *args)
    def sendData(self, *args): return _gnublin.gnublin_module_lcd_sendData(self, *args)
    def command(self, *args): return _gnublin.gnublin_module_lcd_command(self, *args)
    def clear(self): return _gnublin.gnublin_module_lcd_clear(self)
    def home(self): return _gnublin.gnublin_module_lcd_home(self)
    def setdisplay(self, *args): return _gnublin.gnublin_module_lcd_setdisplay(self, *args)
    def setcursor(self, *args): return _gnublin.gnublin_module_lcd_setcursor(self, *args)
    def string(self, *args): return _gnublin.gnublin_module_lcd_string(self, *args)
    def init(self): return _gnublin.gnublin_module_lcd_init(self)
    __swig_destroy__ = _gnublin.delete_gnublin_module_lcd
    __del__ = lambda self : None;
gnublin_module_lcd_swigregister = _gnublin.gnublin_module_lcd_swigregister
gnublin_module_lcd_swigregister(gnublin_module_lcd)

class gnublin_module_dac(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_module_dac, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_module_dac, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gnublin.new_gnublin_module_dac()
        try: self.this.append(this)
        except: self.this = this
    def getErrorMessage(self): return _gnublin.gnublin_module_dac_getErrorMessage(self)
    def fail(self): return _gnublin.gnublin_module_dac_fail(self)
    def setAddress(self, *args): return _gnublin.gnublin_module_dac_setAddress(self, *args)
    def read(self, *args): return _gnublin.gnublin_module_dac_read(self, *args)
    def gain(self, *args): return _gnublin.gnublin_module_dac_gain(self, *args)
    def gainEeprom(self, *args): return _gnublin.gnublin_module_dac_gainEeprom(self, *args)
    def vRef(self, *args): return _gnublin.gnublin_module_dac_vRef(self, *args)
    def vRefEeprom(self, *args): return _gnublin.gnublin_module_dac_vRefEeprom(self, *args)
    def writeAll(self, *args): return _gnublin.gnublin_module_dac_writeAll(self, *args)
    def write(self, *args): return _gnublin.gnublin_module_dac_write(self, *args)
    def writeEeprom(self, *args): return _gnublin.gnublin_module_dac_writeEeprom(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_module_dac
    __del__ = lambda self : None;
gnublin_module_dac_swigregister = _gnublin.gnublin_module_dac_swigregister
gnublin_module_dac_swigregister(gnublin_module_dac)


def base64_encode(*args):
  return _gnublin.base64_encode(*args)
base64_encode = _gnublin.base64_encode

def base64_decode(*args):
  return _gnublin.base64_decode(*args)
base64_decode = _gnublin.base64_decode
SOCKET_ERROR = _gnublin.SOCKET_ERROR
INVALID_SOCKET = _gnublin.INVALID_SOCKET
TIME_IN_SEC = _gnublin.TIME_IN_SEC
BUFFER_SIZE = _gnublin.BUFFER_SIZE
MSG_SIZE_IN_MB = _gnublin.MSG_SIZE_IN_MB
COUNTER_VALUE = _gnublin.COUNTER_VALUE
XPRIORITY_HIGH = _gnublin.XPRIORITY_HIGH
XPRIORITY_NORMAL = _gnublin.XPRIORITY_NORMAL
XPRIORITY_LOW = _gnublin.XPRIORITY_LOW
class gnublin_smtp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_smtp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_smtp, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _gnublin.delete_gnublin_smtp
    __del__ = lambda self : None;
    def AddRecipient(self, *args): return _gnublin.gnublin_smtp_AddRecipient(self, *args)
    def AddBCCRecipient(self, *args): return _gnublin.gnublin_smtp_AddBCCRecipient(self, *args)
    def AddCCRecipient(self, *args): return _gnublin.gnublin_smtp_AddCCRecipient(self, *args)
    def AddAttachment(self, *args): return _gnublin.gnublin_smtp_AddAttachment(self, *args)
    def AddMsgLine(self, *args): return _gnublin.gnublin_smtp_AddMsgLine(self, *args)
    def DelRecipients(self): return _gnublin.gnublin_smtp_DelRecipients(self)
    def DelBCCRecipients(self): return _gnublin.gnublin_smtp_DelBCCRecipients(self)
    def DelCCRecipients(self): return _gnublin.gnublin_smtp_DelCCRecipients(self)
    def DelAttachments(self): return _gnublin.gnublin_smtp_DelAttachments(self)
    def DelMsgLines(self): return _gnublin.gnublin_smtp_DelMsgLines(self)
    def DelMsgLine(self, *args): return _gnublin.gnublin_smtp_DelMsgLine(self, *args)
    def ModMsgLine(self, *args): return _gnublin.gnublin_smtp_ModMsgLine(self, *args)
    def GetBCCRecipientCount(self): return _gnublin.gnublin_smtp_GetBCCRecipientCount(self)
    def GetCCRecipientCount(self): return _gnublin.gnublin_smtp_GetCCRecipientCount(self)
    def GetRecipientCount(self): return _gnublin.gnublin_smtp_GetRecipientCount(self)
    def GetLocalHostName(self): return _gnublin.gnublin_smtp_GetLocalHostName(self)
    def GetMsgLineText(self, *args): return _gnublin.gnublin_smtp_GetMsgLineText(self, *args)
    def GetMsgLines(self): return _gnublin.gnublin_smtp_GetMsgLines(self)
    def GetReplyTo(self): return _gnublin.gnublin_smtp_GetReplyTo(self)
    def GetMailFrom(self): return _gnublin.gnublin_smtp_GetMailFrom(self)
    def GetSenderName(self): return _gnublin.gnublin_smtp_GetSenderName(self)
    def GetSubject(self): return _gnublin.gnublin_smtp_GetSubject(self)
    def GetXMailer(self): return _gnublin.gnublin_smtp_GetXMailer(self)
    def GetXPriority(self): return _gnublin.gnublin_smtp_GetXPriority(self)
    def Send(self): return _gnublin.gnublin_smtp_Send(self)
    def SetSubject(self, *args): return _gnublin.gnublin_smtp_SetSubject(self, *args)
    def SetSenderName(self, *args): return _gnublin.gnublin_smtp_SetSenderName(self, *args)
    def SetSenderMail(self, *args): return _gnublin.gnublin_smtp_SetSenderMail(self, *args)
    def SetReplyTo(self, *args): return _gnublin.gnublin_smtp_SetReplyTo(self, *args)
    def SetXMailer(self, *args): return _gnublin.gnublin_smtp_SetXMailer(self, *args)
    def SetLogin(self, *args): return _gnublin.gnublin_smtp_SetLogin(self, *args)
    def SetPassword(self, *args): return _gnublin.gnublin_smtp_SetPassword(self, *args)
    def SetXPriority(self, *args): return _gnublin.gnublin_smtp_SetXPriority(self, *args)
    def SetSMTPServer(self, *args): return _gnublin.gnublin_smtp_SetSMTPServer(self, *args)
    CSMTP_NO_ERROR = _gnublin.gnublin_smtp_CSMTP_NO_ERROR
    WSA_STARTUP = _gnublin.gnublin_smtp_WSA_STARTUP
    WSA_VER = _gnublin.gnublin_smtp_WSA_VER
    WSA_SEND = _gnublin.gnublin_smtp_WSA_SEND
    WSA_RECV = _gnublin.gnublin_smtp_WSA_RECV
    WSA_CONNECT = _gnublin.gnublin_smtp_WSA_CONNECT
    WSA_GETHOSTBY_NAME_ADDR = _gnublin.gnublin_smtp_WSA_GETHOSTBY_NAME_ADDR
    WSA_INVALID_SOCKET = _gnublin.gnublin_smtp_WSA_INVALID_SOCKET
    WSA_HOSTNAME = _gnublin.gnublin_smtp_WSA_HOSTNAME
    WSA_IOCTLSOCKET = _gnublin.gnublin_smtp_WSA_IOCTLSOCKET
    WSA_SELECT = _gnublin.gnublin_smtp_WSA_SELECT
    BAD_IPV4_ADDR = _gnublin.gnublin_smtp_BAD_IPV4_ADDR
    UNDEF_MSG_HEADER = _gnublin.gnublin_smtp_UNDEF_MSG_HEADER
    UNDEF_MAIL_FROM = _gnublin.gnublin_smtp_UNDEF_MAIL_FROM
    UNDEF_SUBJECT = _gnublin.gnublin_smtp_UNDEF_SUBJECT
    UNDEF_RECIPIENTS = _gnublin.gnublin_smtp_UNDEF_RECIPIENTS
    UNDEF_LOGIN = _gnublin.gnublin_smtp_UNDEF_LOGIN
    UNDEF_PASSWORD = _gnublin.gnublin_smtp_UNDEF_PASSWORD
    UNDEF_RECIPIENT_MAIL = _gnublin.gnublin_smtp_UNDEF_RECIPIENT_MAIL
    COMMAND_MAIL_FROM = _gnublin.gnublin_smtp_COMMAND_MAIL_FROM
    COMMAND_EHLO = _gnublin.gnublin_smtp_COMMAND_EHLO
    COMMAND_AUTH_LOGIN = _gnublin.gnublin_smtp_COMMAND_AUTH_LOGIN
    COMMAND_DATA = _gnublin.gnublin_smtp_COMMAND_DATA
    COMMAND_QUIT = _gnublin.gnublin_smtp_COMMAND_QUIT
    COMMAND_RCPT_TO = _gnublin.gnublin_smtp_COMMAND_RCPT_TO
    MSG_BODY_ERROR = _gnublin.gnublin_smtp_MSG_BODY_ERROR
    CONNECTION_CLOSED = _gnublin.gnublin_smtp_CONNECTION_CLOSED
    SERVER_NOT_READY = _gnublin.gnublin_smtp_SERVER_NOT_READY
    SERVER_NOT_RESPONDING = _gnublin.gnublin_smtp_SERVER_NOT_RESPONDING
    SELECT_TIMEOUT = _gnublin.gnublin_smtp_SELECT_TIMEOUT
    FILE_NOT_EXIST = _gnublin.gnublin_smtp_FILE_NOT_EXIST
    MSG_TOO_BIG = _gnublin.gnublin_smtp_MSG_TOO_BIG
    BAD_LOGIN_PASS = _gnublin.gnublin_smtp_BAD_LOGIN_PASS
    UNDEF_XYZ_RESPONSE = _gnublin.gnublin_smtp_UNDEF_XYZ_RESPONSE
    LACK_OF_MEMORY = _gnublin.gnublin_smtp_LACK_OF_MEMORY
    TIME_ERROR = _gnublin.gnublin_smtp_TIME_ERROR
    RECVBUF_IS_EMPTY = _gnublin.gnublin_smtp_RECVBUF_IS_EMPTY
    SENDBUF_IS_EMPTY = _gnublin.gnublin_smtp_SENDBUF_IS_EMPTY
    OUT_OF_MSG_RANGE = _gnublin.gnublin_smtp_OUT_OF_MSG_RANGE
    def __init__(self, *args): 
        this = _gnublin.new_gnublin_smtp(*args)
        try: self.this.append(this)
        except: self.this = this
    def GetErrorNum(self): return _gnublin.gnublin_smtp_GetErrorNum(self)
    def GetErrorText(self): return _gnublin.gnublin_smtp_GetErrorText(self)
gnublin_smtp_swigregister = _gnublin.gnublin_smtp_swigregister
gnublin_smtp_swigregister(gnublin_smtp)
cvar = _gnublin.cvar
BOUNDARY_TEXT = cvar.BOUNDARY_TEXT

class gnublin_csv(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gnublin_csv, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gnublin_csv, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gnublin.new_gnublin_csv(*args)
        try: self.this.append(this)
        except: self.this = this
    def open(self, *args): return _gnublin.gnublin_csv_open(self, *args)
    def addRow(self, *args): return _gnublin.gnublin_csv_addRow(self, *args)
    def close(self): return _gnublin.gnublin_csv_close(self)
    def delimiterRow(self, *args): return _gnublin.gnublin_csv_delimiterRow(self, *args)
    def delimiterColumn(self, *args): return _gnublin.gnublin_csv_delimiterColumn(self, *args)
    def delimiterField(self, *args): return _gnublin.gnublin_csv_delimiterField(self, *args)
    __swig_destroy__ = _gnublin.delete_gnublin_csv
    __del__ = lambda self : None;
gnublin_csv_swigregister = _gnublin.gnublin_csv_swigregister
gnublin_csv_swigregister(gnublin_csv)

# This file is compatible with both classic and new-style classes.


