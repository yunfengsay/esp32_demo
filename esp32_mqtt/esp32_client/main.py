from wifi_connector import do_connect
from mqtt_subscriber import init_mqtt
# import web

if __name__ == '__main__':
    do_connect()
    
    # after init_mqtt ,code while not be called because while True in init_mqtt func.
    init_mqtt()
    

