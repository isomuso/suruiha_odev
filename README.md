# Sürü İHA Ödev

Ödevleriniz bu repo üzerinden verilecektir.

terminalden workspaceinizin src dosyasının içine giriniz. Aşağıdaki komutu terminale giriniz.

git clone https://github.com/isomuso/suruiha_odev.git

indirme işlemi bittikten sonra workspace klasöründeyken kodunuzu catkin_make (veya catkin build) ile build edin.
Kodu build ettikten sonra source edin. (source devel/setup.bash)

roslaunch suruiha_odev iha.launch 

yukarıdaki komut ile cpp ve python dosyasını aynı anda çalıştırabilirsiniz. İlk başta terminale hiçbir şey basmayacak.
Sonuç almak için ödevi yapın.

launch dosyasının hata vermesi durumunda paketin içindeki src ve launch klasörünün içindeki dosyaları executable yapmanız gerekebilir.
python hatası alıyor iseniz python dosyasındaki ilk satırda bulunan #usr/bin/env python kodunu #usr/bin/env python3 yapmanız gerekebilir. 

