__version__ = "1.0.0"  # Buildozer reads this line to generate the APK package name

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DashboardLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        # Add basic screen title
        self.title_label = Label(
            text="Aviator Data Dashboard", 
            font_size='24sp',
            bold=True
        )
        self.add_widget(self.title_label)
        
        # Interactive status button
        self.action_btn = Button(
            text="Initialize Data Engine", 
            size_hint=(1, 0.25),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.action_btn.bind(on_press=self.on_btn_click)
        self.add_widget(self.action_btn)

    def on_btn_click(self, instance):
        self.title_label.text = "Dashboard Connected & Live!"

class AviatorApp(App):
    def build(self):
        return DashboardLayout()

if __name__ == "__main__":
    AviatorApp().run()
        super().__init__(cols=2, spacing=10, size_hint_y=None, height='140dp', **kwargs)
        
        # Metric 1: Multiplier Target
        self.add_widget(Label(text="Avg. Multiplier Target:", halign='left'))
        self.avg_mult = Label(text="2.45x", bold=True, font_size='18sp', color=(0.2, 0.6, 1, 1))
        self.add_widget(self.avg_mult)
        
        # Metric 2: Success Rate
        self.add_widget(Label(text="Predictive Accuracy:", halign='left'))
        self.accuracy = Label(text="76.4%", bold=True, font_size='18sp', color=(0.1, 0.8, 0.1, 1))
        self.add_widget(self.accuracy)

class DataLogView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(size_hint=(1, 1), **kwargs)
        
        # Scrollable container for telemetry data
        self.layout = GridLayout(cols=3, spacing=5, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.add_widget(self.layout)
        
        # Generate table headers
        headers = ["Timestamp", "Crash Point", "Risk Vector"]
        for header in headers:
            self.layout.add_widget(Label(text=f"[b]{header}[/b]", markup=True, size_hint_y=None, height='40dp'))
            
        # Seed initial dummy rows
        for i in range(1, 11):
            self.add_log_entry(f"Round #{1000 + i}", f"{round(random.uniform(1.0, 5.0), 2)}x", "LOW" if i % 2 == 0 else "MEDIUM")

    def add_log_entry(self, round_id, crash, risk):
        self.layout.add_widget(Label(text=round_id, size_hint_y=None, height='35dp'))
        self.layout.add_widget(Label(text=crash, size_hint_y=None, height='35dp'))
        
        risk_color = (0.1, 0.8, 0.1, 1) if risk == "LOW" else (1, 0.6, 0, 1)
        self.layout.add_widget(Label(text=risk, color=risk_color, size_hint_y=None, height='35dp'))

class ControlPanel(BoxLayout):
    def __init__(self, log_view, metrics_panel, **kwargs):
        super().__init__(orientation='vertical', size_hint_y=None, height='150dp', spacing=10, **kwargs)
        self.log_view = log_view
        self.metrics_panel = metrics_panel
        
        # Input Field for data updates
        self.input_field = TextInput(
            text='', 
            hint_text='Enter manual crash point data (e.g. 1.85)', 
            multiline=False, 
            size_hint_y=None, 
            height='45dp'
        )
        self.add_widget(self.input_field)
        
        # Interaction Button
        self.btn = Button(
            text="PROCESS NEW DATA ENGINE ROUND", 
            size_hint_y=None, 
            height='50dp',
            background_color=(0.2, 0.6, 1, 1),
            font_size='16sp',
            bold=True
        )
        self.btn.bind(on_press=self.process_data)
        self.add_widget(self.btn)

    def process_data(self, instance):
        val = self.input_field.text.strip()
        if not val:
            val = f"{round(random.uniform(1.0, 10.0), 2)}x"
        else:
            val = f"{val}x"
            
        # Append interactive data point dynamically
        rand_round = f"Round #{random.randint(1012, 9999)}"
        risk_profile = random.choice(["LOW", "MEDIUM", "HIGH"])
        self.log_view.add_log_entry(rand_round, val, risk_profile)
        
        # Update random dashboard telemetry metrics on click
        self.metrics_panel.avg_mult.text = f"{round(random.uniform(1.5, 3.5), 2)}x"
        self.metrics_panel.accuracy.text = f"{random.randint(65, 95)}%"
        self.input_field.text = ''

class AviatorDashboardApp(App):
    def build(self):
        # Master Layout Base
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Component Pipeline Composition
        header = DashboardHeader()
        metrics = MetricsPanel()
        logs = DataLogView()
        controls = ControlPanel(log_view=logs, metrics_panel=metrics)
        
        root.add_widget(header)
        root.add_widget(metrics)
        root.add_widget(Label(text="[i]Live Historical Trends Analytics[/i]", markup=True, size_hint_y=None, height='30dp'))
        root.add_widget(logs)
        root.add_widget(controls)
        
        return root

if __name__ == "__main__":
    AviatorDashboardApp().run()
    except Exception as runtime_error:
        # Catches crashes that happen right after the app finishes loading
        crash_log = traceback.format_exc()
        
        from kivy.app import App
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.label import Label
        
        class MobileCrashViewer(App):
            def build(self):
                scroll = ScrollView(size_hint=(1, 1))
                text = Label(
                    text=f"🔴 APPLICATION CRASH LOG:\n\n{crash_log}",
                    size_hint_y=None, halign="left", valign="top", font_size="15sp", color=(1, 0.2, 0.2, 1)
                )
                text.bind(texture_size=text.setter('size'))
                scroll.add_widget(text)
                return scroll
        if __name__ == '__main__':
            MobileCrashViewer().run()
else:
    # Catches crashes that happen during the initial import phase
    from kivy.app import App
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.label import Label
    
    class MobileImportCrashViewer(App):
        def build(self):
            scroll = ScrollView(size_hint=(1, 1))
            text = Label(
                text=f"❌ CRITICAL INITIALIZATION ERROR:\n\n{initialization_error}",
                size_hint_y=None, halign="left", valign="top", font_size="15sp", color=(1, 0.3, 0.3, 1)
            )
            text.bind(texture_size=text.setter('size'))
            scroll.add_widget(text)
            return scroll
    if __name__ == '__main__':
        MobileImportCrashViewer().run()
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='[b]Aviator Predictor v2.5.7[/b]',
            size_hint_y=0.1,
            markup=True,
            font_size='24sp'
        )
        main_layout.add_widget(header)
        
        # Status Display
        self.status_label = Label(
            text='Status: Ready',
            size_hint_y=0.08,
            color=(0, 1, 0, 1)
        )
        main_layout.add_widget(self.status_label)
        
        # Scroll view for content
        scroll = ScrollView(size_hint=(1, 0.7))
        content_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # Prediction Display
        self.prediction_label = Label(
            text='[b]Current Prediction:[/b]\nWaiting for data...',
            markup=True,
            size_hint_y=None,
            height=120
        )
        content_layout.add_widget(self.prediction_label)
        
        # Odds Display
        self.odds_label = Label(
            text='[b]Current Odds:[/b]\nLoading...',
            markup=True,
            size_hint_y=None,
            height=100
        )
        content_layout.add_widget(self.odds_label)
        
        # Statistics Display
        self.stats_label = Label(
            text='[b]Statistics:[/b]\nLoading...',
            markup=True,
            size_hint_y=None,
            height=100
        )
        content_layout.add_widget(self.stats_label)
        
        # Progress Bar
        self.progress = ProgressBar(
            size_hint_y=None,
            height=30,
            max=100
        )
        content_layout.add_widget(self.progress)
        
        scroll.add_widget(content_layout)
        main_layout.add_widget(scroll)
        
        # Button Layout
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        
        # Start Prediction Button
        self.predict_btn = Button(
            text='Start\nPrediction',
            background_color=(0, 1, 0, 1)
        )
        self.predict_btn.bind(on_press=self.start_prediction)
        button_layout.add_widget(self.predict_btn)
        
        # Stop Button
        self.stop_btn = Button(
            text='Stop',
            background_color=(1, 0, 0, 1),
            disabled=True
        )
        self.stop_btn.bind(on_press=self.stop_prediction)
        button_layout.add_widget(self.stop_btn)
        
        # Analytics Button
        analytics_btn = Button(
            text='Analytics',
            background_color=(0, 0, 1, 1)
        )
        analytics_btn.bind(on_press=self.show_analytics)
        button_layout.add_widget(analytics_btn)
        
        # Refresh Button
        refresh_btn = Button(
            text='Refresh',
            background_color=(1, 1, 0, 1)
        )
        refresh_btn.bind(on_press=self.refresh_data)
        button_layout.add_widget(refresh_btn)
        
        main_layout.add_widget(button_layout)
        
        # Start auto-update
        Clock.schedule_interval(self.update_display, 1)
        
        return main_layout
    
    def start_prediction(self, instance):
        """Start prediction in a separate thread"""
        if not self.prediction_running:
            self.prediction_running = True
            self.predict_btn.disabled = True
            self.stop_btn.disabled = False
            self.status_label.text = 'Status: [color=00ff00]Running...[/color]'
            self.status_label.markup = True
            
            # Run prediction in background
            thread = threading.Thread(target=self._run_prediction)
            thread.daemon = True
            thread.start()
    
    def _run_prediction(self):
        """Background prediction task"""
        try:
            for i in range(100):
                if not self.prediction_running:
                    break
                
                # Update progress
                Clock.schedule_once(
                    lambda dt: setattr(self.progress, 'value', i),
                    0
                )
                
                # Get prediction
                prediction = self.predictor.predict()
                odds = self.predictor.get_current_odds()
                
                # Update UI
                Clock.schedule_once(
                    lambda dt, p=prediction, o=odds: 
                    self._update_prediction_ui(p, o),
                    0
                )
                
                # Sleep between predictions
                import time
                time.sleep(2)
                
        except Exception as e:
            Clock.schedule_once(
                lambda dt: self._handle_error(str(e)),
                0
            )
    
    def _update_prediction_ui(self, prediction, odds):
        """Update UI with new prediction"""
        pred_text = f"[b]Current Prediction:[/b]\n"
        pred_text += f"Direction: {prediction['direction']}\n"
        pred_text += f"Confidence: {prediction['confidence']:.2%}\n"
        pred_text += f"Timestamp: {prediction['timestamp']}"
        self.prediction_label.text = pred_text
        
        odds_text = f"[b]Current Odds:[/b]\n"
        odds_text += f"High: {odds['high']:.2f}x\n"
        odds_text += f"Low: {odds['low']:.2f}x\n"
        odds_text += f"Spread: {odds['spread']:.4f}"
        self.odds_label.text = odds_text
    
    def stop_prediction(self, instance):
        """Stop prediction"""
        self.prediction_running = False
        self.predict_btn.disabled = False
        self.stop_btn.disabled = True
        self.status_label.text = 'Status: [color=ffff00]Stopped[/color]'
        self.status_label.markup = True
        self.progress.value = 0
    
    def refresh_data(self, instance):
        """Refresh data from API"""
        self.status_label.text = 'Status: [color=00ffff]Refreshing...[/color]'
        self.status_label.markup = True
        
        thread = threading.Thread(target=self._refresh_thread)
        thread.daemon = True
        thread.start()
    
    def _refresh_thread(self):
        """Background refresh task"""
        try:
            self.predictor.fetch_data()
            stats = self.analyzer.get_statistics()
            
            Clock.schedule_once(
                lambda dt, s=stats: self._update_stats_ui(s),
                0
            )
            
            Clock.schedule_once(
                lambda dt: setattr(
                    self.status_label, 'text',
                    'Status: [color=00ff00]Ready[/color]'
                ),
                0
            )
            Clock.schedule_once(
                lambda dt: setattr(self.status_label, 'markup', True),
                0
            )
            
        except Exception as e:
            Clock.schedule_once(
                lambda dt: self._handle_error(str(e)),
                0
            )
    
    def _update_stats_ui(self, stats):
        """Update statistics display"""
        stats_text = f"[b]Statistics:[/b]\n"
        stats_text += f"Total Predictions: {stats['total']}\n"
        stats_text += f"Accuracy: {stats['accuracy']:.2%}\n"
        stats_text += f"Win Rate: {stats['win_rate']:.2%}"
        self.stats_label.text = stats_text
    
    def show_analytics(self, instance):
        """Show analytics popup"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create a simple chart
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
        
        # Prediction accuracy chart
        labels = ['Win', 'Loss']
        sizes = [65, 35]
        colors = ['green', 'red']
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        ax1.set_title('Accuracy')
        
        # Odds distribution chart
        odds_data = np.random.uniform(1.0, 2.0, 100)
        ax2.hist(odds_data, bins=20, color='blue', alpha=0.7)
        ax2.set_title('Odds Distribution')
        ax2.set_xlabel('Odds Value')
        ax2.set_ylabel('Frequency')
        
        canvas = FigureCanvasKivyAgg(fig)
        content.add_widget(canvas)
        
        close_btn = Button(text='Close', size_hint_y=0.1)
        content.add_widget(close_btn)
        
        popup = Popup(
            title='Analytics',
            content=content,
            size_hint=(0.9, 0.9)
        )
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def update_display(self, dt):
        """Update display periodically"""
        if self.prediction_running:
            self.progress.value = min(self.progress.value + 1, 100)
    
    def _handle_error(self, error_msg):
        """Handle errors"""
        self.status_label.text = f'Status: [color=ff0000]Error: {error_msg}[/color]'
        self.status_label.markup = True
        self.prediction_running = False
        self.predict_btn.disabled = False
        self.stop_btn.disabled = True


if __name__ == '__main__':
    app = AviatorDashboard()
    app.run()
