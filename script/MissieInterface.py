import os
import time
from tkinter import *
from tkinter import ttk
from turtle import color, width
from PIL import ImageTk, Image
import pygame
import vlc

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0')
    os.environ.__setitem__('DISPLAY', ':0')

class REMInterface():

    def __init__(self, root, confusionIcon, confusionMedia, enojoIcon, enojoMedia, felicidadIcon, felicidadMedia, miedoIcon, miedoMedia, neutralIcon, neutralMedia, tristezaIcon, tristezaMedia):

        # configure style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=(
            'Helvetica', 20), background="#fef0e0")
        self.style.configure('TButton', font=(
            'Helvetica', 20), background="#fef0e0", focuscolor='none')
        self.style.map('TButton', background=[('active', '#fef0e0')])
        self.style.configure('TFrame', font=(
            'Helvetica', 20), background="#fef0e0")

        # Image instance

        self.confusionIcon = confusionIcon
        self.enojoIcon = enojoIcon
        self.felicidadIcon = felicidadIcon
        self.miedoIcon = miedoIcon
        self.neutralIcon = neutralIcon
        self.tristezaIcon = tristezaIcon

        self.confusionMedia = confusionMedia
        self.enojoMedia = enojoMedia
        self.felicidadMedia = felicidadMedia
        self.miedoMedia = miedoMedia
        self.neutralMedia = neutralMedia
        self.tristezaMedia = tristezaMedia

        

        # Root config
        root.attributes("-fullscreen", 1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Video instance
        self.vlc_instance, self.vlc_media_player_instance = self.create_vlc_instance()

        events = self.vlc_media_player_instance.event_manager()
        events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.video_finished)
        

        self.main_page = MainPage(root, self)
        self.main_page.grid(row=0, column=0, sticky="nsew")

        self.vlc_media_player_instance.set_xwindow(self.get_handle())
        print(self.get_handle())

        self.main_page.tkraise()
        self.show_confusion_video()

    def videoPuase(self, event):
        self.pause()

    def videoPlay(self, event):
        self.play()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_confusion_video(self):
        print("\n show confusion video")
        self.play_film(confusionMedia)

    def show_enojo_video(self):
        print("\n show enojo video")
        self.play_film(enojoMedia)

    def show_felicidad_video(self):
        print("\n show felicidad video")
        self.play_film(felicidadMedia)

    def show_miedo_video(self):
        print("\n show miedo video")
        self.play_film(miedoMedia)

    def show_neutral_video(self):
        print("\n show neutral video")
        self.play_film(neutralMedia)

    def show_tristeza_video(self):
        print("\n show tristeza video")
        self.play_film(tristezaMedia)

    def show_main_page(self):
        self.main_page.tkraise()

    def video_finished(self, event):
        print("\n video finished")
        self.pause()
        self.show_confusion_video()

    def create_vlc_instance(self):
        """Create a vlc instance; `https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.MediaPlayer-class.html`"""
        vlc_instance = vlc.Instance('--no-xlib', '--vout mmal_vout')
        vlc_media_player_instance = vlc_instance.media_player_new()
        root.update()

        return vlc_instance, vlc_media_player_instance

    def get_handle(self):
        return self.main_page.winfo_id()

    def play(self):
        """Play a file."""
        if not self.vlc_media_player_instance.get_media():
            self.open()
        else:
            if self.vlc_media_player_instance.play() == -1:
                pass

    def close(self):
        """Close the window."""
        self.container.delete_window()

    def stop(self):
        """Stop the player."""
        self.vlc_media_player_instance.stop()

    def pause(self):
        """Pause the player."""
        self.vlc_media_player_instance.pause()

    def play_film(self, media):
        print("Show video")
        print(media)
        self.vlc_media_player_instance.set_media(media)
        # printing value
        self.play()

class MainPage(ttk.Frame):

    def __init__(self, parent, controller):

        # Frame config
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)

        # Button config
        # confusionButton = ttk.Button(self, text='1', image=controller.confusionIcon,
        #                           command=lambda: controller.show_confusion_video()).grid(column=0, row=0, sticky=(N, S, W, E))

        # enojoButton = ttk.Button(self, text='2', image=controller.enojoIcon,
        #                           command=lambda: controller.show_enojo_video()).grid(column=1, row=0, sticky=(N, S, W, E))

        # felicidadButton = ttk.Button(self, text='3', image=controller.felicidadIcon,
        #                           command=lambda: controller.show_felicidad_video()).grid(column=2, row=0, sticky=(N, S, W, E))

        # miedoButton = ttk.Button(self, text='4', image=controller.miedoIcon,
        #                           command=lambda: controller.show_miedo_video()).grid(column=0, row=2, sticky=(N, S, W, E))

        # neutralButton = ttk.Button(self, text='5', image=controller.neutralIcon,
        #                          command=lambda: controller.show_neutral_video()).grid(column=1, row=2, sticky=(N, S, W, E))

        # tristezaButton = ttk.Button(self, text='6', image=controller.tristezaIcon,
        #                         command=lambda: controller.show_tristeza_video()).grid(column=2, row=2, sticky=(N, S, W, E))

root = Tk()

confusionMedia = vlc.Media(r"Assets/video/Confusion.mp4")
confusionImage = Image.open(r"Assets/icons/Confusion.png")
confusionIcon = ImageTk.PhotoImage(confusionImage)

enojoMedia = vlc.Media(r"Assets/video/Enojo.mp4")
enojoImage = Image.open(r"Assets/icons/Enojo.png")
enojoIcon = ImageTk.PhotoImage(enojoImage)

felicidadMedia = vlc.Media(r"Assets/video/Felicidad.mp4")
felicidadImage = Image.open(r"Assets/icons/Felicidad.png")
felicidadIcon = ImageTk.PhotoImage(felicidadImage)

miedoMedia = vlc.Media(r"Assets/video/Miedo.mp4")
miedoImage = Image.open(r"Assets/icons/Miedo.png")
miedoIcon = ImageTk.PhotoImage(miedoImage)

neutralMedia = vlc.Media(r"Assets/video/Neutral.mp4")
neutralImage = Image.open(r"Assets/icons/Neutral.png")
neutralIcon = ImageTk.PhotoImage(neutralImage)

tristezaMedia = vlc.Media(r"Assets/video/Tristeza.mp4")
tristezaImage = Image.open(r"Assets/icons/Tristeza.png")
tristezaIcon = ImageTk.PhotoImage(tristezaImage)


REMInterface(root, confusionIcon, confusionMedia, enojoIcon, enojoMedia, felicidadIcon, felicidadMedia, miedoIcon, miedoMedia, neutralIcon, neutralMedia, tristezaIcon, tristezaMedia)
root.mainloop()
