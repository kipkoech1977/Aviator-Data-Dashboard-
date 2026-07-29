from kivy.app import App
from kivy.utils import platform

class AviatorPredictorApp(App):
    def on_start(self):
        # Fire up the background data bundle fetcher
        if platform == 'android':
            from android import mActivity
            context = mActivity.getApplicationContext()
            service = mActivity.getServiceName('MyWidgetService')
            mActivity.startService(mActivity, service)
