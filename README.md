# nDPI
Here is a documentation for installing and using nDPI on a Linux machine:

---

### Installing and Using nDPI on a Linux Machine

#### Prerequisites

**Install Required Packages**
   
   ```sh
   sudo apt-get install build-essential git gettext flex bison libtool autoconf automake pkg-config libpcap-dev libjson-c-dev libnuma-dev libpcre2-dev libmaxminddb-dev librrd-dev   ```
   ```

#### Installation and Compilation

**Clone Repository**
   
   ```sh
   git clone https://github.com/ntop/nDPI.git
   ```

**Compile project**
   
   ```sh
    ./autogen.sh
    make

   ```

**Clean and Update Package Lists**
   
   ```sh
   sudo apt-get clean all
   sudo apt-get update
   ```

#### Verify Installation

**Check nDPI Version**
   ```sh
   ndpiReader -v
   ```

**Check Network Interfaces**
   ```sh
   ifconfig -a
   ip link show
   ```

#### Using nDPI

**Capture Network Traffic**
   ```sh
   sudo ndpiReader -i wlp1s0 -w test_capture.pcap
   ```

**Filter TCP Traffic on Port 80**
   ```sh
   sudo ndpiReader -i wlp1s0 -f "tcp port 80"
   ```

#### Running from python script 

**Install python**
   
```sh
sudo apt install python3
```

**Install pyshark**
   
```sh
sudo apt-get install tshark
```

**Run the scrip**

```sh
/usr/bin/python3 script.py      
```

