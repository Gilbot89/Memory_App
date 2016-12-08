import random
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout





class MemoryApp(GridLayout):
    def __init__(self, **kwargs):
        super(MemoryApp, self).__init__(**kwargs)


        self.cols = 4

        # setting up variables for containing the name of a photo under a button
        self.click1 = ''
        self.click2 = ''

        # creating the buttons for the game
        btn11 = ToggleButton()
        btn12 = ToggleButton()
        btn13 = ToggleButton()
        btn14 = ToggleButton()
        btn21 = ToggleButton()
        btn22 = ToggleButton()
        btn23 = ToggleButton()
        btn24 = ToggleButton()
        btn31 = ToggleButton()
        btn32 = ToggleButton()
        btn33 = ToggleButton()
        btn34 = ToggleButton()
        btn41 = ToggleButton()
        btn42 = ToggleButton()
        btn43 = ToggleButton()
        btn44 = ToggleButton()

        # organizing the buttons in a list
        self.b = [btn11, btn12, btn13, btn14,
                  btn21, btn22, btn23, btn24,
                  btn31, btn32, btn33, btn34,
                  btn41, btn42, btn43, btn44]

        # loading the photos from the photos folder and storing each twice in a list
        photo_location = 'C:/Users/Gilbert/PycharmProjects/Memory_App/photos'
        self.photos = os.listdir(photo_location)
        self.photos += self.photos


        # adding on press function and photos for revealed and unrevealed status to the buttons
        for i in self.b:
            self.add_widget(i)
            i.bind(on_press=self.on_press)
            i.background_normal='photo.jpg'
            i.background_disabled_down = 'photos/' + self.photos.pop(random.randint(0,len(self.photos) - 1))


        # creating the popup for a won game
        popup_box = BoxLayout()
        popup_box.add_widget(Button(text='Neue Runde?',on_press=self.reset))
        popup_box.add_widget(Button(text='Spiel beenden?', on_press=self.quit))
        self.popup = Popup(content=popup_box, title='Gewonnen!!!')

    # function for resetting the game
    def reset(self, event):
        for y in self.b:
            y.disabled = False
            y.state = 'normal'
        random.shuffle(self.b)
        self.popup.dismiss()

    # function for quitting the game
    def quit(self, event):
        App.get_running_app().stop()

    # checks if game is won
    def won(self):
        return all(x.disabled == True for x in self.b)

    # button event when clicked
    def on_press(self, event):
        # button gets disabled and reveald its background_disabled_down photo
        event.disabled = True

        # click variables store those photos and compare them
        if self.click1 == '':
            self.click1 = event.background_disabled_down

        elif self.click2 == '':
            self.click2 = event.background_disabled_down

            if self.click1 == self.click2:
                self.click1 = ''
                self.click2 = ''

            #after the second click the button gets assigned a new function
            # this is for technical reasons
            else:
                for n in self.b:
                    n.unbind(on_press=self.on_press)
                    n.bind(on_press=self.on_press_two)

            if self.won():
                self.popup.open()


    # covers the buttons again if there is no match, does nothing if there is a match
    # resets click variables
    def on_press_two(self, event):
        event.state = 'normal'
        if self.click1 != self.click2:
            for x in self.b:
                if x.background_disabled_down == self.click1 or x.background_disabled_down == self.click2:
                    x.disabled = False
                    x.state = 'normal'




        self.click1 = ''
        self.click2 = ''
        for m in self.b:
            m.unbind(on_press=self.on_press_two)
            m.bind(on_press=self.on_press)


class MyImageApp(App):
    def build(self):
        return MemoryApp()

if __name__=='__main__':
    MyImageApp().run()