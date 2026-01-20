# Random Number Generator using Fractals and Logistic Maps

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Python version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

This repository contains a random number generator inspired by logistic map and evolution of random fractals. Although this RNG generates integers only, the code can be tweaked to generate random numbers in whatever range one wants.

---

## Table of Contents


- [Getting Started: Using the Code](#getting-started-using-the-code)
- [Verification using STS](#verification-using-sts)

---


## Getting Started: Using the Code

### Prerequisites

- Python 3.6+

### Installation
Clone the repository

```bash
git clone https://github.com/paulpseudoman/Random-Number-Generator.git
cd Random-Number-Generator
```
### Using the repository
Now you can browse through the codes to understand the working principle, can execute the codes to get desired outputs. The codes can be modified to generate random number in your desired range. You can test how _random_ the numbers really are using [NIST SP 800-22](https://csrc.nist.gov/Projects/Random-Bit-Generation/Documentation-and-Software). A sample of the report provided by the software and the `rngtest.txt` testfile containing 20 bitstreams, each stream containing 1000000 bits is present in this repository

## Verification using STS
The NIST Statistical Test Suite (STS) is primarily created for linux. One can also use _Windows Subsystem for Linux_ to use this tool. Run the following codes in your linux terminal to get the desired result.

1. Go to your `$HOME` directory (optional, but I would prefer doing this). Also install `unzip`.

```bash
cd $HOME
sudo apt install build-essential gcc make unzip wget
```

2. Download the test suite and unzip it.

```bash
 wget https://csrc.nist.gov/CSRC/media/Projects/Random-Bit-Generation/documents/sts-2_1_2.zip
 unzip sts-2_1_2.zip
```
3. Go to the directory and install the software.

```bash
 cd sts-2.1.2
 cd sts-2.1.2
 make
```

 4. Copy the `rngtest.txt` file to the `data` directory of the current folder (This is for _Windows Subsystem for Linux_, for other setup, modify it accordingly).

 ```bash
 cp /mnt/c/Users/asus/Documents/rngtest.txt ~/sts-2.1.2/sts-2.1.2/data/

 ```

 5. Run the `assess` executable and choose the suitable options. Specify number of beats per beatstream.

 ```bash
 ./assess 1000000
 ```

 6. choose `0` and enter the prescribed input file

 ```bash
 G E N E R A T O R    S E L E C T I O N
           ______________________________________

    [0] Input File                 [1] Linear Congruential
    [2] Quadratic Congruential I   [3] Quadratic Congruential II
    [4] Cubic Congruential         [5] XOR
    [6] Modular Exponentiation     [7] Blum-Blum-Shub
    [8] Micali-Schnorr             [9] G Using SHA-1

   Enter Choice: 0


                User Prescribed Input File: data/rngtest.txt
```

7. Applying all the statistical tests is advised, press `1` to do so. If you do not want to do so, press `0`, and follow the instructions (write `0` for the tests you do NOT want, and `1` for the tests you DO want to perform sequentially).

8. Changing the parameters is NOT advised. Type `0` to continue.

9. Specify the _number of bitstreams_ (`20` in this case).

10. Select `0` for _input mode_(ASCII in this case).

11. When you see the message `Statistical Testing Complete!!!!!!!!!!!!`, execute the following command, and view the result.
```bash
cat experiments/AlgorithmTesting/finalAnalysisReport.txt
```
