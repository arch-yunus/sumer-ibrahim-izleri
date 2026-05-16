# Veri Katmanı

Makine okunur JSON dosyaları; harita, karşılaştırma ve sözlük uygulamaları için tasarlanmıştır.

| Dosya | İçerik |
|-------|--------|
| `lokasyonlar.json` | Arkeolojik siteler, koordinatlar |
| `metin-paralelleri.json` | Motif düzeyinde metin özetleri |
| `terimler.json` | Dilsel kavram zincirleri |

## Şema

Tüm dosyalarda `schema_version` alanı bulunur. Geriye dönük uyumsuz değişikliklerde sürüm artırılır.

## Arama Betiği

```bash
python scripts/ara.py tufan
python scripts/ara.py --json ur
```

## Katkı

Yeni kayıt eklerken mevcut alan adlarını koruyun; `kaynak` alanına kısa referans yazın.
