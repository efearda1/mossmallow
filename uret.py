import os, html
MAIL="efearda.dev@gmail.com"; DATE_TR="8 Ekim 2026"; DATE_EN="October 8, 2026"
G=[
 ("puffy-oven","Puffy Oven","Kabarık Fırın",True,"Reklamları kaldır, 10 ipucu","Remove ads, 10 hints","açılan tarifler, yıldızlar, ses ayarı","unlocked recipes, stars, sound settings","ipucu","hints"),
 ("alchemist-tavern","Alchemist Tavern","Alchemist Tavern",True,"Reklamları kaldır, elmas paketleri","Remove ads, gem packs","hanın, altının, elmasların, ayarlar","your tavern, gold, gems, settings","çevrimdışı kazanç ve elmas","offline earnings and gems"),
 ("fjordlings","Fjordlings: Viking Defense","Fjordlings",True,"Reklamları kaldır, altın paketi","Remove ads, gold pack","köyün, baskın ilerlemen, ayarlar","your village, raid progress, settings","ganimet ve altın","loot and gold"),
 ("beacon-way","Beacon Way","Fener Yolu",True,"Reklamları kaldır","Remove ads","hikâye ilerlemen, topladıkların, ayarlar","story progress, collectibles, settings","ipucu ve deniz camı","hints and sea glass"),
 ("waffle-wonders","Waffle Wonders","Waffle Wonders",True,"Reklamları kaldır, jeton paketleri, şef paketi","Remove ads, coin packs, chef pack","dükkânın, günler, jetonlar, ayarlar","your shop, days, coins, settings","bahşiş ve jeton","tips and coins"),
]
CSS="body{font-family:-apple-system,Segoe UI,Roboto,sans-serif;max-width:760px;margin:0 auto;padding:24px 16px;line-height:1.6;color:#3a2a22;background:#fff8ec}h1{font-size:1.6em}h2{margin-top:1.6em;border-bottom:2px solid #e8a94b}a{color:#b5562f}.k{color:#7a6a60;font-size:.9em}"
def page(title,body): return f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{body}</body></html>'
def ads_tr(g):
    if not g[3]: return "<p>Bu oyunda reklam yoktur ve reklam kimliği kullanılmaz; izleme yapılmaz.</p>"
    return f"<h2>Reklamlar (Google AdMob)</h2><p>Oyun, Google AdMob ile isteğe bağlı ödüllü video ({g[8]} için) ve geçiş reklamları gösterir. Banner reklam yoktur.</p><p>AdMob reklam göstermek ve ölçmek için cihazının reklam kimliğini (IDFA / Android Advertising ID), IP adresini ve cihaz/kullanım bilgilerini işleyebilir. Bu veriyi biz görmeyiz; Google'ın gizlilik politikası geçerlidir: <a href='https://policies.google.com/privacy'>policies.google.com/privacy</a>.</p><p>AEA, Birleşik Krallık ve benzeri bölgelerde Google'ın onay formu ilk açılışta gösterilir; seçimini Ayarlar'daki \"Gizlilik seçenekleri\" ile değiştirebilirsin. iOS'ta izleme izni (ATT) istenebilir; reddedersen reklamlar kişiselleştirilmeden gösterilir. \"Reklamları kaldır\" satın alımı geçiş reklamlarını kapatır.</p>"
def ads_en(g):
    if not g[3]: return "<p>This game contains no ads, does not use the advertising identifier and does not track you.</p>"
    return f"<h2>Ads (Google AdMob)</h2><p>The game shows optional rewarded videos (for {g[9]}) and interstitial ads through Google AdMob. There are no banner ads.</p><p>AdMob may process your device's advertising ID (IDFA / Android Advertising ID), IP address and device/usage information to serve and measure ads. We do not see this data; Google's privacy policy applies: <a href='https://policies.google.com/privacy'>policies.google.com/privacy</a>.</p><p>In the EEA, the UK and similar regions Google's consent form is shown on first launch; you can change your choice with \"Privacy options\" in Settings. On iOS the tracking permission (ATT) may be requested; if you decline, ads are not personalized. The \"Remove ads\" purchase turns off interstitial ads.</p>"
links=[]
for g in G:
    slug,en,tr=g[0],g[1],g[2]
    os.makedirs(slug,exist_ok=True)
    body=(f"<h1>{html.escape(en)} — Privacy Policy / Gizlilik Politikası</h1><p class=k>Mossmallow Studio · Last updated {DATE_EN} / Son güncelleme {DATE_TR}</p>"
      f"<h2>English</h2><p>{html.escape(en)} asks for no account and does not collect personal data itself. There are no sign-ups or logins.</p><p>Your progress ({g[7]}) is stored only on your device; deleting the game deletes it.</p>{ads_en(g)}"
      f"<h2>Purchases</h2><p>In-app purchases ({g[5]}) are processed by the Apple App Store or Google Play. We never see or store your payment details. \"Restore purchases\" is in Settings.</p>"
      f"<h2>Children</h2><p>The game is not directed at children under 13 and we do not knowingly collect data from children.</p><h2>Contact</h2><p><a href='mailto:{MAIL}'>{MAIL}</a></p>"
      f"<h2>Türkçe</h2><p>{html.escape(tr)} hesap istemez ve kendisi kişisel veri toplamaz. Kayıt ya da giriş yoktur.</p><p>İlerlemen ({g[6]}) yalnızca cihazında saklanır; oyunu silince silinir.</p>{ads_tr(g)}"
      f"<h2>Satın alma</h2><p>Uygulama içi satın almalar ({g[4]}) Apple App Store ya da Google Play üzerinden yapılır. Ödeme bilgilerini görmeyiz, saklamayız. \"Satın alımları geri yükle\" Ayarlar'dadır.</p>"
      f"<h2>Çocuklar</h2><p>Oyun 13 yaş altı çocuklara yönelik değildir; bilerek çocuklardan veri toplamayız.</p><h2>İletişim</h2><p><a href='mailto:{MAIL}'>{MAIL}</a></p>")
    open(f"{slug}/privacy.html","w",encoding="utf-8").write(page(en+" Privacy",body))
    sup=(f"<h1>{html.escape(en)} — Support / Destek</h1><p>Need help, found a bug or have an idea? Write to us and we will answer as soon as we can.</p><p>Yardım mı lazım, bir hata mı buldun? Bize yaz, en kısa sürede dönelim.</p>"
         f"<p><b>E-mail:</b> <a href='mailto:{MAIL}?subject={html.escape(en)}'>{MAIL}</a></p><p>Purchases: use \"Restore purchases\" in Settings. / Satın almalar: Ayarlar'daki \"Satın alımları geri yükle\".</p><p><a href='privacy.html'>Privacy Policy / Gizlilik</a></p>")
    open(f"{slug}/support.html","w",encoding="utf-8").write(page(en+" Support",sup)); open(f"{slug}/index.html","w",encoding="utf-8").write(page(en+" Support",sup))
    links.append(f"<li><b>{html.escape(en)}</b> — <a href='{slug}/support.html'>Support</a> · <a href='{slug}/privacy.html'>Privacy</a></li>")
open("index.html","w",encoding="utf-8").write(page("Mossmallow Studio",f"<h1>Mossmallow Studio</h1><p>Cozy games made with love.</p><ul>{''.join(links)}</ul><p>Contact: <a href='mailto:{MAIL}'>{MAIL}</a></p>"))
print("ok")
