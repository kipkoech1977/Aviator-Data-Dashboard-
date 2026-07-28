import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock

class TelemetryGraph(Widget):
    """
    A custom drawing widget that plots the climbing telemetry curve
    onto the screen frame-by-frame.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.points = []

    def add_point(self, current_multiplier):
        # Scale the data points cleanly to fit beautifully within the app window canvas
        max_points = 100
        self.points.append(current_multiplier)
        if len(self.points) > max_points:
            self.points.pop(0)
        self.redraw()

    def clear_graph(self):
        self.points = []
        self.canvas.clear()

    def redraw(self):
        self.canvas.clear()
        if len(self.points) < 2:
            return

        with self.canvas:
            # Draw the background border envelope bounding box
            Color(0.2, 0.2, 0.2, 1)
            Line(rectangle=(self.x, self.y, self.width, self.height), width=1.5)

            # Draw the orange telemetry trend graph curve lines
            Color(1, 0.65, 0, 1) # Hex Amber Gold
            scaled_points = []
            
            x_step = self.width / 100
            # Scale y based heavily on the highest current value drawn on the axis
            max_val = max(max(self.points), 3.0) 
            
            for i, val in enumerate(self.points):
                x_coord = self.x + (i * x_step)
                # Keep points strictly contained within the visual chart canvas y boundaries
                y_coord = self.y + ((val - 1.0) / (max_val - 1.0)) * (self.height * 0.8)
                scaled_points.extend([x_coord, y_coord])
                
            Line(points=scaled_points, width=2)

class AviatorSimulator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Initialize internal state telemetry variables
        self.next_prediction = 1.00
        self.current_live_value = 1.00
        self.game_running = False
        
        # Generate the first hidden target point right away
        self.generate_new_prediction()

        # 1. Dashboard Header UI Section
        self.header_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15)
        self.title_label = Label(
            text="AVIATOR SIMULATOR v2.5", 
            font_size='20sp', 
            bold=True,
            halign='left',
            size_hint_x=0.5
        )
        self.prediction_label = Label(
            text=f"Calculated Next Target: {self.next_prediction:.2f}x", 
            font_size='18sp', 
            color=(0.3, 1, 0.3, 1), # Green Text accent
            bold=True,
            halign='right',
            size_hint_x=0.5
        )
        self.header_layout.add_widget(self.title_label)
        self.header_layout.add_widget(self.prediction_label)
        self.add_widget(self.header_layout)

        # 2. Main Center Graph Viewport Canvas Section
        self.graph_view = TelemetryGraph(size_hint_y=0.7)
        self.add_widget(self.graph_view)

        # 3. Footer Control Pipeline Trigger Button Section
        self.control_btn = Button(
            text="START TELEMETRY PIPELINE", 
            background_color=(0.1, 0.6, 0.1, 1), # Smooth Emerald Green
            font_size='16sp',
            bold=True,
            size_hint_y=0.15
        )
        self.control_btn.bind(on_press=self.toggle_pipeline)
        self.add_widget(self.control_btn)

    def generate_new_prediction(self):
        """
        Uses mathematical inverse distribution to calculate true simulator crash 
        points (low values appear frequently, high values are rare).
        """
        if random.random() < 0.03:  # 3% House Edge Instant Crash
            self.next_prediction = 1.00
        else:
            scale_constant = 100
            raw_roll = random.randint(1, scale_constant)
            self.next_prediction = round((scale_constant / raw_roll), 2)
            
        # Enforce baseline limits
        if self.next_prediction < 1.00:
            self.next_prediction = 1.00

    def toggle_pipeline(self, instance):
        if not self.game_running:
            # Prepare fresh canvas for running a new prediction
            self.game_running = True
            self.current_live_value = 1.00
            self.graph_view.clear_graph()
            
            # Stylize the execution pipeline state
            self.control_btn.text = "RUNNING... (TAP TO EMERGENCY CRASH)"
            self.control_btn.background_color = (0.7, 0.1, 0.1, 1) # Ruby Crimson Red
            
            # Start looping the frame update function at 60 FPS
            Clock.schedule_interval(self.update_simulation, 1.0 / 60.0)
        else:
            # User manually stops or triggers early crash reset
            self.end_round(manual=True)

    def update_simulation(self, dt):
        if not self.game_running:
            return False

        # Make the curve climb faster over time to mirror real crash game scales
        climb_acceleration = 0.005 + (self.current_live_value * 0.003)
        self.current_live_value += climb_acceleration
        
        # Stream data coordinates into the graph canvas widget
        self.graph_view.add_point(self.current_live_value)

        # Update the live text feed showing the active multiplier run
        self.prediction_label.text = f"Live Run: {self.current_live_value:.2f}x"

        # Check if the climbing graph has met the locally generated target prediction
        if self.current_live_value >= self.next_prediction:
            self.end_round(manual=False)
            return False

    def end_round(self, manual=False):
        self.game_running = False
        Clock.unschedule(self.update_simulation)
        
        # Display outcome status text strings 
        if manual:
            self.prediction_label.text = f"Crashed Manually! Expected: {self.next_prediction:.2f}x"
        else:
            self.prediction_label.text = f"CRASHED at {self.next_prediction:.2f}x!"
        
        # Reset button status interface
        self.control_btn.text = "GENERATE NEXT ROUND"
        self.control_btn.background_color = (0.1, 0.4, 0.8, 1) # Cool Blue Accent
        
        # Immediately compute the next standalone target loop sequence ahead of time
        self.generate_new_prediction()
        
        # Schedule showing the new target text briefly after the crash event updates clear
        Clock.schedule_once(self.display_upcoming_target, 2.5)

    def display_upcoming_target(self, dt):
        if not self.game_running:
            self.prediction_label.text = f"Calculated Next Target: {self.next_prediction:.2f}x"
            self.control_btn.text = "START TELEMETRY PIPELINE"
            self.control_btn.background_color = (0.1, 0.6, 0.1, 1)

class PredictorApp(App):
    def build(self):
        return AviatorSimulator()

if __name__ == '__main__':
    PredictorApp().run()
            on_error=self.on_network_request_error,
            timeout=2.5
        )

    def on_scraper_data_received(self, req, result):
        # Maps raw server response dictionaries cleanly back to your layout items
        try:
            # Replace these mock parsing indexes with the specific JSON keys returned by your scraper server
            # Example: current_odds = float(result.get('latest_multiplier', 1.00))
            import random
            current_odds = round(random.uniform(1.00, 6.50), 2)
            
            # Refresh metric monitors layout elements
            self.lbl_target.text = f"{current_odds}x"
            self.lbl_target.color = (0.2, 0.8, 0.2, 1) if current_odds >= 2.00 else (1, 0.3, 0.3, 1)
            
            new_entry = f"\n[Live Fetch]: Intercepted active target round odds index -> [b]{current_odds}x[/b]"
            self.log_label.text += new_entry
        except Exception as e:
            self.log_label.text += f"\n[Parsing Exception]: {str(e)}"

    def on_network_request_error(self, req, error):
        self.log_label.text += "\n[Connection Timeout]: Awaiting connection validation from data node scraper server..."

class AviatorPredictorApp(App):
    def build(self):
        return AviatorDashboard()

if __name__ == "__main__":
    AviatorPredictorApp().run()
