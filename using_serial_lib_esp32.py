import serial
from loguru import logger
from time import sleep

datas = [{"read_slave": f"01020000000879CC"},
         {"read_slave": f"02020000001079F5"}]
# {"read_slave": f"0302000000107824"},
# {"read_slave": f"0402000000107993"}]

serial_reader = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2
)
logger.info(f"connected successfully to serial port")


def read_esp32_slaves():
    i = 1
    for slaves in datas:
        try:
            send_esp32 = bytes.fromhex(slaves.get("read_slave"))
            serial_reader.write(send_esp32)
            send_data = slaves.get("read_slave")
            logger.info(f"send data to slave_{i} is:{send_data}")
            read_esp32 = serial_reader.read(4096)
            # logger.debug(f"received data from slave{i} is:{read_esp32}")
            if len(read_esp32) > 0:
                try:
                    received_data_from_esp32 = read_esp32.hex().upper()
                    logger.info(f"received data from slave_{i} is:{received_data_from_esp32}")
                except Exception as e:
                    logger.debug(f"Error on Data: {read_esp32}")
            else:
                logger.debug(f"No Data Found")
        except TimeoutError as e:
            logger.error(f"Error occurred  slave_{i}:{e}")
        except Exception as e:
            logger.error(f"Error occurred slave_{i}: {e}")
        finally:
            i = i + 1
            sleep(0.3)


if __name__ == '__main__':
    while True:
        try:
            read_esp32_slaves()
            sleep(0.1)
        except KeyboardInterrupt:
            print(f"Found KeyBoard Interrupt,so EXIT Code")
            break
