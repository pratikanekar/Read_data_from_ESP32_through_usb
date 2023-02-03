from loguru import logger
import serial

# following object is used to for serial communication
serial_reader = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
logger.info(f"Program is started ...")

read_esp32 = serial_reader.read(1024)
if len(read_esp32) > 0:
    try:
        received_data_from_esp32 = read_esp32.hex()
        print(received_data_from_esp32)
    except Exception as e:
        logger.debug(f"Error on Data: {read_esp32}")
else:
    logger.debug(f"No Data Found")

# send_data = bytes.fromhex()
