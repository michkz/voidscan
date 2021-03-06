<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  ![logo](https://user-images.githubusercontent.com/17614548/173921014-8d5b005b-0266-4484-b426-dc15eb399309.png)
</div>

<h1 align="center">A Blackbox Reconnaissance Tool</h1>

<p align="center">
  <a href="https://python.org/">
    <img src="https://img.shields.io/badge/Python-3.8-%23defaff.svg?style=for-the-badge">
  </a>
    <a href="https://github.com/michkz/voidscan/releases">
    <img src="https://img.shields.io/badge/Release-v1-%23cfe9ee.svg?style=for-the-badge">
  </a>
  <a href="https://github.com/michkz/voidscan/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-%23cbe1e7.svg?style=for-the-badge">
  </a>
    <a href="https://opensource.org">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-%23b9d0d4.svg?style=for-the-badge">
  </a>
</p>

<p align="center">
  Voidscan is a free and open-source Blackbox Reconnaissance Tool that gathers information about a given scope.
</p>

<br />

## Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

<!-- TABLE OF CONTENTS -->

### Table of contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

The goal of this project is to fully automate the reconnaissance phase when conducting a penetration test. It uses a textfile which contains an asset per line to scan through a number of tools. Once the program is done scanning, the gathered results will be presented in the form of a markdown report.

This started as an internship assignment, but will be updated regulary with new tools and code improvements.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you can use this program, make sure you have Python 3.8 or higher installed.

##### MacOS

```bash
$ brew install python@3.8
```

##### Windows

Download the right Python version from the [Official Website](https://www.python.org/downloads/windows/)

##### Unix/Linux

```bash
$ sudo apt-get install python3.8
```

### Installation

#### 1. Get the repository

```bash
$ git clone https://github.com/michkz/voidscan
```

#### 2. Go into the repository

```bash
$ cd voidscan/
```

#### 3. Install the requirements

```bash
$ pip install -r requirements.txt
```

#### 4. Run the program

```bash
$ python3.8 main.py -f [file.txt]
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

To use the program, simply go into the project's folder and use the following command

```bash
$ python3.8 main.py -f [file.txt]
```

Where ` [file.txt]` has an asset per line, like in the example below

```bash
# Example of the file.txt contents
127.0.0.1
http://zonetransfer.me/
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Features

At the moment the current version consists of the following tools that have a checkmark in the table below. The planned tools are marked with a date or are still TBD

| Tool        | Status |
| :---------- | :----: |
| `Host`      |   ???    |
| `Curl`      |   ???    |
| `Nmap`      |   ???    |
| `Dirbuster` |  TBD   |

#### Host

The host tool allows to collect IPv4, IPv6 and mail server addresses, as well as DNS zonetransfer information if possible. It will use the following commands within this program

```
# Where asset will be retrieved from the scope.
host [asset]
```

```
# Where asset will be retrieved from the scope.
host -t ns [asset]
```

```
# Where asset will be retrieved from the scope and the nameserver from the previous command.
host -t axfr [asset] [nameserver]
```

#### Curl

The curl tool allows to collect useful header information and will use the following commands within this program

```
# Where asset will be retrieved from the scope.
curl -I [asset]
```

#### Nmap

The nmap tool will collect the open ports and services. It will use the following commands within this program

```
# Where asset will be retrieved from the scope.
nmap [asset]
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Michkz - michkz@protonmail.com

Project Link: [https://github.com/michkz/voidscan](https://github.com/michkz/voidscan)

<p align="right">(<a href="#top">back to top</a>)</p>
