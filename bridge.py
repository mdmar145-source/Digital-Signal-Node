from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class NeuralApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input = TextInput(hint_text="Ask your AI Beacon...")
        self.btn = Button(text="Send Pulse", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.send_query)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.btn)
        return self.layout

    def send_query(self, instance):
        url = "http://localhost:8080/v1/chat/completions"
        data = {"messages":}
        res = requests.post(url, json=data)
        print(res.json()['choices'][0]['message']['content'])

NeuralApp().run()
