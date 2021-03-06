from django.urls import path
from. import views
from .sitemaps import product_sitemap , article_sitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import AdsView

sitemaps ={
    'article': article_sitemap,
    'product': product_sitemap
}

urlpatterns = [
    path('ads.txt', AdsView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("", views.home, name= 'home'),
    path("mobile", views.mob, name='mobile'),
    path("article", views.article, name='article'),
    path("about", views.about, name='about'),
    path("contact-us", views.contact_us, name='contactus'),
    path("privacy-&-policy", views.privacy_policy, name='privacypolicy'),
    path("search", views.search, name='search'),


    # blog mobile links
    path("mobile/Best-PUBG-mobile-between-under-10000-20000-INR", views.pubg, name='pubg'),
    path("mobile/Best-mobile-under-10000-INR", views.mobile_10k, name='mobile10k'),
    path("mobile/Best-camera-mobile-under-15000-INR", views.camera_15k, name='camera15k'),
    path("mobile/Best-top-10-mobile", views.top_ten_mob, name='toptenmob'),
    path("mobile/top-10-Best-battery-backup-mobile", views.battery, name='battery'),
    path("mobile/iphone-12-blog", views.iphone_12_blog, name='iphone12blog'),
    path("mobile/non-chinese-smartphone", views.non_chinese_mobile, name='NonChinese'),
    path("article/boult-audio-probass-curve", views.boult_curve, name='boultcurve'),

    # programing
    path("programing/top-10-Best-backend-framework", views.top_10_framework, name='toptenframework'),
    path("programing/How-to-create-python-virtual-Environment", views.python_venv, name='pythonVenv'),
    path("programing/search-bar-in-django", views.search_bar, name='searchbar'),

    # game
    path("game/how-to-get-free-uc", views.free_uc, name='freeuc'),
    path("game/faug-made-in-india", views.FAUG, name='faug'),
    path("game/csk-vs-rr", views.cskvsrr, name='cskvsrr'),
    path("game/kkr-vs-mi", views.kkrvsmi, name='kkrvsmi'),
    path("game/kxip-vs-rcb", views.kxipvsrcb, name='kxipvsrcb'),
    path("game/csk-vs-dc", views.cskvsdc, name='cskvsdc'),
    path("game/kkr-vs-srh", views.kkrvssrh, name='kkrvssrh'),
    path("game/rr-vs-kxip", views.rrvskxip, name='rrvskxip'),
    path("game/srh-vs-dc", views.srhvsdc, name='srhvsdc'),
    path("game/rr-vs-kkr", views.rrvskkr, name='rrvskkr'),
    path("game/kxip-vs-mi", views.kxipvsmi, name='kxipvsmi'),
    path("game/csk-vs-srh", views.cskvssrh, name='cskvssrh'),
    path("game/dc-vs-kkr", views.dcvskkr, name='dcvskkr'),
    path("game/mi-vs-srh", views.mivssrh, name='mivssrh'),
    path("game/rcb-vs-dc", views.rcbvsdc, name='rcbvsdc'),
    path("game/mi-vs-rr", views.mivsrr, name='mivsrr'),
    path("game/csk-vs-kkr", views.cskvskkr, name='cskvskkr'),
    # technology
    path("technology/upcoming-mobile-phone", views.upcoming_mobile, name='upcomingMobile'),
    path("technology/add-me-to-search", views.add_me_to_search, name='addmetosearch'),
    path("technology/best-smartwatches-for-men-in-2020", views.smartwatch, name='smartwatch'),
    # apps
    path("apps/filmorago-Best-video-editing-app-in-2020", views.filmorago, name='filmorago'),
    path("apps/best-android-game", views.android_game, name='androidgame'),
    path("apps/air-scanner", views.air_scanner, name='airscanner'),
    path("apps/hipein-app", views.hipein_app, name='hipeinapp'),



    # mi page links
    path("mobile/xiaomi", views.redmi, name='xiaomi'),
    path("mobile/Redmi-note-9-pro-max", views.note_9_pro_max, name='note9promax'),
    path("mobile/Redmi-mi-10", views.mi10, name='mi10'),
    path("mobile/Redmi-k-20", views.redmi_k20, name='k20'),
    path("mobile/Redmi-note-7-pro", views.note_7_pro, name='note7pro'),
    path("mobile/Redmi-note-7s", views.note_7s, name='note7s'),
    path("mobile/Redmi-note-8", views.note_8, name='note8'),
    path("mobile/Redmi-note-8-pro", views.note_8_pro, name='note8pro'),
    path("mobile/Redmi-note-9-pro", views.note_9_pro, name='note9pro'),
    path("mobile/Redmi-8", views.redmi_8, name='redmi8'),
    path("mobile/Redmi-8a", views.redmi_8a, name='redmi8A'),
    path("mobile/Xiaomi-poco-f2", views.poco_f2, name='pocof2'),
    path("mobile/Xiaomi-poco-c3", views.poco_c3, name='pococ3'),
    path("mobile/Xiaomi-Mi-Note-10", views.mi_note_10, name='minote10'),
    path("mobile/poco-m2-pro", views.poco_m2_pro, name='pocom2pro'),
    path("mobile/poco-x3", views.poco_x3, name='pocox3'),
    path("mobile/mi-10t-pro", views.mi_10t_pro, name='mi10tpro'),
    path("mobile/mi-10t", views.mi_10t, name='mi10t'),
    path("mobile/Redmi-note-9-pro-5g", views.note_9_pro_5g, name='note9pro5g'),


    # oneplus page links
    path("mobile/oneplus", views.oneplus, name='OnePlus'),
    path("mobile/oneplus-3T", views.oneplus_3T, name='OnePlus_3T'),
    path("mobile/oneplus-5", views.oneplus_5, name='OnePlus_5'),
    path("mobile/oneplus-6T", views.oneplus_6T, name='OnePlus_6T'),
    path("mobile/oneplus-7", views.oneplus_7, name='OnePlus_7'),
    path("mobile/oneplus-7T", views.oneplus_7T, name='OnePlus_7T'),
    path("mobile/oneplus-7T-pro", views.oneplus_7T_pro, name='OnePlus_7T_pro'),
    path("mobile/oneplus-8", views.oneplus_8, name='OnePlus_8'),
    path("mobile/oneplus-8-pro", views.oneplus_8_pro, name='OnePlus_8pro'),
    path("mobile/oneplus-nord", views.oneplus_nord, name='OnePlus_nord'),
    path("mobile/oneplus-8t", views.oneplus_8t, name='OnePlus_8t'),
    path("mobile/oneplus-9", views.oneplus_9, name='OnePlus_9'),


    # realme page link
    path("mobile/realme", views._realme_, name='realme'),
    path("mobile/realme-Narzo", views.narzo, name='narzo'),
    path("mobile/realme-X2", views.realme_x2, name='realmeX2'),
    path("mobile/realme-X2-pro", views.realme_X2_pro, name='realmeX2pro'),
    path("mobile/realme-X50-pro", views.X50_pro, name='realmeX50pro'),
    path("mobile/realme-XT", views.realme_XT, name='realmeXT'),
    path("mobile/realme-5pro", views.realme_5pro, name='realme5pro'),
    path("mobile/realme-5s", views.realme_5s, name='realme5s'),
    path("mobile/realme-6", views.realme_6, name='realme6'),
    path("mobile/realme-6-pro", views.realme_6pro, name='realme6pro'),
    path("mobile/realme-C3", views.realme_C3, name='realmeC3'),
    path("mobile/realme-C11", views.realme_C11, name='realmeC11'),
    path("mobile/realme-C15", views.realme_C15, name='realmeC15'),
    path("mobile/realme-7-pro", views.realme_7_pro, name='realme7pro'),
    path("mobile/realme-7", views.realme_7, name='realme7'),
    path("mobile/realme-7i", views.realme_7i, name='realme7i'),
    path("mobile/realme-c17", views.realme_c17, name='realmec17'),
    path("mobile/realme-narzo-20-pro", views.narzo_20_pro, name='narzo20pro'),
    path("mobile/realme-narzo-20a", views.narzo_20a, name='narzo20a'),
    path("mobile/realme-narzo-20", views.narzo_20, name='narzo20'),
    path("mobile/realme-x7-pro", views.realme_x7_pro, name='realmex7pro'),
    path("mobile/realme-q2", views.realme_q2, name='realmeq2'),
    path("mobile/realme-q2i", views.realme_q2i, name='realmeq2i'),


    #  samsung page
    path("mobile/samsung", views.samsung, name='samsung'),
    path("mobile/samsung-galaxy-note-10", views.note_10, name='note10'),
    path("mobile/samsung-galaxy-note-20", views.note_20, name='note20'),
    path("mobile/samsung-galaxy-note-20-ultra", views.note_20_ultra, name='note20ultra'),
    path("mobile/samsung-galaxy-note-10-plus", views.note_10plus, name='note10plus'),
    path("mobile/samsung-galaxy-s10", views.s10, name='s10'),
    path("mobile/samsung-galaxy-s10-plus", views.s10_plus, name='s10plus'),
    path("mobile/samsung-galaxy-s10e", views.s10e, name='s10e'),
    path("mobile/samsung-galaxy-s20", views.s20, name='s20'),
    path("mobile/samsung-galaxy-s20-ultra", views.s20_ultra, name='s20ultra'),
    path("mobile/samsung-galaxy-s20-plus", views.s20_plus, name='s20plus'),
    path("mobile/samsung-galaxy-z-flip", views.z_flip, name='zflip'),
    path("mobile/samsung-galaxy-s20-fe", views.s20_fe, name='s20fe'),
    path("mobile/samsung-galaxy-a52", views.a52, name='a52'),
    path("mobile/samsung-galaxy-a42", views.a42, name='a42'),
    path("mobile/samsung-galaxy-m62", views.m62, name='m62'),

    # apple page link
    path("mobile/apple", views.apple, name='apple'),
    path("mobile/11-Pro-Max", views._11_pro_max, name='11ProMax'),
    path("mobile/iphone-11", views.iphone11, name='iphone11'),
    path("mobile/iphone-X", views.iphone_x, name='iphoneX'),
    path("mobile/iphone-XR", views.iphone_xr, name='iphoneXR'),
    path("mobile/iphone-8", views.iphone_8, name='iphone8'),
    path("mobile/iphone-7-plus", views.iphone_7plus, name='iphone7Plus'),
    path("mobile/iphone-7", views.iphone_7, name='iphone7'),
    path('mobile/iphone-6s', views.iphone_6s, name='iphone6s'),
    path("mobile/iphone-SE", views.iphone_se, name='iphoneSE'),
    path("mobile/iphone-12", views.iphone_12, name='iphone12'),
    path("mobile/iphone-12-mini", views.iphone_12_mini, name='iphone12mini'),
    path("mobile/iphone-12-pro", views.iphone_12_pro, name='iphone12pro'),
    path("mobile/iphone-12-pro-max", views.iphone_12_pro_max, name='iphone12promax'),


    # vivo page links
    path("mobile/vivo", views.vivo, name='vivo'),
    path("mobile/vivo-S1-pro", views.vivo_s1pro, name='vivoS1pro'),
    path("mobile/vivo-U10", views.vivo_u10, name='vivoU10'),
    path("mobile/vivo-U20", views.vivo_u20, name='vivoU20'),
    path("mobile/vivo-V17", views.vivo_v17, name='vivoV17'),
    path("mobile/vivo-V19", views.vivo_v19, name='vivoV19'),
    path("mobile/vivo-Y15", views.vivo_y15, name='vivoY15'),
    path("mobile/vivo-Y50", views.vivo_y50, name='vivoY50'),
    path("mobile/vivo-Z1pro", views.vivo_z1pro, name='vivoZ1pro'),
    path("mobile/vivo-Z1x", views.vivo_z1x, name='vivoZ1X'),
    path("mobile/vivo-v20-se", views.vivo_v20_se, name='vivov20se'),
    path("mobile/vivo-v20-pro", views.vivo_v20_pro, name='vivov20pro'),
    path("mobile/vivo-x60-pro", views.vivo_x60_pro, name='vivox60pro'),

    #news
    path("news/realme-v15-news", views.realme_v15_news, name='realmev15news'),

    # other
    path("mobile/micromax-in-1b", views.micromax_in_1b, name='in1b'),
    path("mobile/moto-g-5g", views.moto_g_5g, name='motog5g'),
    path(
       "OneSignalSDKWorker.js",
       TemplateView.as_view(
           template_name="OneSignal/OneSignalSDKWorker.js",
           content_type="application/javascript"
       ),
       name="OneSignalSDKWorker.js",
    ),
    path(
       "OneSignalSDKupdaterWorker.js",
       TemplateView.as_view(
           template_name="OneSignal/OneSignalSDKupdaterWorker.js",
           content_type="application/javascript"
       ),
       name="OneSignalSDKupdaterWorker.js",
    )
]
