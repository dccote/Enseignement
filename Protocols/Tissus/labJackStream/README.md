*This code was written by Ludovick Bégin and Arnaud Mercier.  The code was then transferred to DCCote on November 6th 2018 as part of the https://github.com/dccote/Enseignement repository*.



# LabJackStream Readme

This is a program made to automate the measurement of RAT (réflexion, absorption et transmission) data to determine the diffusion coefficients of biological sample. The program, if used with the correct experimental setup, performs a correction of the laser source fluctuations.

## Getting Started

These instructions will get you a copy of the project on your local machine for usage and development purposes.

### Prerequisites

1. It is simpler to get the Anaconda distribution for python 2.x/3.x since it has most of the required modules. You can download it  [here](https://www.anaconda.com/download/)
2. Install the [LabJack Drivers](https://labjack.com/support/software/installers/ud)
3. You must activate Python2 because labjackPython is only compatible with Python2. 
   `$ conda install python=2.7.15`
4. 
5. To be able to use labJackStream, make sure to install the following packages through a command window: `$ pip install labjackpython`

If those modules are missing you wont be able to use the program properly.

### Installing

First of all, if it has not been done yet, get a copy of the repository (with clone, fork, or download - see GitHub's documentation for more information).

```powershell
$ git clone https://github.com/dccote/Enseignement
```

And make sure your IDE has a PATH to the folder containing this project. 

### Running main from IDE

To run the main app, open the labJackStream project in your IDE and run the *main.py* file.

You can now choose to start an acquisition and visualize the data live. Pressing on the 'STOP' button will save a .txt file inside `/data` with the following architecture:

| Time | Laser power | Transmission power | Reflexion Power |
| ---- | ----------- | ------------------ | --------------- |
| ...  | ...         | ...                | ...             |


It will also print a table (MarkDown format) in your *run* window with different statistics (Min, Max, AVG, STD) from the acquisition you just done. It is recommended to rename the .txt data file after each acquisition with a significant name. 


