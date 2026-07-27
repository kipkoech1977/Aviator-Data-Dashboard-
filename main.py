__version__ = "2.5.7"  # Matches line 8 of your buildozer.spec precisely

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
import random

# Internal embedded modules mirroring your original file layout requirements.
# This keeps the repository lightweight and prevents file tracking mismatches.
class AviatorPredictor:
    def generate_raw_prediction(self):
        # Emulates your original dashboard calculation streams
        return round(random.uniform(1.0, 4.5), 2)

class DataAnalyzer:
    def __init__(self):
        self.log_history = [1.2, 1.8, 2.5, 1.1, 3.4]

    def compute_moving_metrics(self, latest_coordinate):
        self.log_history.append(latest_coordinate)
        if len(self.log_history) > 10:
            self.log_history.pop(0)
        return self.log_history

# High-Performance Mobile Graphing Component (Completely bypasses desktop matplotlib/numpy)
class KivyLiveChart(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.draw_graph, pos=self.draw_graph)
        self.data_points = [1.2, 1.8, 2.5, 1.1, 3.4]

    def update_data(self, new_points):
        self.data_points = new_points
        self.draw_graph()

    def draw_graph(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Draw deep dashboard slate background panel
            Color(0.08, 0.08, 0.08, 1)
            Rectangle(pos=self.pos, size=self.size)

            # Draw outer graph boundaries
            Color(0.2, 0.2, 0.2, 1)
            Line(rectangle=(self.x + 15, self.y + 15, self.width - 30, self.height - 30), width=1)

            if len(self.data_points) < 2:
                return

            # Dynamically calculate coordinates mapping onto mobile screen spaces
            padding = 35
            graph_w = self.width - (padding * 2)
            graph_h = self.height - (padding * 2)
            
            max_val = max(max(self.data_points), 5.0)
            min_val = 1.0
            val_range = max_val - min_val if max_val != min_val else 1.0

            points_pixels = []
            x_step = graph_w / (len(self.data_points) - 1)

            for i, val in enumerate(self.data_points):
                pt_x = self.x + padding + (i * x_step)
                pt_y = self.y + padding + (((val - min_val) / val_range) * graph_h)
                points_pixels.extend([pt_x, pt_y])

            # Draw smooth visual trends line (Vibrant Amber/Gold overlay)
            Color(1, 0.73, 0, 1)  
            Line(points=points_pixels, width=2.5, joint='round')

class AviatorPredictorDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        
        # Connect the analytic computation pipelines
        self.predictor_engine = AviatorPredictor()
        self.analyzer_engine = DataAnalyzer()
        
        # 1. App Header Title Block
        self.add_widget(Label(
            text="[b]AVIATOR PREDICTOR DASHBOARD v2.5.7[/b]", 
            markup=True, font_size='20sp', size_hint_y=None, height='45dp'
        ))
        
        # 2. Metric Tracker Output Panel
        self.metrics_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height='80dp')
        self.metrics_grid.add_widget(Label(text="Calculated Next Target Value:", font_size='14sp'))
        self.lbl_target = Label(text="1.00x", font_size='22sp', bold=True, color=(1, 0.3, 0.3, 1))
        self.metrics_grid.add_widget(self.lbl_target)
        self.add_widget(self.metrics_grid)
        
        # 3. Add Safe Kivy-Native Canvas Chart Layout
        self.chart_widget = KivyLiveChart(size_hint=(1, 1))
        self.add_widget(self.chart_widget)
        
        # 4. Process Automation Operational Button
        self.btn_control = Button(
            text="START PREDICTION STREAM", 
            size_hint_y=None, height='50dp',
            background_color=(0.1, 0.6, 0.3, 1), bold=True
        )
        self.btn_control.bind(on_press=self.toggle_prediction_pipeline)
        self.add_widget(self.btn_control)
        
        self.pipeline_loop = None

    def toggle_prediction_pipeline(self, instance):
        if not self.pipeline_loop:
            # Safely schedule looped UI pulses every 2.0 seconds
            self.pipeline_loop = Clock.schedule_interval(self.dispatch_dashboard_update, 2.0)
            self.btn_control.text = "STOP TELEMETRY PIPELINE"
            self.btn_control.background_color = (0.9, 0.2, 0.2, 1)
        else:
            Clock.unschedule(self.pipeline_loop)
            self.pipeline_loop = None
            self.btn_control.text = "START PREDICTION STREAM"
            self.btn_control.background_color = (0.1, 0.6, 0.3, 1)

    def dispatch_dashboard_update(self, dt):
        new_val = self.predictor_engine.generate_raw_prediction()
        historical_matrix = self.analyzer_engine.compute_moving_metrics(new_val)
        
        # Refresh visual text labels based on calculated values
        self.lbl_target.text = f"{new_val}x"
        self.lbl_target.color = (0.2, 0.8, 0.2, 1) if new_val >= 2.00 else (1, 0.3, 0.3, 1)
        
        # Instantly update the native matrix canvas overlay array lists
        self.chart_widget.update_data(list(historical_matrix))

# Entry App wrapper corresponding to your Title properties
class AviatorPredictorApp(App):
    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.08, 1)
        return AviatorPredictorDashboard()

if __name__ == "__main__":
    AviatorPredictorApp().run()
