from googletrans import Translator

trans = Translator()

phrase = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")
trans_en= trans.translate(phrase,"en")
trans_fr= trans.translate(phrase,"fr")

detected= trans.detect(phrase)

print("========================번역결과========================\n")
print("입력어 - ", detected.lang, ":", phrase)
print("번역어1 - en:", trans_en)
print("번역어2 - fr:", trans_fr)
print("\n========================================================")