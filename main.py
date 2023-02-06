from pymodbus.client.serial import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from loguru import logger
from time import sleep

# following variable is used to find received val is little endian or big endian
order = [['little', 'little', Endian.Little, Endian.Little], ['little', 'big', Endian.Little, Endian.Big],
         ['big', 'little', Endian.Big, Endian.Little], ['big', 'big', Endian.Big, Endian.Big]]

# following object is used to for serial communication
client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=2
)
logger.info(f"Program is started ...")

try:
    # it is used for connecting using serial
    client.connect()
    print(client.connect())
    sleep(1)
    decode_type = "int"  # it is hard coded decode_type will be int or float
    size_bits = 32  # it is hard coded size_bits will be 16 or 32
    read_register = client.read_discrete_inputs(address=1, count=2, unit=1)  # it is used for reading input registers
    mod_read_list = read_register # it is used to store input register values
    logger.info(f"Connected Registers {mod_read_list}")
except ValueError:
    logger.error(f"Error with host or port")
except KeyboardInterrupt:
    logger.error(f"Found KeyBoard Interrupt,so EXIT Code")

#     decoded = []
#     for orders in order:
#         decoder = BinaryPayloadDecoder.fromRegisters(mod_read_list, byteorder=orders[2], wordorder=orders[
#             3])  # it is used for to find values are little endian or big endian
#         try:
#             receive_val = None
#             bits_size = size_bits
#             if decode_type == "int":
#                 if bits_size == 16:
#                     receive_val = decoder.decode_16bit_int()  # here receive actual value
#                 elif bits_size == 32:
#                     receive_val = decoder.decode_32bit_int()
#             final_dict = {}
#             final_dict.update({"word_order": orders[1], "byte_order": orders[0], "value": receive_val})
#             decoded.append(final_dict)
#         except Exception as e:
#             continue
#         logger.info(f"Receive Data {final_dict}")
#     # client.close()
# except ValueError:
#     logger.error(f"Error with host or port")
# except KeyboardInterrupt:
#     logger.error(f"Found KeyBoard Interrupt,so EXIT Code")

# send_esp32 = bytes.fromhex("01020000000879CC")
# serial_reader.write(send_esp32)
# logger.debug(f"send data to slave 1 successfully")
# read_esp32 = serial_reader.read(4096)
# logger.debug(f"received data from slave1 is:{read_esp32}")
# if len(read_esp32) > 0:
#     try:
#         received_data_from_esp32 = read_esp32.hex()
#         print(received_data_from_esp32)
#     except Exception as e:
#         logger.debug(f"Error on Data: {read_esp32}")
# else:
#     logger.debug(f"No Data Found")
#
# # send_data = bytes.fromhex()
