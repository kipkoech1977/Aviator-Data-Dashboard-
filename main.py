import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

class StationarySimulator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 30

        # Set a solid premium dark dashboard layout theme
        Window.clearcolor = (0.07, 0.07, 0.09, 1)

        # State Telemetry Parameters
        self.upcoming_target = 1.00
        self.is_running = False

        # Generate the very first stationary number instantly before anything starts
        self.generate_new_target()

        # 1. Dashboard Top Header Banner
        self.add_widget(Label(
            text="STATIONARY PRE-CALCULATOR PIPELINE", 
            font_size='20sp', 
            bold=True,
            size_hint_y=0.15,
            color=(1, 1, 1, 1)
        ))

        # 2. Main Fixed Central Content Window
        self.display_box = BoxLayout(orientation='vertical', size_hint_y=0.55, padding=10)
        
        self.status_label = Label(
            text="UPCOMING ROUND END TARGET", 
            font_size='13sp', 
            color=(0.55, 0.55, 0.6, 1), # Clean slate gray accent
            bold=True,
            size_hint_y=0.25
        )
        
        # Massive main text field displaying the exact standalone target number
        self.value_label = Label(
            text=f"{self.upcoming_target:.2f}x", 
            font_size='72sp', # Extra large format for high-contrast viewing
            color=(0.22, 0.82, 0.22, 1), # Bright Emerald Green
            bold=True,
            size_hint_y=0.5
        )
        
        self.info_feed = Label(
            text="System Status: Stationary. Target Locked.", 
            font_size='15sp', 
            color=(0.7, 0.7, 0.75, 1),
            size_hint_y=0.25
        )
        
        self.display_box.add_widget(self.status_label)
        self.display_box.add_widget(self.value_label)
        self.display_box.add_widget(self.info_feed)
        self.add_widget(self.display_box)

        # 3. Pipeline Simulation Trigger Button Control
        self.action_btn = Button(
            text="SIMULATE CURRENT ROUND", 
            background_color=(0.75, 0.12, 0.12, 1), # Solid bold crimson red
            font_size='18sp',
            bold=True,
            size_hint_y=0.3
        )
        self.action_btn.bind(on_press=self.execute_simulation_step)
        self.add_widget(self.action_btn)

    def generate_new_target(self):
        """
        Computes exactly one standalone multiplier using a standard crash algorithm distribution.
        This provides high odds for lower targets and low odds for large targets.
        """
        if random.random() < 0.03: # 3% House Edge Instant Crash
            self.upcoming_target = 1.00
        else:
            scale_constant = 100
            self.upcoming_target = round((scale_constant / random.randint(1, scale_constant)), 2)
            
        if self.upcoming_target < 1.00:
            self.upcoming_target = 1.00

    def execute_simulation_step(self, instance):
        if self.is_running:
            return

        self.is_running = True
        self.action_btn.disabled = True
        self.action_btn.text = "PROCESSING PIPELINE RUN..."
        
        # Flash a stationary notice showing that the current target is executing
        self.info_feed.text = f"Simulating loop... Crashing at exactly {self.upcoming_target:.2f}x"
        self.info_feed.color = (1, 0.4, 0.4, 1) # Alert Pink/Red
        
        # Schedule the round closure animation break (3 seconds freeze frame)
        Clock.schedule_once(self.finalize_round, 3.0)

    def finalize_round(self, dt):
        self.info_feed.text = f"CRASH EVENT: Round flew away at {self.upcoming_target:.2f}x!"
        self.info_feed.color = (0.6, 0.6, 0.6, 1)
        
        # Compute the brand new upcoming stationary target instantly
        self.generate_new_target()
        
        # Give the user a brief pause to look at the crash result before updating the text screen
        Clock.schedule_once(self.refresh_dashboard_view, 2.0)

    def refresh_dashboard_view(self, dt):
        # Update the giant main display with the fresh pre-calculated target number
        self.value_label.text = f"{self.upcoming_target:.2f}x"
        self.info_feed.text = "System Status: Stationary. Next Target Locked."
        self.info_feed.color = (0.7, 0.7, 0.75, 1)
        
        # Re-enable the interface controls for the next standalone turn
        self.action_btn.disabled = False
        self.action_btn.text = "SIMULATE CURRENT ROUND"
        self.is_running = False
