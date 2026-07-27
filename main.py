__version__ = "2.5.7"  # Must match line 8 of your buildozer.spec precisely

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest  # <-- CRITICAL FOR SAFE ANDROID NETWORKING
from kivy.clock import Clock
import json

class AviatorDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        main_layout = self  
        
        # 1. Header Component Display Frame
        header = Label(
            text='[b]Aviator Betika Live Stream v2.5.7[/b]',
            size_hint_y=0.1,
            markup=True,
            font_size='22sp'
        )
        main_layout.add_widget(header)
        
        # 2. Live Network Engine Connection Status
        self.status_label = Label(
            text='Status: Disconnected (Local Simulation)',
            size_hint_y=0.08,
            color=(1, 0.3, 0.3, 1)
        )
        main_layout.add_widget(self.status_label)
        
        # 3. Main Data Analytics Grid Monitor
        self.metrics_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height='80dp')
        self.metrics_grid.add_widget(Label(text="Live Intercepted Odds:", font_size='14sp'))
        self.lbl_target = Label(text="1.00x", font_size='24sp', bold=True, color=(1, 1, 1, 1))
        self.metrics_grid.add_widget(self.lbl_target)
        main_layout.add_widget(self.metrics_grid)
        
        # 4. Scroll View Console Window Frame for Log Telemetry
        scroll = ScrollView(size_hint=(1, 0.6))
        self.content_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))
        
        self.log_label = Label(
            text='[System Initialized]\nWaiting to attach live betika_scraper_py client stream...',
            markup=True,
            font_size='14sp',
            halign='left',
            valign='top',
            size_hint_y=None
        )
        self.log_label.bind(size=self._update_text_bounds)
        self.content_layout.add_widget(self.log_label)
        scroll.add_widget(self.content_layout)
        main_layout.add_widget(scroll)
        
        # 5. Core Pipeline Operational Control Action Button
        self.btn_run = Button(
            text="CONNECT LIVE SCRAPER STREAM",
            size_hint_y=0.12,
            background_color=(0.1, 0.6, 0.3, 1),
            bold=True
        )
        self.btn_run.bind(on_press=self.toggle_scraper_connection)
        main_layout.add_widget(self.btn_run)
        
        # Internal configuration storage parameters
        self.scraper_loop = None
        self.api_target_endpoint = "https://httpbin.org" # Replace with your hosting server/local node URL

    def _update_text_bounds(self, instance, size):
        self.log_label.text_size = (size, None)
        self.log_label.height = max(self.log_label.texture_size, 300)

    def toggle_scraper_connection(self, instance):
        if not self.scraper_loop:
            # Safely query your betika_scraper_py pipeline node every 3.0 seconds
            self.scraper_loop = Clock.schedule_interval(self.fetch_live_scraper_telemetry, 3.0)
            self.status_label.text = "Status: STREAMING LIVE"
            self.status_label.color = (0.2, 0.8, 0.2, 1)
            self.btn_run.text = "DISCONNECT SCRAPER ENGINE"
            self.btn_run.background_color = (0.9, 0.2, 0.2, 1)
        else:
            Clock.unschedule(self.scraper_loop)
            self.scraper_loop = None
            self.status_label.text = "Status: Disconnected"
            self.status_label.color = (1, 0.3, 0.3, 1)
            self.btn_run.text = "CONNECT LIVE SCRAPER STREAM"
            self.btn_run.background_color = (0.1, 0.6, 0.3, 1)

    def fetch_live_scraper_telemetry(self, dt):
        # Asynchronously fetch real-time text arrays without causing mobile UI freeze loops
        UrlRequest(
            url=self.api_target_endpoint,
            on_success=self.on_scraper_data_received,
            on_failure=self.on_network_request_error,
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
