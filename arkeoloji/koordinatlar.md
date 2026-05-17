# Arkeolojik Koordinatlar ve Lokasyon Sözlüğü

## Coğrafi Veri Entegrasyonu

Aşağıdaki tablo, depodaki makine-okunur veri katmanı olan [`data/lokasyonlar.json`](../data/lokasyonlar.json) dosyasıyla senkronize edilmiştir. Buradaki enlem ve boylam dereceleri doğrudan OpenStreetMap, Google Earth veya CBS (Coğrafi Bilgi Sistemleri) yazılımlarına aktarılarak saha analizleri yapılabilir.

---

## Genişletilmiş Koordinat Tablosu

| ID | Antik Adı | Modern Adı / Mevki | Enlem (N) | Boylam (E) | Egemen Dönemler | Ülke | Teolojik / İbrahimî Önem |
|----|-----------|────────────────────|───────────|────────────|─────────────────|──────|──────────────────────────|
| **ur** | Ur (Urim) | Tell el-Muqayyar | `30.9625` | `46.1031` | Erken Dinastik – Eski Babil | Irak | - İbrahim'in doğum/göç yeri (Tevrat *Ur Kasdim*).<br>- Nanna (Sin) Zigguratı ve Woolley kazısı "Tufan Silt Katmanı". |
| **harran** | Harran | Altınbaşak (Şanlıurfa) | `36.8670` | `39.0330` | Bronz Çağı – İslam Dönemi | Türkiye | - Sin (Ay) Tapınağı *E-hul-hul*.<br>- İbrahim göçünün büyük durağı (Terah'ın ölümü ve Kenan çağrısı).<br>- Ataerkil ailelerin (Rebeka, Lea, Rahel) anayurdu. |
| **uruk** | Uruk | Warka | `31.3242` | `45.6361` | Uruk Dönemi – Seleukid | Irak | - Kral Gılgamış'ın yurdu.<br>- Yazının ilk icat edildiği kent.<br>- Gökyüzü Tanrısı An ve İştar'ın (İnanna) anıtsal tapınakları. |
| **nippur** | Nippur | Nuffar | `32.1260` | `45.2300` | Sümer – Pers Dönemi | Irak | - Sümer panteonunun dini kalbi (Baş tanrı Enlil'in tapınağı Ekur).<br>- Tevrat'taki kanunların teolojik kökenlerini barındıran zengin tablet arşivi. |
| **babilon** | Babil (Babilon) | Tell Babil (Hillah) | `32.5430` | `44.4244` | Eski Babil – Yeni Babil | Irak | - Babil Kulesi motifinin fiziksel mekanı (*Etemenanki* Zigguratı).<br>- Babil Sürgünü (M.Ö. 586-539) ve Tevrat metinlerinin redaksiyon merkezi. |
| **suruppak** | Şuruppak | Fara | `31.7758` | `45.4389` | Erken Dinastik | Irak | - Sümer Tufan efsanesindeki "Nuh" figürü olan bilge kral **Ziusudra**'nın şehri.<br>- Arkeolojik kazılarda saptanan büyük sel tabakalarından biri. |
| **kutha** | Kutha | Tell Ibrahim | `32.7667` | `44.7500` | Eski Babil – Neo-Asur | Irak | - İslamî / halk anlatılarında İbrahim'i ateşe atan **Nemrut**'un kalesi olarak adı geçen bölge.<br>- Yeraltı Tanrısı Nergal'in kült merkezi. |
| **dilmun** | Dilmun (Öneri) | Bahreyn Adası | `26.0667` | `50.5577` | Bronz Çağı (Körfez) | Körfez | - Sümer yaratılış efsanelerinde hastalık ve ölümün olmadığı saf "Dilmun Cenneti".<br>- Tevrat'taki *Gan Eden* (Aden Bahçesi) tasvirinin coğrafi arketipi. |
| **eridu** | Eridu | Abu Shahrain | `30.8158` | `45.9958` | Ubeyd – Ur III | Irak | - Sümer inancında yeryüzünün en eski şehri.<br>- Bilgelik ve Su Tanrısı **Enki**'nin tapınağı *E-abzu*.<br>- **Adapa (Apkallu)** efsanesinin geçtiği yer (Adem anlatısı paraleli). |

---

## Harita Entegrasyonu ve CBS Analizi

Arkeolojik saha çalışmalarında ve karşılaştırmalı tarihsel coğrafya derslerinde bu koordinatlar koordinat dönüştürücüler vasıtasıyla CBS haritalarına katman olarak eklenebilir. Örneğin:

1. **Ur → Harran → Kenan Güzergahı:** Koordinatlar haritaya girildiğinde, kervan rotasının Mezopotamya'nın iki büyük su kaynağı (Fırat ve Dicle) boyunca kuzeye kıvrılıp, ardından güney Levant'a (Kenan) inen "Bereketli Hilal" kavisini mükemmel şekilde izlediği görülür. Bu durum, antik kervan yollarının lojistik gerçekliğiyle tamamen uyumludur.
2. **Dilmun’un Belirsizliği:** Dilmun için önerilen koordinat Bahreyn adasındaki Qal'at al-Bahrain arkeolojik sitine işaret etmektedir. Sümer metinlerinde Dilmun "doğuda, güneşin doğduğu yerde" olarak tanımlanırken, bazı akademisyenler Dilmun'un güney İran veya Körfez kıyılarının tamamını kapsayan daha geniş bir ticaret bölgesi olduğunu savunmaktadır.

## Kaynaklar

- Parpola, Simo. *Neo-Assyrian Toponyms*. Neukirchen-Vluyn, 1970.
- Stone, Elizabeth C. *Nippur Neighborhoods*. The Oriental Institute of the University of Chicago, 1987.
- CDLI - Cuneiform Digital Library Initiative Gazetteer: [https://cdli.ucla.edu/](https://cdli.ucla.edu/)
