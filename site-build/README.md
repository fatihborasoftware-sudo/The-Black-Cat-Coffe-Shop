# Live site build (theblackcatcoffeeshop)

What was put on https://fbsoftwarethemes.com.tr/theblackcatcoffeeshop/ from the branded mockup.

- `additional-css.css`: the site-wide Additional CSS (Customizer). Page sections sit inside `<div class="bc">`.
- `elementor/page-<id>.json`: the Elementor element tree of each page.
  52 Ana Sayfa (homepage), 53 The Black Cat, 54 Şubelerimiz, 55 Franchise, 56 Blog, 57 İletişim.
- Blog posts: 60 Filtre Kahve Deneyimi, 61 Kahve Çeşitleri, 62 Kahve Günü!, 63 Neden Biz?
- Contact Form 7: 50 İletişim Formu, 51 Franchise Başvuru Formu.
- Products: import `../woocommerce/products.csv` in WooCommerce (Ürünler > İçe aktar).
  Home page product cards link to a product search by name, so they work as soon as the products exist.
