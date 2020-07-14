from django import forms

class TextForm(forms.Form):
    InputText = forms.CharField(label='กรุณาใส่คำที่ต้องการตรวจสอบ (เช่น กรุงเทบ / สลม / อุด้งธานี) ', max_length=100)
