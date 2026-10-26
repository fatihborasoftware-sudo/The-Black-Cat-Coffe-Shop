import json,itertools
B="https://fbsoftwarethemes.com.tr/theblackcatcoffeeshop"
U=B+"/wp-content/uploads/2026/10/"
M={"KAHVE.png":16,"BACKGROUND.png":17,"background-SMALL.png":18,"BACKGROUND.jpg":19,"icon_01.png":20,"icon_02.png":21,"icon_03.png":22,"icon_04.png":23,"kahve2.jpg":24,"aksesuar-1.jpg":25,"hediye.jpg":26,"4-1.png":27,"cropped-SQUE-1.png":30,"1-1.jpg":42,"2-1.jpg":43,"3-1.jpg":44,"4-4.jpg":45,"5-1.jpg":46,"4-1.jpg":47,"4-2.jpg":48,"4-3.jpg":49}
INK="#2D3748";MUTED="#718096";TXT="#4A5568";SOFT="#F7FAFC";SOFT2="#EDF2F7"
cnt=itertools.count(1)
def nid(): return "b%06x"%next(cnt)
def img(f): return {"url":U+f,"id":M[f]}
def dims(t,r=None,b=None,l=None,u="px"):
    r=t if r is None else r;b=t if b is None else b;l=r if l is None else l
    return {"unit":u,"top":str(t),"right":str(r),"bottom":str(b),"left":str(l),"isLinked":t==r==b==l}
def gap(n): return {"column":str(n),"row":str(n),"unit":"px","isLinked":True,"size":n}
SHADOW={"box_shadow_box_shadow_type":"yes","box_shadow_box_shadow":{"horizontal":0,"vertical":10,"blur":30,"spread":0,"color":"rgba(26,32,44,0.08)"}}
def C(children,**s):
    base={"content_width":"full","flex_direction":"column","flex_gap":gap(0),"padding":dims(0)}
    base.update(s);return {"id":nid(),"elType":"container","settings":base,"elements":children,"isInner":False}
def section(children,bg=None,pad=(84,16),**s):
    st={"content_width":"boxed","boxed_width":{"unit":"px","size":1240},"flex_direction":"column","flex_gap":gap(0),"padding":dims(pad[0],pad[1]),"padding_mobile":dims(56,16)}
    if bg=="soft": st.update(background_background="classic",background_color=SOFT)
    elif bg=="soft2": st.update(background_background="classic",background_color=SOFT2)
    elif bg=="pattern": st.update(background_background="classic",background_color="#FFFFFF",background_image=img("background-SMALL.png"),background_repeat="repeat",background_position="top left",background_size="initial")
    st.update(s);return {"id":nid(),"elType":"container","settings":st,"elements":children,"isInner":False}
def W(t,s): return {"id":nid(),"elType":"widget","widgetType":t,"settings":s,"elements":[]}
def H(title,tag="h2",size=38,weight="700",align="center",upper=True,color=INK,cls="",tablet=None,mobile=None,lh=1.1,**x):
    s={"title":title,"header_size":tag,"align":align,"title_color":color,"typography_typography":"custom","typography_font_size":{"unit":"px","size":size},"typography_font_weight":weight,"typography_line_height":{"unit":"em","size":lh}}
    if upper: s["typography_text_transform"]="uppercase"
    if tablet: s["typography_font_size_tablet"]={"unit":"px","size":tablet}
    if mobile: s["typography_font_size_mobile"]={"unit":"px","size":mobile}
    if cls: s["_css_classes"]=cls
    s.update(x);return W("heading",s)
def ST(light,bold,align="center",mb=44): return H(f"<span>{light}</span> {bold}",size=38,mobile=26,align=align,cls="bc-st",_margin=dims(0,0,mb,0))
def T(html,size=15,color=TXT,align="",weight="400",**x):
    s={"editor":html,"text_color":color,"typography_typography":"custom","typography_font_size":{"unit":"px","size":size},"typography_font_weight":weight}
    if align: s["align"]=align
    s.update(x);return W("text-editor",s)
def I(f,alt,width=100,align="center",radius=0,height=None,link=None,**x):
    s={"image":img(f)|{"alt":alt},"image_size":"full","align":align,"width":{"unit":"%","size":width}}
    if radius: s["image_border_radius"]=dims(radius)
    if height: s.update({"height":{"unit":"px","size":height},"object-fit":"cover"})
    if link: s.update(link_to="custom",link={"url":link})
    s.update(x);return W("image",s)
