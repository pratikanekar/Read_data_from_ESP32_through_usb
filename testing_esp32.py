from pymodbus.pdu import ModbusRequest
from pymodbus.client.serial import ModbusSerialClient

read_client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', stopbits=1, bytesize=8, parity='N', baudrate=9600)

# create serial connection for esp32
connect = read_client.connect()
print(connect)

#
coil = read_client.read_discrete_inputs(address=1, count=16, unit=1)
print(coil)
