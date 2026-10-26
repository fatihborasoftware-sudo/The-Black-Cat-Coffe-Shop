# Live site build (theblackcatcoffeeshop)

What was put on https://fbsoftwarethemes.com.tr/theblackcatcoffeeshop/ from the branded mockup.

- `additional-css.css`: the site-wide Additional CSS (Customizer). Page sections sit inside `<div class="bc">`.
- `elementor/page-<id>.json`: the Elementor element tree of each page.
  52 Ana Sayfa (homepage), 53 The Black Cat, 54 Şubelerimiz, 55 Franchise, 56 Blog, 57 İletişim.
- Blog posts: 60 Filtre Kahve Deneyimi, 61 Kahve Çeşitleri, 62 Kahve Günü!, 63 Neden Biz?
- Contact Form 7: 50 İletişim Formu, 51 Franchise Başvuru Formu.
- Products: import `../woocommerce/products.csv` in WooCommerce (Ürünler > İçe aktar).
  Home page product cards link to a product search by name, so they work as soon as the products exist.


## Native Elementor rebuild (2026-10-26)

All six pages are now built from native Elementor widgets (containers, heading, text-editor, image, button, icon-list, shortcode), so every text, image and button can be edited in the Elementor editor. No HTML widgets are used. `gen.py` generates the JSON in `elementor/`; `additional-css.css` only adds small brand effects (outline text, ghost titles, product and form styling) via CSS classes.

## Update (2026-10-26, later)

- `additional-css.css` is now an exact copy of the live Additional CSS: page headers for Woo/blog pages, repeating coffee pattern backgrounds, cookie banner, rotating "Bayimiz ol" badge, franchise popup, form grid, dropdown menus, Turkish popup-cart labels, hidden comments/reviews.
- `elementor/page-52..57.json` re-exported from the live site (Turkish capital headings, repeat pattern backgrounds, seam fix).
- `widgets/footer6.html`: footer widget area 6 (PayTR logos, cookie banner, badge, franchise popup with CF7 form 51).
- `widgets/site-script.html`: the small script for the cookie banner and popup. WordPress strips `<script>` from widgets, so it lives in an Elementor HTML widget (container `bccookie`) at the bottom of pages 52, 53, 54, 55 and 57. This is the only HTML widget; all page content stays native.
- Images: every file in the WordPress media library is in `../assets/site-images/` (34 files).
