# isic_grabber
Downloads the ISIC Archive by dataset.

# Install

`pip install git+https://github.com/stamas02/isic_grabber`

# Usage

#### List ISIC Archive datasets
To list datasets available in the ISIC Archive run the following command in the terminal.

`ls_isic`

The current output in 14.July.2021 is:
`2018JIDEditorialImages,
BCN20000,
BCN2020Challenge
BrisbaneISICChallenge2020,
DermoscopediaCC0,
DermoscopediaCCBY,
DermoscopediaCCBYNC,
HAM10000,
ISIC2020ChallengeMSKCCcontribution,
ISIC2020Viennapart2,
ISIC2020Viennapart1,
MSK1,
MSK2,
MSK3,
MSK4,
MSK5,
SONIC,
SydneyMIASMDC2020ISICchallengecontribution,
UDA1,
UDA2,
`


#### Download ISIC Archive datasets

Using the list obtained from the ls_isic choose a dataset and then run:

`grab_isic DATASET -d /PATH/TO/THE/DESTINATION/FOLDER`

The script has the following options:

| param | lonf param | description
| :---: | :---: | :---: | 
| -d | --destination TEXT | The destination folder where the dataset is saved  |
| -f | --force-update | Forces the image list to be updated. |

Note that first use the image list is automatically updated and it takes about an hour.
