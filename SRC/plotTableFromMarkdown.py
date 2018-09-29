import sys
import os
import re
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk


class Plotter:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        self.acceptedExtensions = [".md"]
        self.compatible = 0
        self.filePath = ""
        self.fileExtension = ""
        self.lines = ''

        self.askUserOpenFile()
        self.findFileExtension()
        self.printFileInfo()
        self.extensionVerify()
        self.extentionHandle()

        self.dataPlot()

    def reset(self):
        self.askUserOpenFile()
        self.findFileName()
        self.findFileExtension()
        self.printFileInfo()
        self.extensionVerify()
        self.extentionHandle()

    def openFile(self):
        with open(self.filePath) as file:
            self.lines = file.readlines()

    def askUserOpenFile(self):
        self.filePath = filedialog.askopenfilename()

    def findFileExtension(self):
        trash, self.fileExtension = os.path.splitext(self.filePath)
        return self.fileExtension

    def printFileInfo(self):
        print("File Path: %s\nFile Extension:%s" % (self.filePath, self.fileExtension))

    def extensionVerify(self):
        if self.fileExtension in self.acceptedExtensions:
            self.compatible = 1
            print("File Extension is compatile.")

        else:
            self.compatible = 0
            print("File Extension is Not Compatible.")
            self.reset()

    def extentionHandle(self):
        if self.compatible == 1:
            if self.fileExtension == ".md":
                print("Markdown Data Handler will find tables and store its data.")
                self.markdownDataHandle()

            elif self.fileExtension == ".txt":
                self.txtDataHadle()

            elif self.fileExtension == ".csv":
                pass

    def markdownDataHandle(self):
        self.openFile()
        self.x = []
        self.y = []
        self.xLabel = ""
        self.yLabel = ""
        for line in self.lines:
            if re.match("\\|\s*---+\s*\\|\s*---+\s*", line):
                continue

            matchObj = re.match("\\|\s*(\.?\d+\.?\d*)\s*\\|\s*(\.?\d+\.?\d*)\s*", line)
            if matchObj:
                value = float(matchObj.group(1))
                self.x.append(value)
                value = float(matchObj.group(2))
                self.y.append(value)
                continue

            matchObj = re.match("\\|\s(.+?)\s\\|\s(.+?)\s\\|", line)
            if matchObj and self.xLabel == "" and self.yLabel == "":
                self.xLabel = matchObj.group(1)
                self.yLabel = matchObj.group(2)
                continue

    def txtDataHandle(self):
        pass
    def csvDataHandle(self):
        pass
    def GUIPlot(self):
        pass

    def dataPlot(self):
        plt.plot(self.x, self.y, 'ko')
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.show()


LabnoteGraphs = Plotter()