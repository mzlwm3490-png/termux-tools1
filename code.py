import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from threading import Thread
from kivy.clock import Clock
class Dd(BoxLayout):
    
    def show_popup(self, title, message):
        # صندوق ترتيب العناصر داخل النافذة عمودياً
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # أضفنا Label يحتوي على نص الرسالة بالإنجليزية
        popup_layout.add_widget(Label(text=message, font_size=30))
        
        # إنشاء الـ Popup
        popup = Popup(
            title=title,             # عنوان النافذة (مثل Success, Error)
            content=popup_layout,    # المحتوى الداخلي
            size_hint=(0.5, 0.17),   # حجم النافذة
            auto_dismiss=True        # تُغلق تلقائياً عند الضغط خارجها
        )
        
        # فتح النافذة على الشاشة
        popup.open()

    def send_msg(self):
        # إشعار البدء بالإرسال بالإنجليزية
        self.show_popup('Please Wait', 'Sending data...')
        
        token = self.ids.token_input.text.strip()
        CHATID = self.ids.chat_input.text.strip()
        
        # التحقق من أن الحقول ليست فارغة
        if not token or not CHATID:
            self.show_popup('Warning', 'Please enter Token and Chat ID!')
            return
        Thread(target=self.req,args=(token,CHATID)).start()

        
    def req(self , token, CHATID):    
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            response = requests.post(url, data={"chat_id": CHATID, 'text': 'Login successful via Kivy app!'})
            res_data = response.json()
            
            # التحقق من نجاح الإرسال من سيرفر تيليجرام
            if res_data.get("ok"):
                Clock.schedule_once(lambda dt:self.show_popup('Success', 'Message sent to Telegram successfully!'))
            else:
                Clock.schedule_once(lambda dt: self.show_popup('Error', 'Failed to send. Check Token or Chat ID.'))
                
        except Exception as e:
            self.show_popup('Connection Error', f'An error occurred: {e}')