def BTN(text,url,line=False,align="left",small=False,white=False):
    s={"text":text,"link":{"url":url},"align":align}
    if line: s.update(button_text_color=INK,background_background="classic",background_color="rgba(255,255,255,0)",border_border="solid",border_width=dims(2),border_color=INK,hover_color="#FFFFFF",button_background_hover_background="classic",button_background_hover_color=INK,button_hover_border_color=INK)
    if white: s.update(button_text_color=INK,background_background="classic",background_color="#FFFFFF",border_border="solid",border_width=dims(2),border_color="#FFFFFF",hover_color="#FFFFFF",button_background_hover_background="classic",button_background_hover_color=INK,button_hover_border_color=INK)
    if small: s.update(text_padding=dims(7,16),typography_typography="custom",typography_font_size={"unit":"px","size":12})
    return W("button",s)
def SC(code): return W("shortcode",{"shortcode":code})
def row(children,g=32,align="center",mobile_col=True,**x):
    s=dict(flex_direction="row",flex_gap=gap(g),flex_align_items=align,flex_wrap="nowrap")
    if mobile_col: s["flex_direction_mobile"]="column"
    s.update(x);return C(children,**s)
def col(children,w=50,**x):
    s=dict(width={"unit":"%","size":w},width_mobile={"unit":"%","size":100});s.update(x);return C(children,**s)
def grid(children,cols,tab=2,mob=1,g=20):
    return C(children,container_type="grid",grid_columns_grid={"unit":"fr","size":cols},grid_columns_grid_tablet={"unit":"fr","size":tab},grid_columns_grid_mobile={"unit":"fr","size":mob},grid_rows_grid={"unit":"fr","size":1},grid_gaps={"column":str(g),"row":str(g),"unit":"px","isLinked":True},grid_auto_flow="row")
def card(children,pad=(26,22),align="center",**x):
    s=dict(background_background="classic",background_color="#FFFFFF",border_radius=dims(8),padding=dims(pad[0],pad[1]),flex_gap=gap(10),flex_align_items=align,overflow="hidden");s.update(SHADOW);s.update(x);return C(children,**s)
def crumb(here): return T(f'<a href="{B}/">Ana sayfa</a> / {here}',size=13,color=MUTED,align="center")
def phead(ghost,here,h1,sub=None):
    ch=[H(ghost,size=160,tablet=110,mobile=70,weight="800",upper=False,cls="bc-ghost bc-ghost-center",lh=0.9),crumb(here),H(h1,tag="h1",size=56,tablet=44,mobile=34,cls="bc-st",_margin=dims(10,0,0,0))]
    if sub: ch.append(T(f"<p>{sub}</p>",size=16,align="center",_margin=dims(12,0,0,0)))
    return section(ch,bg="soft2",pad=(58,16),css_classes="bc-phead",padding_mobile=dims(44,16))
