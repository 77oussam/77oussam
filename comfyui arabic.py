# pip install googletrans==3.1.0a0

from googletrans import Translator

class عقدة_الترجمة_اليابانية:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "نص_المدخل": ("STRING", {"default": "مرحباً بالعالم!"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "ترجمة_إلى_اليابانية"
    CATEGORY = "عقد مخصصة"

    def ترجمة_إلى_اليابانية(self, نص_المدخل):
        مترجم = Translator()
        ترجمة = مترجم.translate(نص_المدخل, dest='ja')
        return (ترجمة.text,)

# اختبار العقدة
def اختبار_العقدة():
    عقدة = عقدة_الترجمة_اليابانية()
    نصوص_الاختبار = [
        "مرحباً بالعالم!",
        "How are you?",
        "Bonjour le monde!",
        "こんにちは世界！"
    ]
    
    for نص in نصوص_الاختبار:
        نتيجة = عقدة.ترجمة_إلى_اليابانية(نص)
        print(f"النص الأصلي: {نص}")
        print(f"الترجمة اليابانية: {نتيجة[0]}")
        print("---")

if __name__ == "__main__":
    اختبار_العقدة()