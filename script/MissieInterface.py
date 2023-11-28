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
        
        self.video_page = VideoPage(root, self)
        self.video_page.grid(row=0, column=0, sticky="nsew")

        self.main_page = MainPage(root, self)
        self.main_page.grid(row=0, column=0, sticky="nsew")

        self.gifLable = ttk.Label(self.main_page, text='', anchor=CENTER).grid(
            column=0, row=0, sticky=(N, W, S, E))
        
        os.chdir(self.original_cwd + "/Assets/video")
        gif=gifplay(self.gifLable,r"Felicidad.gif",0.1)
        gif.infinite()

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
        time.sleep(4)
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

class VideoPage(ttk.Frame):

    def __init__(self, parent, controller):

        # Frame config
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        

class gifplay:
    """
    Usage: mygif=gifplay(<<tkinter.label Objec>>,<<GIF path>>,<<frame_rate(in ms)>>)
    example:
    gif=GIF.gifplay(self.model2,'./res/neural.gif',0.1)
    gif.play()
    This will play gif infinitely
    """
    def __init__(self,label,giffile,delay):
        self.frame=[]
        i=0
        while 1:
            try:
                image=PhotoImage(file = giffile, format="gif -index "+str(i))
                self.frame.append(image)
                i=i+1
            except:
                break
        print(i)
        self.totalFrames=i-1
        self.delay=delay
        self.labelspace=label
        self.labelspace.image=self.frame[0]

    def play(self):
        """
        plays the gif
        """
        _thread.start_new_thread(self.infinite,())

    def infinite(self):
        i=0
        while 1:
            self.labelspace.configure(image=self.frame[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)

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