FEAT=[("01","icon_01.png","Fincan ikonu","Kaliteli çekirdekler","İyi bir kahve iyi bir çekirdek ile başlar!"),("02","icon_02.png","Madalya ikonu","En uygun kavurma","Dünya standartlarında kavurma yöntemleri ile kavrulur!"),("03","icon_03.png","Kahve çekirdeği ikonu","Özel paketleme","Uygun koşullarda dayanıklı kalacak şekilde paketlenir!"),("04","icon_04.png","Kahve paketi ikonu","Mükemmel aroma","Sonucunda da mükemmel bir aroma verir!")]
def features(): return section([grid([card([H(n,tag="div",size=12,weight="600",color=MUTED,cls="bc-dot"),I(i,a,width=None) if False else W("image",{"image":img(i)|{"alt":a},"image_size":"full","align":"center","width":{"unit":"px","size":36}}),H(h,tag="h3",size=16),T(f"<p>{p}</p>",size=13,color=MUTED,align="center")]) for n,i,a,h,p in FEAT],4)],bg="soft")
SHOP=B+"/shop/";cat=lambda s:f"{B}/?product_cat={s}";pg=lambda i:f"{B}/?page_id={i}"
out={}
# HOME
out[52]=[
 section([row([col([H("Gerçek kahveyi<br>keşfet!",tag="h1",size=78,tablet=56,mobile=44,align="left",lh=1.02,align_mobile="center"),T("<p>Kendi kavurduğumuz çekirdekler, beş şehirdeki şubelerimizde ve online mağazamızda.</p>",size=17,align="left",align_mobile="center",_margin=dims(22,0,30,0)),row([BTN("Kahve Noktaları",pg(54)),BTN("Kahve Al!",SHOP,line=True)],g=12,mobile_col=False,flex_wrap="wrap",flex_justify_content_mobile="center")]),col([I("KAHVE.png","Black Cat logolu fincandan sıçrayan kahve ve çekirdekler",align="right",_css_classes="bc-float",align_mobile="center",width_mobile={"unit":"%","size":80})])])],pad=(40,16),background_background="classic",background_color="#FFFFFF",background_image=img("BACKGROUND.png"),background_position="center center",background_repeat="no-repeat",background_size="contain"),
 features(),
 section([ST("Online","ürünlerimiz"),grid([C([H(t,tag="h3",size=24,mobile=22,align="left",cls="bc-cat-title"),BTN("İncele",u,small=True,white=True)],background_background="classic",background_image=img(f),background_size="cover",background_position="center center",min_height={"unit":"px","size":214},min_height_mobile={"unit":"px","size":160},flex_justify_content="center",flex_align_items="flex-start",flex_gap=gap(12),padding=dims(0,22),border_radius=dims(8),overflow="hidden",**SHADOW) for t,f,u in [("Kahveler","kahve2.jpg",cat("kahveler")),("Aksesuar","aksesuar-1.jpg",cat("aksesuarlar")),("Hediye<br>paketleri","hediye.jpg",cat("hediye-paketleri"))]],3,tab=1)]),
 section([row([col([H("The Black Cat",size=92,tablet=64,mobile=50,weight="800",upper=False,align="left",cls="bc-ghost",lh=0.9),H("The Black Cat termosunu getir",size=28,mobile=20,align="left",_margin=dims(-30,0,0,0)),H("%20",tag="div",size=128,mobile=80,weight="300",align="left",cls="bc-outline",lh=1),H("İndirimli kahveni al",tag="h3",size=28,mobile=20,align="left",_margin=dims(0,0,22,0)),BTN("Termoslar",cat("aksesuarlar"),line=True)],padding=dims(40,0,40,44),padding_mobile=dims(30,22,0,22)),col([],min_height={"unit":"px","size":340},min_height_mobile={"unit":"px","size":220},background_background="classic",background_image=img("BACKGROUND.jpg"),background_size="cover",background_position="center right")],g=20,align="stretch",background_background="classic",background_color="#FFFFFF",border_radius=dims(10),overflow="hidden",**SHADOW)],bg="pattern",pad=(20,16)),
 section([ST("Popüler","ürünlerimiz"),C([SC('[products limit="6" columns="3" orderby="popularity" category="kahveler"]')],css_classes="bc-products"),C([BTN("Tüm ürünler",SHOP,line=True,align="center")],margin=dims(24,0,0,0))],bg="pattern",border_border="solid",border_width=dims(1,0,0,0),border_color="#E2E8F0"),
 section([ST("Sipariş","takip"),row([col([SC("[woocommerce_order_tracking]")],w=55),col([I("4-1.png","Kedi silüetinde Black Cat ekibi fotoğrafları")],w=45)],g=40)],bg="soft",_element_id="takip"),
]
# ABOUT
out[53]=[
 phead("Black Cat","Hakkımızda","<span>Hakkımızda</span> The Black Cat"),
 section([row([col([I("4-1.png","Kedi silüetinde Black Cat ekibi fotoğrafları")]),col([H("<span>Hakkımızda</span><br>The Black Cat",align="left",cls="bc-st",mobile=26,_margin=dims(0,0,18,0)),T("<p>The Black Cat, iyi kahvenin karmaşık olmak zorunda olmadığına inanan küçük bir ekip olarak başladı.</p>",size=20,color=INK,weight="500"),T("<p>Çekirdeklerimizi Kolombiya'dan Ruanda'ya farklı kökenlerden seçiyor, kendi atölyemizde küçük partiler hâlinde kavuruyoruz. Her kökenin kendine has tadını korumak için kavurma profillerini tek tek ayarlıyoruz.</p><p>Bugün beş şehirdeki şubelerimizde ve online mağazamızda, her paketi kavrumdan sonraki birkaç gün içinde size ulaştırmaya çalışıyoruz.</p>")])],g=56)]),
 features(),
 section([row([col([W("image",{"image":img("cropped-SQUE-1.png")|{"alt":"Black Cat amblemi"},"image_size":"full","align":"left","width":{"unit":"px","size":160},"_margin":dims(0,0,20,0)}),H("<span>Kahvemizi artık</span><br>kendimiz kavuruyoruz!",size=60,tablet=44,mobile=34,align="left",lh=1,cls="bc-st"),row([C([H(v,tag="div",size=28,align="left"),T(f"<p>{l}</p>",size=12,color=MUTED)]) for v,l in [("12 dk","ORTALAMA KAVURMA"),("205°C","BİTİŞ SICAKLIĞI"),("48 sa","DİNLENME")]],g=28,mobile_col=False,flex_wrap="wrap",margin=dims(24,0,0,0))],w=40),col([T("<p>Çekirdek seçiminden soğutmaya kadar her partiyi kendi atölyemizde takip ediyoruz.</p>",size=20,color=INK,weight="500"),T("<p>Böylece rafta bekleyen değil, yeni kavrulmuş kahve satıyoruz. Her paketin üzerinde kavrum tarihi yazar.</p>")],w=60)],g=50)]),
 section([ST("Bizden","kareler"),grid([I(f,a,radius=8,height=420) for f,a in [("4-3.jpg","Black Cat barista ekibi"),("4-1.jpg","Espresso makineleri başında barista"),("4-2.jpg","Kahve hazırlayan barista")]],3,tab=3,mob=1,g=16)],bg="pattern",border_border="solid",border_width=dims(1,0,0,0),border_color="#E2E8F0"),
]
# BRANCHES
BR=[("İSTANBUL","istanbul","1-1.jpg","Fevzipaşa Cd. No:1 Beyoğlu İstanbul","%C4%B0stanbul"),("İZMİR","izmir","2-1.jpg","Adres eklenecek","%C4%B0zmir"),("ANTALYA","antalya","3-1.jpg","Adres eklenecek","Antalya"),("ANKARA","ankara","4-4.jpg","Adres eklenecek","Ankara"),("BURSA","bursa","5-1.jpg","Adres eklenecek","Bursa")]
def il(items): return W("icon-list",{"icon_list":[{"_id":nid()[1:],"text":t,"selected_icon":{"value":ic,"library":"fa-solid"},**({"link":{"url":l}} if l else {})} for t,ic,l in items],"icon_color":INK,"text_color":TXT,"space_between":{"unit":"px","size":10},"icon_typography_typography":"custom","icon_typography_font_size":{"unit":"px","size":15}})
brs=[]
for i,(c,idn,f,a,q) in enumerate(BR):
    brs.append(C([col([I(f,f"{c.title()} şubesi",height=340,height_mobile={"unit":"px","size":220})]),col([H(f"<span>{c}</span> Şube",tag="h3",size=30,align="left",cls="bc-st"),il([("444 11 844","fas fa-phone","tel:44411844"),(a,"fas fa-map-marker-alt",""),("Her gün 08:00 – 22:00","fas fa-clock","")]),BTN("Haritalar'da aç",f"https://www.google.com/maps/search/?api=1&query=The%20Black%20Cat%20Coffee%20{q}",line=True)],padding=dims(34),padding_mobile=dims(24),flex_gap=gap(16),flex_justify_content="center")],flex_direction="row-reverse" if i%2 else "row",flex_direction_mobile="column",flex_gap=gap(0),flex_align_items="stretch",background_background="classic",background_color="#FFFFFF",border_radius=dims(10),overflow="hidden",margin=dims(0,0,24,0),_element_id=idn,**SHADOW))
