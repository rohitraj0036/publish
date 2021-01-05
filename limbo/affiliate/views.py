from django.shortcuts import render
from .models import product
from django.views import View
from django.http import HttpResponse


# Create your views here.
class AdsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse( "google.com, pub-5452473448420018, DIRECT, f08c47fec0942fa0")

def home(request):
    return render(request, 'page/Home_page.html')

def mob(request):
    return render(request, 'page/mobile_page.html')

def contact_us(request):
    return render(request, 'page/contact us.html')

def privacy_policy(request):
    return render(request, 'page/privacy&policy.html')

def article(request):
    return render(request, 'page/article_page.html')

def search(request):
    srh = request.GET['search']
    if len(srh) > 30:
        products = []
    elif len(srh) < 4:
        products = []
    else:
        products = product.objects.filter(name__icontains=srh)

    params = {'products': products, 'search':srh}
    return render(request, "page/search.html",params)

def about(request):
    return render(request, 'page/about_page.html')

# mobile bolg
def pubg(request):
    return render(request, "blog/pubg_mobile/pubg.html")

def mobile_10k(request):
    return render(request, "blog/mobile_10k/mobile_10k.html")

def camera_15k(request):
    return render(request, "blog/camera_15k/camera-15k.html")

def top_ten_mob(request):
    return render(request, "blog/best-top-10/best-top-10.html")

def iphone_12_blog(request):
    return render(request, "mobile/apple/12/12.html")

def battery(request):
    return render(request, "blog/battery/battery.html")

def non_chinese_mobile(request):
    return render(request, "blog/mobile/non-chinese-mobile/non-chinese-mobile.html")

# programing
def top_10_framework(request):
    return render(request, "blog/programing/top-10-framework.html")

def python_venv(request):
    return render(request, "blog/programing/python_venv.html")

def search_bar(request):
    return render(request, "blog/programing/search bar.html")

# technology
def upcoming_mobile(request):
    return render(request, "blog/technology/upcoming-mobile.html")

def add_me_to_search(request):
    return render(request, "blog/technology/add-me-to-search.html")

def smartwatch(request):
    return render(request, "blog/technology/smartwatch/smartwatch.html")

# earphone
def boult_curve(request):
    return render(request, "blog/technology/earphone/boult-audio-probass-curve.html")

# game
def free_uc(request):
    return render(request, "blog/game/free uc/free uc.html")

def FAUG(request):
    return render(request, "blog/game/FAUG/FAUG.html")

# ipl
def cskvsrr(request):
    return render(request, "blog/game/IPL/cssvsrr.html")

def kkrvsmi(request):
    return render(request, "blog/game/IPL/kkrvsmi.html")

def kxipvsrcb(request):
    return render(request, "blog/game/IPL/kxipvsrcb.html")

def cskvsdc(request):
    return render(request, "blog/game/IPL/cskvsdc.html")

def rrvskxip(request):
    return render(request, "blog/game/IPL/rrvskxip.html")

def kkrvssrh(request):
    return render(request, "blog/game/IPL/kkrvssrh.html")

def srhvsdc(request):
    return render(request, "blog/game/IPL/srhvsdc.html")

def rrvskkr(request):
    return render(request, "blog/game/IPL/rrvskkr.html")

def kxipvsmi(request):
    return render(request, "blog/game/IPL/kxipvsmi.html")

def cskvssrh(request):
    return render(request, "blog/game/IPL/cskvssrh.html")

def dcvskkr(request):
    return render(request, "blog/game/IPL/dcvskkr.html")

def mivssrh(request):
    return render(request, "blog/game/IPL/mivssrh.html")

def rcbvsdc(request):
    return render(request, "blog/game/IPL/rcbvsdc.html")

def mivsrr(request):
    return render(request, "blog/game/IPL/mivsrr.html")

def cskvskkr(request):
    return render(request, "blog/game/IPL/cskvskkr.html")
# app
def filmorago(request):
    return render(request, "blog/apps/filmorago/filmorago.html")

def android_game(request):
    return render(request, "blog/apps/game/top-10-android-game.html")

def air_scanner(request):
    return render(request, "blog/apps/air scanner/air-scanner.html")

def hipein_app(request):
    return render(request, "blog/apps/hipein app/hipein-app.html")
# mi moblie page
def redmi(request):
    return render(request, "mobile/mi/mi_page/mi_page.html")

def note_9_pro_max(request):
    return  render(request, "mobile/mi/note 9pro max/note 9 pro max.html")

def redmi_k20(request):
    return  render(request, "mobile/mi/k20/k20.html")

def mi10(request):
    return  render(request, "mobile/mi/mi 10/mi 10.html")

def note_7_pro(request):
    return  render(request, "mobile/mi/Note 7pro/note 7 pro.html")

def note_7s(request):
    return  render(request, "mobile/mi/note 7s/note 7s.html")

