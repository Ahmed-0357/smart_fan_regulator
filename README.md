<h1 align="center"> <b>Smart Fan Regulator With Computer Vision</b></h1>

- According to [World Energy Outlook (WEO)](https://www.iea.org/reports/world-energy-outlook-2019/electricity), electricity demand is projected to grow at 2.1% per year until 2040, and this will raise more environmental and economical challenges.

- Therefore, I would like to present this prototype of a smart ceiling fan regulator which can help to reduce electricity consumption in public places (e.g, restaurants, laundry shops, and train stations).

- The smart regulator receives the video feed from CCTV camera(s) to detect the number of individuals present, also it has a built-in sensor to measure the surrounding temperature.

- Then the regulator utilizes these two pieces of information to switch on the fan and control its speed.

---

<p align="center">
  <img src=./demo/picture1.gif alt="animated" />
</p>

---

<h2><b> How to run this project </b><img src="https://emojis.slackmojis.com/emojis/images/1600706728/10521/meow_code.gif?1600706728" width="25"/> </h2>

### **1. Hardware**

<p align="center">
  <img src=./demo/schematic.png alt="animated" />
</p>

### **2. Code**

- Upload the arduino code
  `./arduino/controllerapp.ino` to the UNO board ([info](https://www.dummies.com/article/technology/computers/hardware/arduino/how-to-upload-a-sketch-to-an-arduino-164738)).

- Run main.py from the command line.

```console
$ python main.py
```

<p align="center">
  <img src=./demo/picture2.png alt="animated" />
</p>

---

<h2><b> Authors </b></h2>

- [Ahmed Abdulrahman](https://github.com/Ahmed-0357)
