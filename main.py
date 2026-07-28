import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class InstantCrashSimulator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 25

        # Set a clean, solid premium dark background color
        Window.clearcolor = (0.08, 0.08, 0.1, 1)

        # 1. Header Title Banner Area
        self.title_label = Label(
            text="UPCOMING TARGET GENERATOR", 
            font_size='22sp', 
            bold=True,
            size_hint_y=0.15,
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.title_label)

        # 2. Main Center Fixed Content Window (Displays your standalone outcome)
        self.display_box = BoxLayout(
            orientation='vertical',
            size_hint_y=0.55,
            padding=15
        )
        
        self.status_label = Label(
            text="PRE-CALCULATED END CRASH POINT", 
            font_size='13sp', 
            color=(0.55, 0.55, 0.6, 1), # Clean slate gray accent
            bold=True,
            size_hint_y=0.3
        )
        
        self.value_label = Label(
            text="READY", 
            font_size='68sp', # Massively scaled up for direct readability
            color=(0.22, 0.78, 0.22, 1), # Bright Emerald Green
            bold=True,
            size_hint_y=0.7
        )
        
        self.display_box.add_widget(self.status_label)
        self.display_box.add_widget(self.value_label)
        self.add_widget(self.display_box)

        # 3. Simple Instant Trigger Action Button Container
        self.generate_btn = Button(
            text="GENERATE NEXT TARGET", 
            background_color=(0.78, 0.12, 0.12, 1), # Solid bold crimson red
            font_size='18sp',
            bold=True,
            size_hint_y=0.3
        )
        self.generate_btn.bind(on_press=self.generate_single_crash_point)
        self.add_widget(self.generate_btn)

    def generate_single_crash_point(self, instance):
        """
        Instantly computes a single standalone upcoming crash value.
        Uses an inverse distribution so lower numbers appear frequently 
        and high numbers appear rarely.
        """
        # 3% chance the game instant-crashes at 1.00x (House Edge simulation)
        if random.random() < 0.03: 
            next_crash = 1.00
        else:
            scale_constant = 100
            raw_roll = random.randint(1, scale_constant)
            next_crash = round((scale_constant / raw_roll), 2)
            
        # Ensure it never rolls mathematically below base multiplier limits
        if next_crash < 1.00:
            next_crash = 1.00
            
        # Update the text layout instantly with no moving elements or delays
        self.value_label.text = f"{next_crash:.2f}x"

class PredictorApp(App):
    def build(self):
        return InstantCrashSimulator()

if __name__ == '__main__':
    PredictorApp().run()
