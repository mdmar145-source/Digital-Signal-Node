from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import requests

# إعدادات واجهة المهابيل (ألوان سوداء وخضراء)
Window.clearcolor = (0, 0, 0, 1)

class GhostShellApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان المنارة
        self.label = Label(text="[ AI GHOST SHELL ]", font_size='24sp', color=(0, 1, 0, 1), bold=True)
        self.layout.add_widget(self.label)
        
        # خانة إدخال الأوامر
        self.input = TextInput(
            hint_text="Enter Terminal Command...", 
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1),
            font_name="Roboto",
            cursor_color=(0, 1, 0, 1),
            multiline=False
        )
        self.layout.add_widget(self.input)
        
        # زر إرسال النبضة
        self.btn = Button(
            text="SEND NEURAL PULSE", 
            background_color=(0, 0.5, 0, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.btn.bind(on_press=self.send_to_beacon)
        self.layout.add_widget(self.btn)
        
        # منطقة عرض الرد الرقمي
        self.response_label = Label(text="Waiting for signal...", color=(0, 0.8, 0, 1), halign="center")
        self.layout.add_widget(self.response_label)
        
        return self.layout

    def send_to_beacon(self, instance):
        self.response_label.text = "STREEMING SIGNAL..."
        try:
            url = "http://localhost:8080/v1/chat/completions"
            payload = {
                "messages":,
                "temperature": 0.7
            }
            res = requests.post(url, json=payload, timeout=30)
            reply = res.json()['choices'][0]['message']['content']
            self.response_label.text = f"AI REPLY: {reply}"
        except Exception as e:
            self.response_label.text = "ERROR: BEACON OFFLINE!"

if __name__ == "__main__":
    GhostShellApp().run()
