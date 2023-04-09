"""
Copyright (c) 2023, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from string import ascii_uppercase

import os

import EnigmComputAuto
import EnigmInputAuto
import EnigmFonctionAuto


# Creation of the necessary global variables
DCablage, LTRotor, LDecalageRotor, TReflecteur = {}, [], (0, 0, 0), ()
Cablage, Rotor, DecalageRotor, Reflecteur = "", "", "", ""


# Creating the screen class TK
class Screen:

    def __init__(self):
        # Create the main window
        self.window = Tk()
        self.window.title("Enigma project")
        self.window.geometry("1920x1080")
        self.window.config(background="#283747")
        self.window.minsize(1480, 720)
        self.window.iconbitmap("enigma.ico")

        # Create the main screen
        self.MainScreen = Frame(self.window, bg="#283747")
        self.creat_main_screen()
        self.MainScreen.pack()

        # Creates the options screen (parameter) but does not display it
        self.OptionScreen = Frame(self.window, bg="#283747")
        self.creat_option_screen()

        # Puts basic random parameters
        self.fRandomize()
        self.fApplyChoice()


    # Create the 2 parts of the main screen (Settings and Input/Output)
    def creat_main_screen(self):
        self.SettingFrame = Frame(self.window, bg="#283747", bd=5)
        self.creat_settings_widgets()
        self.SettingFrame.pack(side="left")

        self.InputFrame = Frame(self.window, bg="#283747", bd=5)
        self.creat_inputs_widgets()
        self.InputFrame.pack(side="right")

    # Create the 2 parts of the Settings part (main screen)
    def creat_settings_widgets(self):
        self.SettingFrameUp = Frame(self.SettingFrame, bg="#283747", bd=5)
        self.creat_settings_up_widgets()
        self.SettingFrameUp.pack(expand="YES", fill="both")

        self.SettingFrameDown = Frame(self.SettingFrame, bg="#283747", bd=5)
        self.creat_settings_down_widgets()
        self.SettingFrameDown.pack(expand="YES", fill="both")

    # Create the 4 parts of the upper part of the Settings part (1 reflector and 3 rotors)
    def creat_settings_up_widgets(self):
        self.Reflector1Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_reflector1_widgets()
        self.Reflector1Frame.grid(column=0, row=0)

        self.Rotor1Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_rotor1_widgets()
        self.Rotor1Frame.grid(column=2, row=0)

        self.Rotor2Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_rotor2_widgets()
        self.Rotor2Frame.grid(column=3, row=0)

        self.Rotor3Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_rotor3_widgets()
        self.Rotor3Frame.grid(column=4, row=0)

    # Create the elements of the reflector part of the Settings part
    def creat_reflector1_widgets(self):
        self.reflector1_label = StringVar()
        self.reflector1_title = Label(self.Reflector1Frame, textvariable=self.reflector1_label, fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.reflector1_title.grid(column=0, row=0)

        self.reflector11 = StringVar()
        self.reflector11_title = Label(self.Reflector1Frame, textvariable=self.reflector11, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.reflector11_title.grid(column=0, row=1)

        self.reflector12 = StringVar()
        self.reflector12_title = Label(self.Reflector1Frame, textvariable=self.reflector12, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.reflector12_title.grid(column=0, row=2)

        self.reflector13 = StringVar()
        self.reflector13_title = Label(self.Reflector1Frame, textvariable=self.reflector13, fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.reflector13_title.grid(column=0, row=3)

        self.reflector14 = StringVar()
        self.reflector14_title = Label(self.Reflector1Frame, textvariable=self.reflector14, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.reflector14_title.grid(column=0, row=4)

        self.reflector15 = StringVar()
        self.reflector15_title = Label(self.Reflector1Frame, textvariable=self.reflector15, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.reflector15_title.grid(column=0, row=5)

    # Create the elements of the first rotor of the Settings part
    def creat_rotor1_widgets(self):
        self.rotor1_label = StringVar()
        self.rotor1_title = Label(self.Rotor1Frame, textvariable=self.rotor1_label, fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.rotor1_title.grid(column=0, row=0)

        self.rotor11 = StringVar()
        self.rotor11_title = Label(self.Rotor1Frame, textvariable=self.rotor11, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor11_title.grid(column=0, row=1)

        self.rotor12 = StringVar()
        self.rotor12_title = Label(self.Rotor1Frame, textvariable=self.rotor12, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor12_title.grid(column=0, row=2)

        self.rotor13 = StringVar()
        self.rotor13_title = Label(self.Rotor1Frame, textvariable=self.rotor13, fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.rotor13_title.grid(column=0, row=3)

        self.rotor14 = StringVar()
        self.rotor14_title = Label(self.Rotor1Frame, textvariable=self.rotor14, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor14_title.grid(column=0, row=4)

        self.rotor15 = StringVar()
        self.rotor15_title = Label(self.Rotor1Frame, textvariable=self.rotor15, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor15_title.grid(column=0, row=5)

    # Create the elements of the second rotor from the Settings part
    def creat_rotor2_widgets(self):
        self.rotor2_label = StringVar()
        self.rotor2_title = Label(self.Rotor2Frame, textvariable=self.rotor2_label, fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.rotor2_title.grid(column=0, row=0)

        self.rotor21 = StringVar()
        self.rotor21_title = Label(self.Rotor2Frame, textvariable=self.rotor21, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor21_title.grid(column=0, row=1)

        self.rotor22 = StringVar()
        self.rotor22_title = Label(self.Rotor2Frame, textvariable=self.rotor22, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor22_title.grid(column=0, row=2)

        self.rotor23 = StringVar()
        self.rotor23_title = Label(self.Rotor2Frame, textvariable=self.rotor23, fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.rotor23_title.grid(column=0, row=3)

        self.rotor24 = StringVar()
        self.rotor24_title = Label(self.Rotor2Frame, textvariable=self.rotor24, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor24_title.grid(column=0, row=4)

        self.rotor25 = StringVar()
        self.rotor25_title = Label(self.Rotor2Frame, textvariable=self.rotor25, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor25_title.grid(column=0, row=5)

    # Create the elements of the third rotor from the Settings part
    def creat_rotor3_widgets(self):
        self.rotor3_label = StringVar()
        self.rotor3_title = Label(self.Rotor3Frame, textvariable=self.rotor3_label, fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.rotor3_title.grid(column=0, row=0)

        self.rotor31 = StringVar()
        self.rotor31_title = Label(self.Rotor3Frame, textvariable=self.rotor31, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor31_title.grid(column=0, row=1)

        self.rotor32 = StringVar()
        self.rotor32_title = Label(self.Rotor3Frame, textvariable=self.rotor32, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor32_title.grid(column=0, row=2)

        self.rotor33 = StringVar()
        self.rotor33_title = Label(self.Rotor3Frame, textvariable=self.rotor33, fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.rotor33_title.grid(column=0, row=3)

        self.rotor34 = StringVar()
        self.rotor34_title = Label(self.Rotor3Frame, textvariable=self.rotor34, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.rotor34_title.grid(column=0, row=4)

        self.rotor35 = StringVar()
        self.rotor35_title = Label(self.Rotor3Frame, textvariable=self.rotor35, fg="#FDFEFE", font=("Calibri", 13), bg="#283747")
        self.rotor35_title.grid(column=0, row=5)

    # Creates the 12 parts of the lower part of the Settings part (12 front connections possible)
    def creat_settings_down_widgets(self):
        self.Connect1Frame = Frame(self.SettingFrameUp, bg="#283747", padx=45, bd=5)
        self.creat_connect1_widgets()
        self.Connect1Frame.grid(column=0, row=6)

        self.Connect2Frame = Frame(self.SettingFrameUp, bg="#283747", padx=45, bd=5)
        self.creat_connect2_widgets()
        self.Connect2Frame.grid(column=1, row=6)

        self.Connect3Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect3_widgets()
        self.Connect3Frame.grid(column=2, row=6)

        self.Connect4Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect4_widgets()
        self.Connect4Frame.grid(column=3, row=6)

        self.Connect5Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect5_widgets()
        self.Connect5Frame.grid(column=4, row=6)

        self.Connect6Frame = Frame(self.SettingFrameUp, bg="#283747", padx=45, bd=5)
        self.creat_connect6_widgets()
        self.Connect6Frame.grid(column=5, row=6)

        self.Connect7Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect7_widgets()
        self.Connect7Frame.grid(column=0, row=7)

        self.Connect8Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect8_widgets()
        self.Connect8Frame.grid(column=1, row=7)

        self.Connect9Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect9_widgets()
        self.Connect9Frame.grid(column=2, row=7)

        self.Connect10Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect10_widgets()
        self.Connect10Frame.grid(column=3, row=7)

        self.Connect11Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect11_widgets()
        self.Connect11Frame.grid(column=4, row=7)

        self.Connect12Frame = Frame(self.SettingFrameUp, bg="#283747", bd=5)
        self.creat_connect12_widgets()
        self.Connect12Frame.grid(column=5, row=7)

    # Create the elements of the first connection of the Settings part
    def creat_connect1_widgets(self):
        self.connect1_title = Label(self.Connect1Frame, text="C1", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect1_title.grid(column=0, row=0)

        self.connect1_let1, self.connect1_let2 = StringVar(name="connect1_let1"), StringVar(name="connect1_let2")
        self.connect1_let1_title = Label(self.Connect1Frame, textvariable=self.connect1_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect1_let1_title.grid(column=0, row=1)

        self.connect1_let2_title = Label(self.Connect1Frame, textvariable=self.connect1_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect1_let2_title.grid(column=0, row=3)

    # Create the elements of the first connection of the Settings part
    def creat_connect2_widgets(self):
        self.connect2_title = Label(self.Connect2Frame, text="C2", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect2_title.grid(column=0, row=0)

        self.connect2_let1, self.connect2_let2 = StringVar(name="connect2_let1"), StringVar(name="connect2_let2")
        self.connect2_let1_title = Label(self.Connect2Frame, textvariable=self.connect2_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect2_let1_title.grid(column=0, row=1)

        self.connect2_let2_title = Label(self.Connect2Frame, textvariable=self.connect2_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect2_let2_title.grid(column=0, row=3)

    # Create the elements of the third connection of the Settings part
    def creat_connect3_widgets(self):
        self.connect3_title = Label(self.Connect3Frame, text="C3", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect3_title.grid(column=0, row=0)

        self.connect3_let1, self.connect3_let2 = StringVar(name="connect3_let1"), StringVar(name="connect3_let2")
        self.connect3_let1_title = Label(self.Connect3Frame, textvariable=self.connect3_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect3_let1_title.grid(column=0, row=1)

        self.connect3_let2_title = Label(self.Connect3Frame, textvariable=self.connect3_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect3_let2_title.grid(column=0, row=3)

    # Create the elements of the fourth connection of the Settings part
    def creat_connect4_widgets(self):
        self.connect4_title = Label(self.Connect4Frame, text="C4", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect4_title.grid(column=0, row=0)

        self.connect4_let1, self.connect4_let2 = StringVar(name="connect4_let1"), StringVar(name="connect4_let2")
        self.connect4_let1_title = Label(self.Connect4Frame, textvariable=self.connect4_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect4_let1_title.grid(column=0, row=1)

        self.connect4_let2_title = Label(self.Connect4Frame, textvariable=self.connect4_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect4_let2_title.grid(column=0, row=3)

    # Create the elements of the fifth connection of the Settings part
    def creat_connect5_widgets(self):
        self.connect5_title = Label(self.Connect5Frame, text="C5", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect5_title.grid(column=0, row=0)

        self.connect5_let1, self.connect5_let2 = StringVar(name="connect5_let1"), StringVar(name="connect5_let2")
        self.connect5_let1_title = Label(self.Connect5Frame, textvariable=self.connect5_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect5_let1_title.grid(column=0, row=1)

        self.connect5_let2_title = Label(self.Connect5Frame, textvariable=self.connect5_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect5_let2_title.grid(column=0, row=3)

    # Create the elements of the sixth connection of the Settings part
    def creat_connect6_widgets(self):
        self.connect6_title = Label(self.Connect6Frame, text="C6", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect6_title.grid(column=0, row=0)

        self.connect6_let1, self.connect6_let2 = StringVar(name="connect6_let1"), StringVar(name="connect6_let2")
        self.connect6_let1_title = Label(self.Connect6Frame, textvariable=self.connect6_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect6_let1_title.grid(column=0, row=1)

        self.connect6_let2_title = Label(self.Connect6Frame, textvariable=self.connect6_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect6_let2_title.grid(column=0, row=3)

    # Create the elements of the seventh connection of the Settings part
    def creat_connect7_widgets(self):
        self.connect7_title = Label(self.Connect7Frame, text="C7", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect7_title.grid(column=0, row=0)

        self.connect7_let1, self.connect7_let2 = StringVar(name="connect7_let1"), StringVar(name="connect7_let2")
        self.connect7_let1_title = Label(self.Connect7Frame, textvariable=self.connect7_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect7_let1_title.grid(column=0, row=1)

        self.connect7_let2_title = Label(self.Connect7Frame, textvariable=self.connect7_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect7_let2_title.grid(column=0, row=3)

    # Create the elements of the eighth connection of the Settings part
    def creat_connect8_widgets(self):
        self.connect8_title = Label(self.Connect8Frame, text="C8", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect8_title.grid(column=0, row=0)

        self.connect8_let1, self.connect8_let2 = StringVar(name="connect8_let1"), StringVar(name="connect8_let2")
        self.connect8_let1_title = Label(self.Connect8Frame, textvariable=self.connect8_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect8_let1_title.grid(column=0, row=1)

        self.connect8_let2_title = Label(self.Connect8Frame, textvariable=self.connect8_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect8_let2_title.grid(column=0, row=3)

    # Create the elements of the ninth connection of the Settings part
    def creat_connect9_widgets(self):
        self.connect9_title = Label(self.Connect9Frame, text="C9", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect9_title.grid(column=0, row=0)

        self.connect9_let1, self.connect9_let2 = StringVar(name="connect9_let1"), StringVar(name="connect9_let2")
        self.connect9_let1_title = Label(self.Connect9Frame, textvariable=self.connect9_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect9_let1_title.grid(column=0, row=1)

        self.connect9_let2_title = Label(self.Connect9Frame, textvariable=self.connect9_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect9_let2_title.grid(column=0, row=3)

    # Create the elements of the tenth connection of the Settings part
    def creat_connect10_widgets(self):
        self.connect10_title = Label(self.Connect10Frame, text="C10", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect10_title.grid(column=0, row=0)

        self.connect10_let1, self.connect10_let2 = StringVar(name="connect10_let1"), StringVar(name="connect10_let2")
        self.connect10_let1_title = Label(self.Connect10Frame, textvariable=self.connect10_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect10_let1_title.grid(column=0, row=1)

        self.connect10_let2_title = Label(self.Connect10Frame, textvariable=self.connect10_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect10_let2_title.grid(column=0, row=3)

    # Create the elements of the eleventh connection of the Settings part
    def creat_connect11_widgets(self):
        self.connect11_title = Label(self.Connect11Frame, text="C11", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect11_title.grid(column=0, row=0)

        self.connect11_let1, self.connect11_let2 = StringVar(name="connect11_let1"), StringVar(name="connect11_let2")
        self.connect11_let1_title = Label(self.Connect11Frame, textvariable=self.connect11_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect11_let1_title.grid(column=0, row=1)

        self.connect11_let2_title = Label(self.Connect11Frame, textvariable=self.connect11_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect11_let2_title.grid(column=0, row=3)

    # Create the elements of the twelfth connection of the Settings part
    def creat_connect12_widgets(self):
        self.connect12_title = Label(self.Connect12Frame, text="C12", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#2E4053")
        self.connect12_title.grid(column=0, row=0)

        self.connect12_let1, self.connect12_let2 = StringVar(name="connect12_let1"), StringVar(name="connect12_let2")
        self.connect12_let1_title = Label(self.Connect12Frame, textvariable=self.connect12_let1, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect12_let1_title.grid(column=0, row=1)

        self.connect12_let2_title = Label(self.Connect12Frame, textvariable=self.connect12_let2, fg="#FDFEFE", font=("Calibri", 17), bg="#283747")
        self.connect12_let2_title.grid(column=0, row=3)


    # Create the 2 parts + 2 elements of the Input/Output part (main screen)
    def creat_inputs_widgets(self):
        self.TextInputFrame = Frame(self.InputFrame, bg="#283747",  bd=5)
        self.creat_inputs_text_widgets()
        self.TextInputFrame.grid(pady=20, column=0, row=0)

        self.param_button = Button(self.InputFrame, text="Paramètres", fg="#FDFEFE", font=("Calibri", 20), bg="#0B5345", command=self.fGoToParametere)
        self.param_button.grid(pady=20, column=0, row=1)

        self.reinit_button = Button(self.InputFrame, text="Re-appliquer tout", fg="#FDFEFE", font=("Calibri", 20), bg="#78281F", command=self.fApplyChoice)
        self.reinit_button.grid(pady=20, column=0, row=2)

        self.TextOutputFrame = Frame(self.InputFrame, bg="#283747",  bd=5)
        self.creat_outputs_text_widgets()
        self.TextOutputFrame.grid(pady=20, column=0, row=3)

    # Creates the elements of the Input part of the Input/Output part
    def creat_inputs_text_widgets(self):
        self.inputbox_title = Label(self.TextInputFrame, text="Entrer le texte à encrypter ici: ",fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#283747")
        self.inputbox_title.pack()

        self.inputtext = StringVar()
        self.input_entry = Entry(self.TextInputFrame, width=50, bg="#FBFCFC", font=("Calibri", 20), textvariable=self.inputtext)
        self.input_entry.pack()

        self.input_button = Button(self.TextInputFrame, text="Encrypter", fg="#FDFEFE", font=("Calibri", 20), bg="#4A235A", command=self.fEncrypt)
        self.input_button.pack(pady=5)

    # Creates the elements of the Output part of the Input/Output part
    def creat_outputs_text_widgets(self):
        self.inputbox_title = Label(self.TextOutputFrame, text="Voici le texte en sortie: ", fg="#FDFEFE", font=("Calibri", 20, "bold"), bg="#283747")
        self.inputbox_title.pack()

        self.outputtext = StringVar()
        self.input_entry = Entry(self.TextOutputFrame, width=50, bg="#D0D3D4", fg="#5D6D7E", font=("Calibri", 20), state="disabled", textvariable=self.outputtext)
        self.input_entry.pack()


    # Create the 4 parts + 3 elements of the options screen
    def creat_option_screen(self):
        self.randomize_button = Button(self.OptionScreen, text="Randomizer", fg="#FDFEFE", font=("Calibri", 20, "italic"), bg="#4A235A", command=self.fRandomize)
        self.randomize_button.grid(column=0, row=0, sticky="w")

        self.import_button = Button(self.OptionScreen, text="Importer une configuration", fg="#FDFEFE", font=("Calibri", 20), bg="#21618C", command=self.fBrowseFiles)
        self.import_button.grid(column=0, row=0, sticky="e")

        self.ConnectionFrame = Frame(self.OptionScreen, bg="#283747")
        self.creat_connect_widgets()
        self.ConnectionFrame.grid(pady=20, column=0, row=1)

        self.NumRotorFrame = Frame(self.OptionScreen, bg="#283747")
        self.creat_num_rotor_widgets()
        self.NumRotorFrame.grid(pady=20, column=0, row=2)

        self.DecalageFrame = Frame(self.OptionScreen, bg="#283747")
        self.creat_decalage_widgets()
        self.DecalageFrame.grid(pady=20, column=0, row=3)

        self.ReflectorFrame = Frame(self.OptionScreen, bg="#283747")
        self.creat_reflector_widgets()
        self.ReflectorFrame.grid(pady=20, column=0, row=4)

        self.retour_button = Button(self.OptionScreen, text="Retour", fg="#FDFEFE", font=("Calibri", 20), bg="#0B5345", command=self.fGoToMain)
        self.retour_button.grid(column=0, row=5, sticky="w")

        self.export_button = Button(self.OptionScreen, text="Enregistrer la configuration", fg="#FDFEFE", font=("Calibri", 20), bg="#21618C", command=self.fEnregistrerFile)
        self.export_button.grid(column=0, row=5)

        self.aplly_button = Button(self.OptionScreen, text="Appliquer tout", fg="#FDFEFE", font=("Calibri", 20), bg="#78281F", command=self.fApplyChoice)
        self.aplly_button.grid(column=0, row=5, sticky="e")

    # Creates the elements of the front connections part of the options screen
    def creat_connect_widgets(self):
        self.connectbox_title = Label(self.ConnectionFrame, text="Connections frontales (dictionnaire des lettres liées)", fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.connectbox_title.grid(column=0, row=0)

        self.connecttext = StringVar()
        self.connect_entry = Entry(self.ConnectionFrame, width=50, bg="#FBFCFC", font=("Calibri", 20), textvariable=self.connecttext)
        self.connect_entry.grid(column=0, row=1)

        self.connect_button = Button(self.ConnectionFrame, text="Appliquer", fg="#FDFEFE", font=("Calibri", 20), bg="#212F3C", command=self.fApplyChangementConnect)
        self.connect_button.grid(column=1, row=1)

    # Creates the items for the rotor number part of the options screen
    def creat_num_rotor_widgets(self):
        self.numrotorbox_title = Label(self.NumRotorFrame, text="Numéros des rotors (entre 1 et 9)", fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.numrotorbox_title.grid(column=0, row=0)

        self.numrotortext = StringVar()
        self.numrotor_entry = Entry(self.NumRotorFrame, width=50, bg="#FBFCFC", font=("Calibri", 20), textvariable=self.numrotortext)
        self.numrotor_entry.grid(column=0, row=1)

        self.numrotor_button = Button(self.NumRotorFrame, text="Appliquer", fg="#FDFEFE", font=("Calibri", 20), bg="#212F3C", command=self.fApplyChangementRotors)
        self.numrotor_button.grid(column=1, row=1)

    # Creates the items for the rotor offset part of the options screen
    def creat_decalage_widgets(self):
        self.decalagebox_title = Label(self.DecalageFrame, text="Décalages des rotors (entre 0 et 25)", fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.decalagebox_title.grid(column=0, row=0)

        self.decalagetext = StringVar()
        self.decalage_entry = Entry(self.DecalageFrame, width=50, bg="#FBFCFC", font=("Calibri", 20), textvariable=self.decalagetext)
        self.decalage_entry.grid(column=0, row=1)

        self.decalage_button = Button(self.DecalageFrame, text="Appliquer", fg="#FDFEFE", font=("Calibri", 20), bg="#212F3C", command=self.fApllyChangementDecalage)
        self.decalage_button.grid(column=1, row=1)

    # Creates the elements of the reflector part of the options screen
    def creat_reflector_widgets(self):
        self.reflectorbox_title = Label(self.ReflectorFrame, text="Numéro du reflecteur (entre 1 et 3)", fg="#FDFEFE", font=("Calibri", 20), bg="#283747")
        self.reflectorbox_title.grid(column=0, row=0)

        self.reflectortext = StringVar()
        self.reflector_entry = Entry(self.ReflectorFrame, width=50, bg="#FBFCFC", font=("Calibri", 20), textvariable=self.reflectortext)
        self.reflector_entry.grid(column=0, row=1)

        self.reflector_button = Button(self.ReflectorFrame, text="Appliquer", fg="#FDFEFE", font=("Calibri", 20), bg="#212F3C", command=self.fApplyChangementReflecteur)
        self.reflector_button.grid(column=1, row=1)



    # Function that allows you to switch from the main screen to the options screen
    def fGoToParametere(self):
        # screens to stop displaying
        self.MainScreen.pack_forget()
        self.SettingFrame.pack_forget()
        self.SettingFrameUp.pack_forget()
        self.SettingFrameDown.pack_forget()
        self.InputFrame.pack_forget()
        self.TextInputFrame.pack_forget()
        self.TextOutputFrame.pack_forget()
        # screen to display
        self.OptionScreen.pack()

    # Function that allows you to switch from the options screen to the main screen
    def fGoToMain(self):
        # screen to stop displaying
        self.OptionScreen.pack_forget()
        # screens to display
        self.MainScreen.pack()
        self.SettingFrame.pack(side="left")
        self.SettingFrameUp.pack(expand="YES", fill="both")
        self.SettingFrameDown.pack(expand="YES", fill="both")
        self.InputFrame.pack(side="right")
        self.TextInputFrame.grid(pady=20, column=0, row=0)
        self.TextOutputFrame.grid(pady=20, column=0, row=3)


    # Function that manages the display of the main screen reflector
    def fAffichageReflecteur(self):
        global TReflecteur, Reflecteur
        # change the name (number) of the reflector
        self.reflector1_label.set(f'Réflé {Reflecteur}')
        # change the reflector for the display
        self.reflector11.set(TReflecteur[0])
        self.reflector12.set(TReflecteur[1])
        self.reflector13.set(TReflecteur[2])
        self.reflector14.set(TReflecteur[3])
        self.reflector15.set(TReflecteur[4])

    # Function that manages the display of the main screen rotors
    def fAffichageRotor(self):
        global LTRotor, LDecalageRotor, Rotor
        # change the names (numbers) of the rotors
        self.rotor1_label.set(f'Rotor {Rotor[2]}-{EnigmFonctionAuto.fEasyAffichNum(LDecalageRotor[2])}')
        self.rotor2_label.set(f'Rotor {Rotor[1]}-{EnigmFonctionAuto.fEasyAffichNum(LDecalageRotor[1])}')
        self.rotor3_label.set(f'Rotor {Rotor[0]}-{EnigmFonctionAuto.fEasyAffichNum(LDecalageRotor[0])}')
        # change the rotors for the display by rotating them if necessary
        let1, let2, let3, let4, let5 = EnigmFonctionAuto.fCalculPosRotor(LTRotor[2], LDecalageRotor[2])
        self.rotor11.set(let1)
        self.rotor12.set(let2)
        self.rotor13.set(let3)
        self.rotor14.set(let4)
        self.rotor15.set(let5)
        let1, let2, let3, let4, let5 = EnigmFonctionAuto.fCalculPosRotor(LTRotor[1], LDecalageRotor[1])
        self.rotor21.set(let1)
        self.rotor22.set(let2)
        self.rotor23.set(let3)
        self.rotor24.set(let4)
        self.rotor25.set(let5)
        let1, let2, let3, let4, let5 = EnigmFonctionAuto.fCalculPosRotor(LTRotor[0], LDecalageRotor[0])
        self.rotor31.set(let1)
        self.rotor32.set(let2)
        self.rotor33.set(let3)
        self.rotor34.set(let4)
        self.rotor35.set(let5)

    # Function that manages the display of connections on the front of the machine on the main screen
    def fAffichageConnect(self):
        global DCablage
        ind, Lfait = 1, []
        # shows the connections if there are any
        for key, value in DCablage.items():
            if (key not in Lfait) and (value not in Lfait):
                self.window.setvar(name=f'connect{ind}_let1', value=key)
                self.window.setvar(name=f'connect{ind}_let2', value=value)
                Lfait.append(key)
                Lfait.append(value)
                ind += 1
        # make the front connections disappear if there are none
        for i in range(ind, 13):
            self.window.setvar(name=f'connect{i}_let1', value="")
            self.window.setvar(name=f'connect{i}_let2', value="")


    # Function that applies changes for the reflector 
    # check input - show error if there is a problem - update display when done
    def fApplyChangementReflecteur(self):
        global TReflecteur, Reflecteur
        verif, retour, refl = EnigmInputAuto.InputReflecteur(self.reflectortext.get())
        if verif == True:
            TReflecteur, Reflecteur = retour, refl
        else:
            messagebox.showinfo("Action impossible (reflecteur)", retour)
        self.fAffichageReflecteur()

    # Function that applies changes for rotors
    # check input - show error if there is a problem - update display when done
    def fApplyChangementRotors(self):
        global LTRotor, Rotor
        verif, retour, rot = EnigmInputAuto.InputRotor(self.numrotortext.get())
        if verif == True:
            LTRotor, Rotor = retour, rot
        else:
            messagebox.showinfo("Action impossible (rotors)", retour)
        self.fAffichageRotor()

    # Function that applies the changes for the offset of the rotors
    # check input - show error if there is a problem - update display when done
    def fApllyChangementDecalage(self):
        global LDecalageRotor
        verif, retour = EnigmInputAuto.InputDecalageRotor(self.decalagetext.get())
        if verif == True:
            LDecalageRotor = retour
        else:
            messagebox.showinfo("Action impossible (décalage)", retour)
        self.fAffichageRotor()

    # Function that applies changes for wiring
    # check input - show error if there is a problem - update display when done
    def fApplyChangementConnect(self):
        global DCablage
        verif, retour = EnigmInputAuto.InputConnexAvant(self.connecttext.get())
        if verif == True:
            DCablage = retour
        else:
            messagebox.showinfo("Action impossible (connections frontales)", retour)
        self.fAffichageConnect()

    # Function that applies all changes at the same time
    def fApplyChoice(self):
        self.fApplyChangementReflecteur()
        self.fApplyChangementRotors()
        self.fApllyChangementDecalage()
        self.fApplyChangementConnect()


    # Function that allows you to create random parameters
    def fRandomize(self):
        global Cablage, Rotor, DecalageRotor, Reflecteur
        Cablage = EnigmInputAuto.subInputConnexAvant(ascii_uppercase)
        Rotor = EnigmInputAuto.subInputRotor()
        DecalageRotor = EnigmInputAuto.subInputDecalageRotor()
        Reflecteur = EnigmInputAuto.subInputReflecteur()
        #affecte les variables pour l'affichage
        self.connecttext.set(Cablage)
        self.numrotortext.set(Rotor)
        self.decalagetext.set(DecalageRotor)
        self.reflectortext.set(Reflecteur)

    # Function that allows the call to EnigmComputAuto.py for the encryption of the message
    def fEncrypt(self):
        global DCablage, LTRotor, LDecalageRotor, TReflecteur
        Lintext = []
        intext = EnigmComputAuto.fInputTexte(self.inputtext.get())
        # input text formatting
        self.inputtext.set(' '.join(EnigmFonctionAuto.fPuissanceTexte(intext)))
        # formatting variables in a format acceptable to the main function (dictionary)
        LDRotor, DReflecteur = EnigmComputAuto.fsubInputRealParametre(LTRotor, TReflecteur)
        outtext = EnigmComputAuto.main(DCablage, LDRotor, LDecalageRotor, DReflecteur, intext)
        # display of the result and the rotation of the rotors after encryption
        self.outputtext.set(outtext)
        self.fAffichageRotor()

    # Function that allows you to manage the recovery of a QRcode to enter it in the settings
    def fBrowseFiles(self):
        global Cablage, Rotor, DecalageRotor, Reflecteur
        # open file manager
        filename = filedialog.askopenfilename(initialdir = "/", title = "Choisi un fichier",
            filetypes = (("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")))
        rtn = EnigmInputAuto.QRcodeToData(filename)
        if rtn[1] == False:
            messagebox.showinfo("Erreur: ", rtn[0])
        else:
            try:
                # change of variables (for display) in the correct format from the data
                data = rtn[1].strip("()").split(", ")
                self.connecttext.set(data[0].strip('""').replace(":",": ").replace(",",", "))
                Cablage = data[0].strip('""').replace(":",": ").replace(",",", ")
                self.numrotortext.set(f'{data[1]} {data[2]} {data[3]}'.strip('[]'))
                Rotor = f'{data[1]} {data[2]} {data[3]}'.strip('[]')
                self.decalagetext.set(f'{data[4]} {data[5]} {data[6]}'.strip('[]'))
                DecalageRotor = f'{data[4]} {data[5]} {data[6]}'.strip('[]')
                self.reflectortext.set(f'{data[7]}')
                Reflecteur = f'{data[7]}'
            except:
                messagebox.showinfo("Erreur: ", "Erreur de format dans les données")

    # Function that allows you to manage the saving of parameters in QRcode (placed in the QRcode file)
    def fEnregistrerFile(self):
        global Cablage, Rotor, DecalageRotor, Reflecteur
        data = (str(Cablage).replace(" ",""), Rotor, DecalageRotor, Reflecteur)
        i = 1
        # choice of automatic and unique name so as not to replace a previous one
        name = "QRCparametre"
        while os.path.isfile(f'QRcode/{name}.png'):
            name = f'QRCparametre{i}'
            i+=1
        rtn = EnigmInputAuto.DataToQRcode(str(data), name)
        if rtn[1] != True:
            messagebox.showinfo("Erreur: ", rtn[0])



# Display main loop - main function
def main():
    app = Screen()
    app.window.mainloop()


# Used to launch the main() function
if __name__ == '__main__':
    main()
