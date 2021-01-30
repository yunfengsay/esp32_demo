from umqtt.simple import MQTTClient
import time
import json

def init_mqtt():
    try:
        with open('mqtt_config.json','r') as f:
            config = json.loads(f.read())
    # 若初次运行,则将进入excpet,执行配置文件的创建        
    except:
        essid = ''
        password = ''
    print('config')
    client = MQTTClient(config['client_id'], config['server'])
    client.set_callback(mqtt_callback)
    client.connect()
    print('connect mqtt success')
    client.subscribe(config['topic'])
    while True:
        # 查看是否有数据传入
        # 有的话就执行 mqtt_callback
        client.check_msg()
        time.sleep(1)

def mqtt_callback(topic, msg):
    try:

        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        try:
            msg_json = json.loads(msg)
        except:
            print('error: msg is not json')
            msg_json = {}
        if msg_json.get("code") is not None:
            code = msg_json.get("code")
            file_name = msg_json.get('save_name')
            is_exec = msg_json.get('is_exec')
            if is_exec == 'True':
                cc = compile(code, 'mqtt_eval_temp', 'single')
                exec(cc)
            if file_name is not None:
                with open(file_name + '.py', 'r') as f:
                    f.write(code)
        if msg_json.get('open_led') is not None:
            print('open_led')
    except Exception as e:
        print(e)

