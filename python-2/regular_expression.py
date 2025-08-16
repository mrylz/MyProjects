import re
text = "van gölünde +90 535 345 6234 numaral bir telefon bulundu.gerekenin 15-May-2025 tarhihne kadar sahibne erilesi gerekir."
pattern  =  r"\d{2}-[a-zA-Z]{3}-\d{4}"
matches =  re.finditer(pattern,text)
for match in matches:
    print(match)
    # verilen textteki tarihleri bulan bu kod parçası re kütüphanesinin dahil edilmesi ile verilen işlemleri yapıyor
    # daha farklı işlemlerde yaplabilir ve genişletilebilir.
    # 
    #  