import dht
import json
import machine
import micropython
from machine import Pin
from machine import Timer
from simple import MQTTClient


# 继电器定义为0引脚
p0 = Pin(0, Pin.OUT)
# 定义温湿度检测对象为p5
p5 = machine.Pin(5)
# 实例化adc对象以方便获取一氧化碳值
adc = machine.ADC(0)   

def pubdata(data):
    """ 组合成协议要求的报文格式 """
    j_d = json.dumps(data)
    j_l = len(j_d)
    arr = bytearray(j_l + 3)
    arr[0] = 1 
    arr[1] = int(j_l / 256) 
    arr[2] = j_l % 256      
    arr[3:] = j_d.encode('ascii') 
    return arr


# MQTT服务器地址域名为：183.230.40.39,不变
SERVER = "183.230.40.39"
#设备ID
CLIENT_ID = "606535869"
#随便起个名字
TOPIC = b"tpyboardV202"
#产品ID
username='356831'
#产品APIKey:
password='ZB=te7OdfUlUnxw7oXt2Nw5WXDE='


# 控制继电器
def sub_cb(topic, msg):
    print(msg)
    print((topic, msg))
    if msg == b"0":
        p0.off()
        print("The current status is OFF")
    elif msg == b"1":
        p0.on()
        print("The current status is ON")
    elif msg == b"toggle":
        p0.off()
        print("The current status is OFF")

def main(server=SERVER):
    #端口号为：6002
    c = MQTTClient(CLIENT_ID, server,6002,username,password)

    # 控制开关
    c.set_callback(sub_cb)

    c.connect()

    # 数据推送
    def upload_temperature_humidity(temp):
        # 温湿度测量
        data = dht.DHT11(p5)
        data.measure()
        temperature = data.temperature()
        humidity = data.humidity()

        # 一氧化碳测量
        Carbon_monoxide = adc.read()

        message = {
            'datastreams':[
                {
                    'id':'humidity',
                    'datapoints':[
                        {'value':humidity}
                    ]
                },
                {
                    'id':'temperature',
                    'datapoints':[
                        {'value':temperature}
                    ]
                },
                {
                    'id':'Carbon_monoxide',
                    'datapoints':[
                        {'value':Carbon_monoxide}
                    ]
                }
            ]
        }

        c.publish('$dp',pubdata(message))
        print('publish message:',message)
    temperature_humidity_tim = Timer(-1)  # 新建一个虚拟定时器 温湿度定时器
    # temperature_humidity_tim.init(period=5000, mode=Timer.ONE_SHOT, callback=upload_temperature_humidity)
    temperature_humidity_tim.init(period=5000, mode=Timer.PERIODIC, callback=upload_temperature_humidity)

    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    try:
        while True:
            c.wait_msg()
            
    finally:
        c.disconnect()
