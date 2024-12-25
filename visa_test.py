import pyvisa
import time


if __name__ == "__main__":
    arduino = None
    # 建立 Resource Manager
    rm = pyvisa.ResourceManager("@py")

    # 列出所有可用資源
    print("Available resources:", rm.list_resources())

    # 連接至 Arduino 的 COM 埠
    try:

        arduino = rm.open_resource(rm.list_resources()[0])
        arduino.baud_rate = 9600  # 設置與 Arduino 一致的波特率
        arduino.data_bits = 8
        arduino.parity = pyvisa.constants.Parity.none
        arduino.stop_bits = pyvisa.constants.StopBits.one
        arduino.timeout = 5000  # 設置逾時為 5 秒
        time.sleep(2)

        # 發送資料並接收回應
        arduino.write("-a\n")
        time.sleep(1)
        response = arduino.read()
        print("Arduino responded:", response)
    except Exception as e:
        print("Error:", e)
    finally:
        if arduino:
            arduino.close()
