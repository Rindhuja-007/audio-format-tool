import os

newfolder = []
path = "R:\\song"
audio_extensions = ["3gp", "aa", "aac", "aax", "act", "aiff", "alac", "amr", "ape", "au", "awb", "dct", "dss", "dvf", "flac", "gsm", "iklax", "ivs", "m4a", "m4b", "m4p", "mmf", "mp3", "mpc", "msv", "nmf", "ogg", "oga", "mogg", "opus", "ra", "rm", "raw", "rf64", "sln", "tta", "voc", "vox", "wav", "wma", "wv", "webm", "8svx", "cda"]

for file in os.listdir(path):
    if file.endswith(tuple(audio_extensions)):
        newfolder = os.path.join(path, file)
        print(newfolder)
