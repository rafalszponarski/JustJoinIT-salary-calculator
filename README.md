# justjoin.it salary calculator
This project is designed to calculate minimum, maximum, and average earnings on the justjoin.it website.
The user can select a profession, level of experience, and type of employment, and then receive information about earnings for the selected combination.
The project uses the Selenium library to automatically browse web pages and the re library to search for text. 
It is intended for users wanting to check market rates for their services

## Install
Install the required libraries from the requirements.txt file using the following command:
`pip install -r requirements.txt`

Download the latest version of chromedriver from https://chromedriver.chromium.org/downloads and place it in the appropriate directory on your computer. 
Make sure to download the version that matches the version of Chrome you have installed.

You need chromium browser to run the program: 
- For windows, I recommend: https://github.com/Hibbiki/chromium-win64 | `winget install Hibbiki.Chromium`

- For linux packet should be in sources, e.g. `sudo apt install -y chromium-browser`

- Manually install: https://www.chromium.org/getting-involved/download-chromium/


## Usage
Program can be started by executing the following command: `python3 calculator.py`
or using optional arguments e.g. `python3 calculator.py --emp b2b --exp mid --prof python`.


If You want to store permanent value like profession, You can edit this in code. Example:

original line: `prof = '' if not args.prof else args.prof  # You can set is as permanent value. Use one of values in professions`

line with permanent value `prof = 'python' if not args.prof else args.prof  # You can set is as permanent value. Use one of values in professions`

Then just omit the relevant parameter e.g. `python3 calculator.py --emp b2b --exp mid`

Remember the proper nomenclature! For more information run `python3 calculator.py -h`