def note_8(request):
    return  render(request, "mobile/mi/note 8/note 8.html")

def note_8_pro(request):
    return  render(request, "mobile/mi/note 8 pro/note 8 pro.html")

def note_9_pro(request):
    return  render(request, "mobile/mi/note 9pro/note 9 pro.html")

def redmi_8(request):
    return  render(request, "mobile/mi/redmi 8/redmi 8.html")

def redmi_8a(request):
    return  render(request, "mobile/mi/redmi 8A/redmi 8A.html")

def poco_f2(request):
    return  render(request, "mobile/mi/poco f2/poco-f2.html")

def poco_c3(request):
    return  render(request, "mobile/mi/poco c3/poco-c3.html")

def mi_note_10(request):
    return  render(request, "mobile/mi/redmi note 10/redmi-note-10.html")

def poco_m2_pro(request):
    return  render(request, "mobile/mi/poco m2 pro/poco m2 pro.html")

def poco_x3(request):
    return  render(request, "mobile/mi/poco x3/poco-x3.html")

def mi_10t_pro(request):
    return  render(request, "mobile/mi/mi 10t pro/mi-10t-pro.html")

def mi_10t(request):
    return  render(request, "mobile/mi/mi 10t/mi-10t.html")

def note_9_pro_5g(request):
    return  render(request, "mobile/mi/note 9 pro 5g/note-9-pro-5g.html")

# oneplus page
def oneplus(request):
    return render(request, "mobile/oneplus/oneplus_page/OnePlus .html")

def oneplus_3T(request):
    return render(request, "mobile/oneplus/oneplus 3T/OnePlus_3T.html")

def oneplus_5(request):
    return render(request, "mobile/oneplus/oneplus 5/OnePlus_5.html")

def oneplus_6T(request):
    return render(request, "mobile/oneplus/oneplus 6T/OnePlus_6T.html")

def oneplus_7(request):
    return render(request, "mobile/oneplus/oneplus 7/OnePlus_7.html")

def oneplus_7T(request):
    return render(request, "mobile/oneplus/oneplus 7T/OnePlus_7T.html")

def oneplus_7T_pro(request):
    return render(request, "mobile/oneplus/oneplus 7T pro/OnePlus_7T_Pro.html")

def oneplus_8(request):
    return render(request, "mobile/oneplus/oneplus 8/OnePlus_8.html")

def oneplus_8_pro(request):
    return render(request, "mobile/oneplus/oneplus 8pro/OnePlus_8_Pro.html")

def oneplus_nord(request):
    return render(request, "mobile/oneplus/oneplus_nord/oneplus nord.html")

def oneplus_8t(request):
    return render(request, "mobile/oneplus/oneplus 8t/oneplus-8t.html")

def oneplus_9(request):
    return render(request, "mobile/oneplus/oneplus 9/oneplus-9.html")


# realme page link
def _realme_(request):
    return  render(request, "mobile/realme/realme_page/realme_page.html")

def X50_pro(request):
    return render(request, "mobile/realme/realme X50 pro/realme X50 pro.html")

def narzo(request):
    return render(request, "mobile/realme/realme narzo/realme narzo.html")

def realme_x2(request):
    return render(request, "mobile/realme/realme X2/realme X2.html")

def realme_X2_pro(request):
    return render(request, "mobile/realme/realme X2 pro/realme X2pro.html")

def realme_XT(request):
    return render(request, "mobile/realme/realme XT/realme XT.html")

def realme_5pro(request):
    return render(request,"mobile/realme/realme 5pro/realme 5pro.html")

def realme_5s(request):
    return render(request,"mobile/realme/realme 5s/realme 5s.html")

def realme_6(request):
    return render(request,"mobile/realme/realme 6/realme 6.html")

def realme_6pro(request):
    return render(request,"mobile/realme/realme 6pro/realme 6pro.html")

def realme_C3(request):
    return render(request,"mobile/realme/realme C3/realme C3.html")

def realme_C11(request):
    return render(request,"mobile/realme/realme c11/realme c11.html")

def realme_C15(request):
    return render(request,"mobile/realme/realme c15/realme-c15.html")

def realme_7_pro(request):
    return render(request,"mobile/realme/realme 7 pro/realme-7-pro.html")

def realme_7(request):
    return render(request,"mobile/realme/realme 7/realme-7.html")

def realme_7i(request):
    return render(request,"mobile/realme/realme 7i/realme-7i.html")

def realme_c17(request):
    return render(request,"mobile/realme/realme c17/realme-c17.html")

def narzo_20_pro(request):
    return render(request,"mobile/realme/narzo 20 pro/narzo-20-pro.html")

def narzo_20a(request):
    return render(request,"mobile/realme/narzo 20a/narzo-20a.html")

def narzo_20(request):
    return render(request,"mobile/realme/narzo 20/narzo-20.html")

