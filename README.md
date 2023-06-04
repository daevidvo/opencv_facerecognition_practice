# OpenCV Simple Facial Recognition

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Technology Used 🖥️

| Technology Used         | Resource URL           | 
| ------------- |:-------------:| 
| Python | [https://www.python.org/](https://www.python.org/) |
| OpenCV | [https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html) |
| pip | [https://pypi.org/project/pip/](https://pypi.org/project/pip/) |
| Git | [https://git-scm.com/](https://git-scm.com/)     |  


---

## Description 📝

This is a simple facial recognition program using OpenCV and [its datasets found here](https://github.com/opencv/opencv/tree/master/data/haarcascades).

There is recognition for a front-on looking face, face profile, smile, and eyes in this program.

![example of app](./assets/images/example.gif)

-----------------------

## Table of Contents 📋
* [Installation Instructions](#installation-instructions-📥)
* [Usage Information](#usage-information-✅)
* [Author Info](#author-info-👺)
* [Questions?](#questions-❓)
* [License](#license-🚩)

----------------------

## Installation Instructions 📥

To install this program, follow the steps below:

1. Download/clone the contents of this repo on to your local machine

------------------------

## Usage Information ✅

1. Open main.py
2. Change the `2` in ```cam = cv2.VideoCapture(2)``` to whatever number your webcam is.
3. Uncomment the eyes_cascade or smile_cascade along with its corresponding detectMultiScale and for loop if you'd like.

------------------------

## Bugs 🕷

- Profile dataset doesn't seem to like it when you face to the left. Need to find a better dataset for face
- Smiles dataset makes a lot of false positives. Need to tweak its detectMultiScale and find a better dataset.

------------------------

## Author Info 👺

### ***daevidvo***
* [Github](https://www.github.com/daevidvo)
* [LinkedIn](https://www.linkedin.com/in/daevidvo)
* [Instagram](https://www.instagram.com/daevidvo)

--------------------------

## Questions ❓

Email me at: [daevidvo@gmail.com](mailto:daevidvo@gmail.com) or [visit my GitHub](https://www.github.com/daevidvo)

------------------------

## License 🚩

https://opensource.org/licenses/MIT


The MIT License (MIT)
=====================

Copyright © daevidvo

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