out[54]=[phead("Şubelerimiz","Şubelerimiz","<span>Şubelerimiz</span> The Black Cat"),section(brs,bg="pattern")]
# FRANCHISE
STEPS=[("01","Başvuru","Formu doldurun, bölgenizi ve hedeflerinizi paylaşın."),("02","Tanışma","Ekibimiz sizinle görüşür, lokasyonu birlikte değerlendiririz."),("03","Eğitim","Barista ve işletme eğitimleri kavurma atölyemizde verilir."),("04","Açılış","Tedarik, tasarım ve açılış desteğiyle kapılarınızı açarsınız.")]
out[55]=[
 phead("Franchise","Franchise","<span>Franchise</span> bayimiz olun!","Kendi şehrinde bir Black Cat açmak ister misin? Kahveyi, eğitimi ve markayı biz getiriyoruz."),
 section([row([col([I("2-1.jpg","İzmir şubesinde kahve hazırlayan barista",radius=10)]),col([H("<span>Kahvemizi artık</span><br>kendimiz kavuruyoruz!",align="left",cls="bc-st",mobile=26,_margin=dims(0,0,18,0)),T("<p>Kendi kavurduğumuz kahve, hazır online mağaza altyapısı ve tanınan bir marka ile kendi kahve noktanızı açın.</p>",size=20,color=INK,weight="500"),T("<p>Lokasyon seçiminden açılışa kadar her adımda yanınızdayız.</p>"),BTN("Başvuru formu","#basvuru")],flex_gap=gap(8))],g=56)]),
 section([ST("Başvurudan","açılışa"),grid([card([H(n,tag="div",size=40,weight="300",align="left",cls="bc-outline",lh=1),H(h,tag="h3",size=17,align="left"),T(f"<p>{p}</p>",size=13.5,color=MUTED)],pad=(24,24),align="flex-start") for n,h,p in STEPS],4)],bg="soft"),
 section([ST("Başvuru","formu"),C([card([SC('[contact-form-7 id="51" title="Franchise Başvuru Formu"]')],pad=(30,30),align="stretch",css_classes="bc-form")],max_width={"unit":"px","size":760},width={"unit":"%","size":100},margin=dims(0,"auto",0,"auto"),flex_align_items="stretch")],bg="pattern",_element_id="basvuru",flex_align_items="center"),
]
# BLOG
POSTS=[(60,"Filtre Kahve Deneyimi","3-1.jpg","V60 ile evde filtre kahve: oran, öğütme ve su sıcaklığı. Kafedeki tadı evde yakalamanın en kısa yolu."),(61,"Kahve Çeşitleri","4-4.jpg","Espresso, filtre, Türk kahvesi… Hangi demleme yöntemi hangi çekirdekle daha iyi sonuç verir, kısa bir rehber."),(62,"Kahve Günü!","2-1.jpg","Dünya Kahve Günü'nü şubelerimizde nasıl kutladığımıza bir göz atın."),(63,"Neden Biz?","5-1.jpg","Çekirdeği seçmekten paketlemeye kadar her adımı neden kendimiz yapıyoruz?")]
out[56]=[phead("Blog","Blog","Blog"),section([grid([card([I(f,t,height=300,link=f"{B}/?p={i}",height_mobile={"unit":"px","size":200}),C([T("<p>Blog · The Black Cat</p>",size=12,color=MUTED),H(f'<a href="{B}/?p={i}">{t}</a>',tag="h3",size=22,align="left"),T(f"<p>{x}</p>",size=14),BTN("Devamını oku",f"{B}/?p={i}",line=True,small=True)],padding=dims(22,24,24,24),flex_gap=gap(10),flex_align_items="flex-start")],pad=(0,0),align="stretch") for i,t,f,x in POSTS],2,tab=2,mob=1,g=28)],bg="pattern")]
# CONTACT
info=[("Çağrı merkezi",'<a href="tel:44411844">444 11 844</a>'),("Merkez","Fevzipaşa Cd. No:1<br>Beyoğlu, İstanbul"),("Çalışma saatleri","Her gün 08:00 – 22:00"),("E-posta",'<a href="mailto:info@fbsoftwarethemes.com.tr">info@fbsoftwarethemes.com.tr</a>')]
out[57]=[phead("İletişim","İletişim","<span>The Black Cat</span> bizimle iletişime geçin"),section([row([col([C([T(f"<p>{k.upper()}</p>",size=11,color=MUTED,weight="600"),T(f"<p>{v}</p>",size=20,color=INK,weight="600")]) for k,v in info],w=45,flex_gap=gap(22)),col([card([H("İletişim formu",size=22,align="left"),SC('[contact-form-7 id="50" title="İletişim Formu"]')],pad=(30,30),align="stretch",css_classes="bc-form")],w=55)],g=56,align="flex-start")],bg="pattern")]
for k,v in out.items(): open(f"p{k}.json","w").write(json.dumps(v,ensure_ascii=False,separators=(",",":")))
print({k:len(json.dumps(v,ensure_ascii=False,separators=(",",":"))) for k,v in out.items()})
