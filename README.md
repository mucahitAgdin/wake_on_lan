# Wake on LAN (WOL) Kullanım Kılavuzu

Bu kılavuz, Wake on LAN (WOL) kodunuzu çalıştırmak için adım adım talimatlar sunar. WOL, bir bilgisayarı uzaktan ağ üzerinden uyandırmak için kullanılan bir tekniktir.

## Gereksinimler

- İki bilgisayarın da aynı yerel ağ üzerinde olması gereklidir.
- Uyandırılacak bilgisayarın BIOS ayarlarında WOL özelliğinin etkinleştirilmiş olması gereklidir.
- Windows Defender veya diğer güvenlik yazılımlarının ayarları düzenlenmelidir, böylece ağ portlarından gelen erişime izin verilir.
- Uzaktan erişim için kullanılacak UDP portu belirlenmelidir. Genellikle 7 veya 9 numaralı portlar tercih edilir.

## Adım Adım Talimatlar

1. **Ağ Bağlantıları Kontrolü:**
   - Her iki bilgisayarın da aynı yerel ağa bağlı olduğundan emin olun. WOL komutu ağ üzerinden iletilir, bu yüzden bilgisayarların aynı ağ segmentinde olması gereklidir.

2. **Uyandırılacak Bilgisayarın BIOS Ayarları:**
   - Uyandırılacak bilgisayarın BIOS ayarlarına erişin.
   - Power veya Advanced sekmesinde Wake on LAN veya WOL gibi bir seçeneği etkinleştirin.
   - Ayarları kaydedin ve çıkın.

3. **Güvenlik Duvarı Ayarları:**
   - Windows Defender veya herhangi bir güvenlik duvarı kullanıyorsanız, ağ portlarına gelen erişime izin vermesi gerekmektedir.
   - Güvenlik duvarı ayarlarına girin.
   - Gelen bağlantılara izin vermek için gereken ayarları yapılandırın. Özellikle kullanacağınız UDP portuna izin verdiğinizden emin olun.

4. **UDP Portunu Belirleme:**
   - Uzaktan erişim için kullanacağınız UDP portunu belirleyin. Genellikle 7 veya 9 numaralı portlar WOL için kullanılır. Bu portun bilgisayarlar arasında iletişim kurmak için kullanılacağını unutmayın.

5. **Kodunuzu Çalıştırma:**
   - Kodunuzu çalıştırarak uyandırma komutunu gönderin. Bu komut, hedef bilgisayarı belirttiğiniz UDP portu üzerinden uyandıracaktır.




