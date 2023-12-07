import json
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor

def translate_conversation(conversation):
    source_text = conversation['value']
    try:
        target_text = translator.translate(source_text, dest='tr').text
        conversation['value'] = target_text
        return True
    except Exception as e:
        print("Ceviri hatası:", str(e))
        return False

# Veriyi yükleyin
with open('sharegpt_clean_en_part2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Çeviri için Translator sınıfını oluşturun
translator = Translator()

# Diyaloğu çevirin ve Türkçe çevirileri kaydedin
with ThreadPoolExecutor() as executor:
    for conversation_group in data: 
        for conversation in conversation_group['conversations']:
            if translate_conversation(conversation):
                pass

# Türkçe çeviri ile güncellenmiş JSON dosyasını kaydedin
with open('sharegpt_clean_tr_part2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Çeviri tamamlandı. Sonuçlar 'sharegpt_clean_en_part2.json' dosyasına kaydedildi.")
