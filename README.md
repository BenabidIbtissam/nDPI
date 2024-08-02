# nDPI
Here is a documentation for installing and using nDPI on a Linux machine:

---

### Installing and Using nDPI on a Linux Machine

#### Prerequisites

1. **Install Required Packages**
   ```sh
   sudo apt-get install software-properties-common wget
   ```

2. **Add the Universe Repository**
   ```sh
   sudo add-apt-repository universe
   ```

#### Installation

1. **Download and Install the ntop Package**
   ```sh
   sudo wget https://packages.ntop.org/apt/22.04/all/apt-ntop.deb
   sudo apt install ./apt-ntop.deb
   ```

2. **Clean and Update Package Lists**
   ```sh
   sudo apt-get clean all
   sudo apt-get update
   ```

3. **Install nDPI and Dependencies**
   ```sh
   sudo apt-get install pfring-dkms nprobe ntopng n2disk cento ntap
   ```

#### Verify Installation

1. **Check nDPI Version**
   ```sh
   ndpiReader -v
   ```

2. **Check Network Interfaces**
   ```sh
   ifconfig -a
   ip link show
   ```

#### Using nDPI

1. **Capture Network Traffic**
   ```sh
   sudo ndpiReader -i wlp1s0 -w test_capture.pcap
   ```

2. **Filter TCP Traffic on Port 80**
   ```sh
   sudo ndpiReader -i wlp1s0 -f "tcp port 80"
   ```

---

This guide provides a step-by-step process to install and use nDPI on a Linux machine, ensuring that each command is clear and well-formatted for ease of use.
