from django.shortcuts import render
from .models import product
from django.http import HttpResponse


# Create your views here.
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

# game
def free_uc(request):
    return render(request, "blog/game/free uc/free uc.html")

# app
def filmorago(request):
    return render(request, "blog/apps/filmorago/filmorago.html")

def android_game(request):
    return render(request, "blog/apps/game/top-10-android-game.html")

# mi moblie page
def redmi(request):
    return render(request, "mobile/mi/mi_page/mi_page.html")

def note_9_pro_max(request):
    product_price = '16,999'
    product_name = 'Redmi note 9 pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/note 9pro max/note 9 pro max.html", context=price)

def redmi_k20(request):
    product_price = '16,999'
    product_name = 'Redmi K20'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/k20/k20.html", context=price)

def mi10(request):
    product_price = '16,999'
    product_name = 'Redmi MI 10'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/mi 10/mi 10.html", context=price)

def note_7_pro(request):
    product_price = '16,999'
    product_name = 'Redmi note 97pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/Note 7pro/note 7 pro.html", context=price)

def note_7s(request):
    product_price = '16,999'
    product_name = 'Redmi note 7s'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/note 7s/note 7s.html", context=price)

def note_8(request):
    product_price = '16,999'
    product_name = 'Redmi note 8'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/note 8/note 8.html", context=price)

def note_8_pro(request):
    product_price = '16,999'
    product_name = 'Redmi note 8 pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/note 8 pro/note 8 pro.html", context=price)

def note_9_pro(request):
    product_price = '16,999'
    product_name = 'Redmi note 9 pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/note 9pro/note 9 pro.html", context=price)

def redmi_8(request):
    product_price = '16,999'
    product_name = 'Redmi 8'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/redmi 8/redmi 8.html", context=price)

def redmi_8a(request):
    product_price = '16,999'
    product_name = 'Redmi 8A'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/mi/redmi 8A/redmi 8A.html", context=price)

def poco_f2(request):
    return  render(request, "mobile/mi/poco f2/poco-f2.html")

def poco_c3(request):
    return  render(request, "mobile/mi/poco c3/poco-c3.html")

def mi_note_10(request):
    return  render(request, "mobile/mi/redmi note 10/redmi-note-10.html")

def poco_m2_pro(request):
    return  render(request, "mobile/mi/poco m2 pro/poco m2 pro.html")

# oneplus page
def oneplus(request):
    return render(request, "mobile/oneplus/oneplus_page/OnePlus .html")

def oneplus_3T(request):
    product_price = '16,999'
    product_name = 'OnePlus 3T'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 3T/OnePlus_3T.html", context=price)

def oneplus_5(request):
    product_price = '16,999'
    product_name = 'OnePlus 5'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 5/OnePlus_5.html", context=price)

def oneplus_6T(request):
    product_price = '16,999'
    product_name = 'OnePlus 6T'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 6T/OnePlus_6T.html", context=price)

def oneplus_7(request):
    product_price = '16,999'
    product_name = 'OnePlus 7'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 7/OnePlus_7.html", context=price)

def oneplus_7T(request):
    product_price = '16,999'
    product_name = 'OnePlus 7T'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 7T/OnePlus_7T.html", context=price)

def oneplus_7T_pro(request):
    product_price = '16,999'
    product_name = 'OnePlus 7T pro'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 7T pro/OnePlus_7T_Pro.html", context=price)

def oneplus_8(request):
    product_price = '16,999'
    product_name = 'OnePlus 8'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 8/OnePlus_8.html", context=price)

def oneplus_8_pro(request):
    product_price = '16,999'
    product_name = 'OnePlus 8 Pro'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus 8pro/OnePlus_8_Pro.html", context=price)

def oneplus_nord(request):
    product_price = '24,999'
    product_name = 'OnePlus nord'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/oneplus/oneplus_nord/oneplus nord.html", context=price)



# realme page link
def _realme_(request):
    return  render(request, "mobile/realme/realme_page/realme_page.html")

def X50_pro(request):
    product_price = '16,999'
    product_name = 'Realme X50'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/realme/realme X50 pro/realme X50 pro.html", context=price)

def narzo(request):
    product_price = '16,999'
    product_name = 'Realme Narzo'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/realme/realme narzo/realme narzo.html", context=price)

