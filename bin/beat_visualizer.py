#!/usr/bin/env python
# encoding: utf-8

from time import time
import tkinter as tk
import argparse
import pyaudio
import wave


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("tkinter")
        self.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        self.downbeat_oval_id = self.canvas.create_oval(10, 10, 90, 90, fill='red')
        self.beat_oval_id = self.canvas.create_oval(110, 10, 190, 90, fill='black')

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def blink_downbeat(self):
        self.canvas.itemconfig(self.downbeat_oval_id, fill='white')
        self.update()

        def _revert():
            self.canvas.itemconfig(self.downbeat_oval_id, fill='red')

        self.after(200, _revert)

    def blink_beat(self):
        self.canvas.itemconfig(self.beat_oval_id, fill='white')
        self.update()

        def _revert():
            self.canvas.itemconfig(self.beat_oval_id, fill='black')

        self.after(200, _revert)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wav', help='input *.wav file')
    parser.add_argument('beats', help='input *.beats.txt file. This should be the output of DBNDownBeatTracker')
    args = parser.parse_args()

    beats_file = open(args.beats, 'r')
    beats = []
    for line in beats_file.readlines():
        t, b = line.strip('\r\n').split('\t')
        beats.append((float(t), int(b)))

    wav_file = wave.open(args.wav, 'rb')

    # create an audio object
    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = p.open(format=
                    p.get_format_from_width(wav_file.getsampwidth()),
                    channels=wav_file.getnchannels(),
                    rate=wav_file.getframerate(),
                    output=True)

    root = tk.Tk()
    app = Application(master=root)
    t0 = time()

    def play_audio():
        # read data (based on the chunk size)
        chunk = 1024
        data = wav_file.readframes(chunk)

        # play stream (looping from beginning of file to the end)
        if data != '':
            # writing to the stream is what *actually* plays the sound.
            stream.write(data)
            dt = time() - t0
            if dt >= beats[0][0]:
                if beats[0][1] == 1:
                    app.blink_downbeat()
                else:
                    app.blink_beat()
                beats.pop(0)

            app.after(1, play_audio)

    app.after(1, play_audio)
    app.mainloop()

    # cleanup stuff.
    stream.close()
    p.terminate()

if __name__ == '__main__':
    main()
