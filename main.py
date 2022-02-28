import datetime
import time
from multiprocessing import Process, Value

import serial
from scipy.stats import mode

from human_detection import HumanCounter

if __name__ == '__main__':
    # # establish a serial connection to arduino
    # arduino = serial.Serial('com3', 9600)

    # instantiate human counter class
    h_count = HumanCounter()

    # receive human count
    child_conn1 = Value('d', 0)
    p1 = Process(target=h_count.run_count, args=(child_conn1,))
    p1.start()

    # pass num humans to arduino board every 10 seconds
    time_1 = time.time()
    time_2 = time.time()
    count_list = []
    while True:
        time_3 = time.time()

        if time_3 >= (time_1+2):  # human count taken every 2 sec
            num_humans = child_conn1.value
            count_list.append(num_humans)
            time_1 = time.time()

        if time_3 >= (time_2+10):  # mode of human count taken every 10 sec
            print(count_list)

            count_mode = mode(count_list)[0][0]
            # arduino.write(f'H, {count_mode}')

            print('time: ', datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
            print('number of humans: ', count_mode)
            print()

            # update time and clear list
            time_2 = time.time()
            count_list.clear()