def realme_x2(request):
    product_price = '16,999'
    product_name = 'Realme X2'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/realme/realme X2/realme X2.html", context=price)

def realme_X2_pro(request):
    product_price = '16,999'
    product_name = 'Realme X2 pro'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/realme/realme X2 pro/realme X2pro.html", context=price)

def realme_XT(request):
    product_price = '16,999'
    product_name = 'Realme XT'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/realme/realme XT/realme XT.html", context=price)

def realme_5pro(request):
    product_price = '16,999'
    product_name = 'Realme 5 pro'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme 5pro/realme 5pro.html", context=price)

def realme_5s(request):
    product_price = '16,999'
    product_name = 'Realme 5s'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme 5s/realme 5s.html", context=price)

def realme_6(request):
    product_price = '16,999'
    product_name = 'Realme 6'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme 6/realme 6.html", context=price)

def realme_6pro(request):
    product_price = '16,999'
    product_name = 'Realme 6 pro'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme 6pro/realme 6pro.html", context=price)

def realme_C3(request):
    product_price = '16,999'
    product_name = 'Realme C3'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme C3/realme C3.html", context=price)

def realme_C11(request):
    product_price = '7,499'
    product_name = 'Realme C11'
    price = {'product':product_price, 'product_name':product_name}
    return render(request,"mobile/realme/realme c11/realme c11.html", context=price)

def realme_C15(request):
    return render(request,"mobile/realme/realme c15/realme-c15.html")

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


# apple page link
def apple(request):
    return render(request, "mobile/apple/apple_page/apple_page.html")

def _11_pro_max(request):
    product_price = '16,999'
    product_name = 'Apple iphone 11 pro max'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/11 pro max/11 pro max.html", context=price)

def iphone11(request):
    product_price = '16,999'
    product_name = 'Apple iphone 11'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/11/11.html", context=price)

def iphone_x(request):
    product_price = '16,999'
    product_name = 'Apple iphone X'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/x/x.html", context=price)

def iphone_xr(request):
    product_price = '16,999'
    product_name = 'Apple iphone XR'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/xr/xr.html", context=price)

def iphone_se(request):
    product_price = '16,999'
    product_name = 'Apple iphone SE'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/se/SE.html", context=price)

def iphone_8(request):
    product_price = '16,999'
    product_name = 'Apple iphone 8'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/8/8.html", context=price)

def iphone_7plus(request):
    product_price = '16,999'
    product_name = 'Apple iphone 7 plus'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/7 plus/7plus.html", context=price)

def iphone_7(request):
    product_price = '16,999'
    product_name = 'Apple iphone 7'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/7/7.html", context=price)

def iphone_6s(request):
    product_price = '16,999'
    product_name = 'Apple iphone 6s'
    price = {'product':product_price, 'product_name':product_name}
    return render(request, "mobile/apple/6s/6s.html", context=price)

# vivo page link
def vivo(request):
    return  render(request, "mobile/vivo/vivo_page/vivo.html")

def vivo_s1pro(request):
    product_price = '16,999'
    product_name = 'Vivo S1 pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo s1 pro/vivo s1pro.html", context=price)

def vivo_u10(request):
    product_price = '16,999'
    product_name = 'Vivo U10'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo u10/vivo u10.html", context=price)

def vivo_u20(request):
    product_price = '16,999'
    product_name = 'Vivo U20'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo u20/vivo u20.html", context=price)

def vivo_v19(request):
    product_price = '16,999'
    product_name = 'Vivo V19'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo v19/vivo v19.html", context=price)

def vivo_v17(request):
    product_price = '16,999'
    product_name = 'Vivo V17'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo v17/vivo v17.html", context=price)

def vivo_y15(request):
    product_price = '16,999'
    product_name = 'Vivo Y15'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo y15/vivo y15.html", context=price)

def vivo_y50(request):
    product_price = '16,999'
    product_name = 'Vivo Y50'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo y50/vivo y50.html", context=price)

def vivo_z1pro(request):
    product_price = '16,999'
    product_name = 'Vivo Z1 pro'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo z1 pro/vivo z1 pro.html", context=price)

def vivo_z1x(request):
    product_price = '16,999'
    product_name = 'Vivo Z1X'
    price = {'product':product_price, 'product_name':product_name}
    return  render(request, "mobile/vivo/vivo Z1X/vivo Z1X.html", context=price)
