# -*- coding: utf-8 -*-
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

_watermark_attached = False

def attach_watermark(*args):
    global _watermark_attached
    if _watermark_attached:
        return
    _watermark_attached = True
    try:
        layer = FloatLayout(size_hint=(1, 1))
        btn = Button(
            text="أبو مظلوم",
            size_hint=(None, None),
            size=(150, 38),
            pos_hint={"x": 0.02, "y": 0.015},
            font_size="12sp",
            background_color=(0.06, 0.09, 0.16, 0.85),
            color=(1, 1, 1, 1),
        )
        def _show_ad(_instance):
            content = Label(text="تم بناء هذا التطبيق عبر منصة مدير البناء - تطوير محمد جميل سالم علي مجمل اللقب أبو مظلوم.", halign="center", valign="middle")
            content.bind(size=lambda inst, val: setattr(inst, "text_size", (val[0] - 24, None)))
            Popup(
                title="إعلان المطور",
                content=content,
                size_hint=(0.82, 0.42),
            ).open()
        btn.bind(on_release=_show_ad)
        layer.add_widget(btn)
        Window.add_widget(layer)
    except Exception as exc:
        print("[WatermarkOverlay] attach failed:", exc)
