*This code was written by Ludovick Bégin and Arnaud Mercier*



# LabJackStream Readme

This is a program made to automate the measurement of RAT (réflexion, absorption et transmission) data to determine the diffusion coefficients of biological sample. The program, if used with the correct experimental setup, performs a correction of the laser source fluctuations.

## Getting Started

These instructions will get you a copy of the project on your local machine for usage and development purposes.

### Prerequisites

It is obligatory to get the Anaconda distribution for python 3.x since it has most of the required modules. You can download it  [here](https://www.anaconda.com/download/).
**To be able to use labJackStream, make sure to install the following packages through a command window: (power shell)**

```powershell
$ pip install labjackpython
```

**You will also need to install the [LabJack Drivers](https://labjack.com/support/software/installers/ud)**

If those modules are missing you wont be able to use the program properly.

### Installing

First of all, if it has not been done yet, get a copy of the repository (with clone, fork, or download - see GitHub's documentation for more information).

```powershell
$ git clone https://github.com/JLBegin/TPOBLabs.git
```

And make sure your IDE has a PATH to the folder containing this project. 

### Running main from IDE

To run the main app, open the labJackStream project in your IDE and run the *main.py* file.

You can now choose to start an acquisition and visualize the data live. Pressing on the 'STOP' button will save a .txt file inside `/data` with the following architecture:

| Time | Laser power | Transmission power | Reflexion Power |
| ---- | ----------- | ------------------ | --------------- |
| ...  | ...         | ...                | ...             |


It will also print a table (MarkDown format) in your *run* window with different statistics (Min, Max, AVG, STD) from the acquisition you just done. It is recommended to rename the .txt data file after each acquisition with a significant name. 


