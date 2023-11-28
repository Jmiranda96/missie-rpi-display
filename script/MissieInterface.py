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

    def __init__(self, root, confusionIcon, confusionMedia, enojoIcon, enojoMedia, felicidadIcon, felicidadMedia, miedoIcon, miedoMedia, neutralIcon, neutralMedia, tristezaIcon, tristezaMedia, mainImage):

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

        self.mainImage = mainImage

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
        
        self.video_page = VideoPage(root, self)
        self.video_page.grid(row=0, column=0, sticky="nsew")

        self.main_page = MainPage(root, self)
        self.main_page.grid(row=0, column=0, sticky="nsew")

        self.vlc_media_player_instance.set_xwindow(self.get_handle())
        print("\n add event")
        events = self.vlc_media_player_instance.event_manager()
        events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.video_finished)
        
        self.main_page.tkraise()

    def videoPuase(self, event):
        self.pause()

    def videoPlay(self, event):
        self.play()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_confusion_video(self):
        print("\n show confusion video")
        self.video_page.tkraise()
        self.play_film(confusionMedia)

    def show_enojo_video(self):
        print("\n show enojo video")
        self.video_page.tkraise()
        self.play_film(enojoMedia)

    def show_felicidad_video(self):
        print("\n show felicidad video")
        self.video_page.tkraise()
        self.play_film(felicidadMedia)

    def show_miedo_video(self):
        print("\n show miedo video")
        self.video_page.tkraise()
        self.play_film(miedoMedia)

    def show_neutral_video(self):
        print("\n show neutral video")
        self.video_page.tkraise()
        self.play_film(neutralMedia)

    def show_tristeza_video(self):
        print("\n show tristeza video")
        self.video_page.tkraise()
        self.play_film(tristezaMedia)

    def show_main_page(self):
        self.main_page.tkraise()

    def video_finished(self, event):
        print("\n video finished")
        time.sleep(1)
        self.show_main_page()

    def create_vlc_instance(self):
        """Create a vlc instance; `https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.MediaPlayer-class.html`"""
        vlc_instance = vlc.Instance('--verbose=1','--no-xlib')
        vlc_media_player_instance = vlc_instance.media_player_new()
        root.update()

        return vlc_instance, vlc_media_player_instance

    def get_handle(self):
        return self.video_page.winfo_id()

    def play(self):
        """Play a file."""
        print("play video")
        self.vlc_media_player_instance.play()

    def close(self):
        """Close the window."""
        self.container.delete_window()

    def stop(self):
        """Stop the player."""
        print("stop video")
        self.vlc_media_player_instance.stop()

    def pause(self):
        """Pause the player."""
        print("pause video")
        self.vlc_media_player_instance.pause()

    def play_film(self, media):
        self.vlc_media_player_instance.set_media(media)
        self.play()
        self.pause()
        time.sleep(1)
        self.play()

class MainPage(ttk.Frame):

    def __init__(self, parent, controller):

        # Frame config
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        
        buttonsFrame = ttk.Frame(self)
        buttonsFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        buttonsFrame.columnconfigure(0, weight=1)
        buttonsFrame.columnconfigure(1, weight=1)
        buttonsFrame.columnconfigure(2, weight=1)
        buttonsFrame.rowconfigure(0, weight=1)
        buttonsFrame.rowconfigure(1, weight=1)
        buttonsFrame.rowconfigure(2, weight=1)
        buttonsFrame.rowconfigure(3, weight=1)
        buttonsFrame.rowconfigure(4, weight=1)
        buttonsFrame.rowconfigure(5, weight=1)

        # Button config
        print("icono")
        print(controller.confusionIcon)
        mainLabel = ttk.Label(buttonsFrame, image = controller.mainImage)
        mainLabel.place(x = 0, y = 0, anchor = NW)

        self.confusionButton = ttk.Button(buttonsFrame, text='1', image=controller.confusionIcon,
                                  command=lambda: controller.show_confusion_video()).grid(column=0, row=0, sticky=(N, S, W, E))

        self.enojoButton = ttk.Button(buttonsFrame, text='2', image=controller.enojoIcon,
                                  command=lambda: controller.show_enojo_video()).grid(column=1, row=0, sticky=(N, S, W, E))

        self.felicidadButton = ttk.Button(buttonsFrame, text='3', image=controller.felicidadIcon,
                                  command=lambda: controller.show_felicidad_video()).grid(column=2, row=0, sticky=(N, S, W, E))

        self.miedoButton = ttk.Button(buttonsFrame, text='4', image=controller.miedoIcon,
                                  command=lambda: controller.show_miedo_video()).grid(column=0, row=5, sticky=(N, S, W, E))

        self.neutralButton = ttk.Button(buttonsFrame, text='5', image=controller.neutralIcon,
                                 command=lambda: controller.show_neutral_video()).grid(column=1, row=5, sticky=(N, S, W, E))

        self.tristezaButton = ttk.Button(buttonsFrame, text='6', image=controller.tristezaIcon,
                                command=lambda: controller.show_tristeza_video()).grid(column=2, row=5, sticky=(N, S, W, E))
        

class VideoPage(ttk.Frame):

    def __init__(self, parent, controller):

        # Frame config
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

root = Tk()

confusionMedia = vlc.Media(r"Assets/video/Confusion.mp4")
confusionImage = Image.open(r"Assets/icons/Confusion.png")
confusionImage.thumbnail((70, 70))
confusionIcon = ImageTk.PhotoImage(confusionImage)

enojoMedia = vlc.Media(r"Assets/video/Enojo.mp4")
enojoImage = Image.open(r"Assets/icons/Enojo.png")
enojoImage.thumbnail((70, 70))
enojoIcon = ImageTk.PhotoImage(enojoImage)

felicidadMedia = vlc.Media(r"Assets/video/Felicidad.mp4")
felicidadImage = Image.open(r"Assets/icons/Felicidad.png")
felicidadImage.thumbnail((70, 70))
felicidadIcon = ImageTk.PhotoImage(felicidadImage)

miedoMedia = vlc.Media(r"Assets/video/Miedo.mp4")
miedoImage = Image.open(r"Assets/icons/Miedo.png")
miedoImage.thumbnail((70, 70))
miedoIcon = ImageTk.PhotoImage(miedoImage)

neutralMedia = vlc.Media(r"Assets/video/Neutral.mp4")
neutralImage = Image.open(r"Assets/icons/Neutral.png")
neutralImage.thumbnail((70, 70))
neutralIcon = ImageTk.PhotoImage(neutralImage)

tristezaMedia = vlc.Media(r"Assets/video/Tristeza.mp4")
tristezaImage = Image.open(r"Assets/icons/Tristeza.png")
tristezaImage.thumbnail((70, 70))
tristezaIcon = ImageTk.PhotoImage(tristezaImage)

mainImageFile = Image.open(r"Assets/icons/face.jpg")
mainImageFile.thumbnail((500, 650))
mainImage = ImageTk.PhotoImage(mainImageFile)


REMInterface(root, confusionIcon, confusionMedia, enojoIcon, enojoMedia, felicidadIcon, felicidadMedia, miedoIcon, miedoMedia, neutralIcon, neutralMedia, tristezaIcon, tristezaMedia, mainImage)
root.mainloop()