def realme_x7_pro(request):
    return render(request,"mobile/realme/realme x7 pro/realme-x7-pro.html")

def realme_q2(request):
    return render(request,"mobile/realme/realme q2/realme-q2.html")

def realme_q2i(request):
    return render(request,"mobile/realme/realme q2i/realme-q2i.html")

# samsung pages
def samsung(request):
    return render(request, "mobile/samsung/samsung_page/samsung.html")

def note_10(request):
    return render(request, "mobile/samsung/note 10/note 10.html")

def note_20(request):
    return render(request, "mobile/samsung/note 20/note 20.html")

def note_20_ultra(request):
    return render(request, "mobile/samsung/note 20 ultra/note 20 ultra.html")

def note_10plus(request):
    return render(request, "mobile/samsung/note 10plus/note 10plus.html")

def s10(request):
    return render(request, "mobile/samsung/s10/s10.html")

def s10_plus(request):
    return render(request, "mobile/samsung/s10plus/s10plus.html")

def s10e(request):
    return render(request, "mobile/samsung/s10e/s10e.html")

def s20(request):
    return render(request, "mobile/samsung/s20/s20.html")

def s20_ultra(request):
    return render(request, "mobile/samsung/s20 ultra/s20 ultra.html")

def s20_plus(request):
    return render(request, "mobile/samsung/s20plus/s20plus.html")

def z_flip(request):
    return render(request, "mobile/samsung/z flip/z flip.html")

def s20_fe(request):
    return render(request, "mobile/samsung/samsung s20 fe/samsung-s20-fe.html")

def a52(request):
    return render(request, "mobile/samsung/a52/a52.html")

def m62(request):
    return render(request, "mobile/samsung/m62/m62.html")

def a42(request):
    return render(request, "mobile/samsung/a42/a42.html")
# apple page link
def apple(request):
    return render(request, "mobile/apple/apple_page/apple_page.html")

def _11_pro_max(request):
    return render(request, "mobile/apple/11 pro max/11 pro max.html")

def iphone11(request):
    return render(request, "mobile/apple/11/11.html")

def iphone_x(request):
    return render(request, "mobile/apple/x/x.html")

def iphone_xr(request):
    return render(request, "mobile/apple/xr/xr.html")

def iphone_se(request):
    return render(request, "mobile/apple/se/SE.html")

def iphone_8(request):
    return render(request, "mobile/apple/8/8.html")

def iphone_7plus(request):
    return render(request, "mobile/apple/7 plus/7plus.html")

def iphone_7(request):
    return render(request, "mobile/apple/7/7.html")

def iphone_6s(request):
    return render(request, "mobile/apple/6s/6s.html")

def iphone_12(request):
    return render(request, "mobile/apple/iphone 12/iphone-12.html")

def iphone_12_mini(request):
    return render(request, "mobile/apple/12 mini/12-mini.html")

def iphone_12_pro(request):
    return render(request, "mobile/apple/12 pro/12-pro.html")

def iphone_12_pro_max(request):
    return render(request, "mobile/apple/12 pro max/12-pro-max.html")
# vivo page link
def vivo(request):
    return  render(request, "mobile/vivo/vivo_page/vivo.html")

def vivo_s1pro(request):
    return  render(request, "mobile/vivo/vivo s1 pro/vivo s1pro.html")

def vivo_u10(request):
    return  render(request, "mobile/vivo/vivo u10/vivo u10.html")

def vivo_u20(request):
    return  render(request, "mobile/vivo/vivo u20/vivo u20.html")

def vivo_v19(request):
    return  render(request, "mobile/vivo/vivo v19/vivo v19.html")

def vivo_v17(request):
    return  render(request, "mobile/vivo/vivo v17/vivo v17.html")

def vivo_y15(request):
    return  render(request, "mobile/vivo/vivo y15/vivo y15.html")

def vivo_y50(request):
    return  render(request, "mobile/vivo/vivo y50/vivo y50.html")

def vivo_z1pro(request):
    return  render(request, "mobile/vivo/vivo z1 pro/vivo z1 pro.html")

def vivo_z1x(request):
    return  render(request, "mobile/vivo/vivo Z1X/vivo Z1X.html")

def vivo_v20_se(request):
    return  render(request, "mobile/vivo/v20 se/v20-se.html")

def vivo_v20_pro(request):
    return  render(request, "mobile/vivo/vivo v20 pro/vivo-v20-pro.html")

def vivo_x60_pro(request):
    return  render(request, "mobile/vivo/vivo x60/vivo-x60-pro.html")

#news
def realme_v15_news(request):
    return  render(request, "mobile/realme/realme-v15/realme-v15-news.html")

# other
def micromax_in_1b(request):
    return  render(request, "mobile/other/micromax-in-1b.html")

def moto_g_5g(request):
    return  render(request, "mobile/other/moto-g-5g.html")
