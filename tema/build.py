"""Genera los JSON del tema 'Lunerie · marca' (Horizon 4.2) a partir de la página de marca."""
import json, pathlib

OUT = pathlib.Path(__file__).parent
INK, GREEN, GOLD, MIST, LINE, SOFT = "#16201B", "#006039", "#A6834A", "#F2F4F2", "#E2E6E3", "#3D4842"
FG = "{{ settings.color_palette.foreground }}"
BG = "{{ settings.color_palette.background }}"
C1 = "{{ settings.color_palette.color1 }}"
C2 = "{{ settings.color_palette.color2 }}"

settings = {
    "logo_height": 36, "logo_height_mobile": 28,
    "color_palette": {"background": "#FFFFFF", "foreground": INK, "color1": SOFT, "color2": LINE},
    "page_background_color": BG, "page_text_color": FG, "page_width": "narrow",
    # Letras: Cormorant (títulos) + Jost ligera (texto)
    "type_body_font": "jost_n3", "type_subheading_font": "jost_n4",
    "type_heading_font": "cormorant_n4", "type_accent_font": "cormorant_n5",
    "type_size_paragraph": "16", "type_line_height_paragraph": "body-loose",
    "type_font_h1": "heading", "type_size_h1": "48", "type_line_height_h1": "display-tight",
    "type_letter_spacing_h1": "heading-normal", "type_case_h1": "none",
    "type_font_h2": "heading", "type_size_h2": "40", "type_line_height_h2": "display-tight",
    "type_letter_spacing_h2": "heading-normal", "type_case_h2": "none",
    "type_font_h3": "heading", "type_size_h3": "32", "type_line_height_h3": "display-normal",
    "type_letter_spacing_h3": "heading-normal", "type_case_h3": "none",
    "type_font_h4": "heading", "type_size_h4": "24", "type_line_height_h4": "display-tight",
    "type_letter_spacing_h4": "heading-normal", "type_case_h4": "none",
    "type_font_h5": "subheading", "type_size_h5": "12", "type_line_height_h5": "display-loose",
    "type_letter_spacing_h5": "heading-loose", "type_case_h5": "uppercase",
    "type_font_h6": "subheading", "type_size_h6": "12", "type_line_height_h6": "display-loose",
    "type_letter_spacing_h6": "heading-loose", "type_case_h6": "uppercase",
    # Sin animaciones
    "page_transition_enabled": False, "transition_to_main_product": False,
    "add_to_cart_animation": False, "card_hover_effect": "none",
    # Etiquetas discretas
    "badge_position": "top-left", "badge_corner_radius": 0,
    "badge_sale_background_color": BG, "badge_sale_text_color": FG,
    "badge_sold_out_background_color": MIST, "badge_sold_out_text_color": FG,
    "badge_font_family": "body", "badge_text_transform": "uppercase",
    # Botones: verde, rectos, mayúsculas (el verde solo en lo que se pulsa)
    "palette_primary_button_background": GREEN, "palette_primary_button_text": "#FFFFFF",
    "palette_primary_button_border": GREEN, "primary_button_border_width": 0,
    "button_border_radius_primary": 0, "type_font_button_primary": "body",
    "button_text_case_primary": "uppercase",
    "palette_secondary_button_background": "rgba(0,0,0,0)", "palette_secondary_button_text": FG,
    "palette_secondary_button_border": FG, "secondary_button_border_width": 1,
    "button_border_radius_secondary": 0, "type_font_button_secondary": "body",
    "button_text_case_secondary": "uppercase", "pills_border_radius": 0,
    # Cesta
    "cart_type": "drawer", "product_title_case": "default", "cart_price_font": "body",
    "auto_open_cart_drawer": True, "show_cart_note": False, "show_add_discount_code": True,
    "show_installments": False, "show_accelerated_checkout_buttons": True,
    "drawer_background_color": BG, "drawer_text_color": FG, "drawer_border_color": C2,
    "icon_stroke": "thin",
    "palette_input_background": BG, "palette_input_text": FG, "palette_input_border": C2,
    "input_border_width": 1, "inputs_border_radius": 0,
    "popover_background_color": BG, "popover_text_color": FG, "popover_border_radius": 0,
    "popover_border_color": C2, "popover_border_width": 1, "popover_drop_shadow": False,
    "currency_code_enabled_product_pages": False, "currency_code_enabled_product_cards": False,
    "currency_code_enabled_cart_items": False, "currency_code_enabled_cart_total": False,
    # Fichas de producto: foto con fondo niebla, sin zoom ni carrusel
    "quick_add": False, "mobile_quick_add": False, "quick_add_background": BG, "quick_add_text": FG,
    "show_second_image_on_hover": True, "product_card_carousel": False,
    "product_corner_radius": 0, "card_corner_radius": 0, "card_title_case": "default",
    # Muestras de color redondas, como en la maqueta
    "show_variant_image": False, "variant_swatch_width": 34, "variant_swatch_height": 34,
    "variant_swatch_radius": 100, "variant_swatch_border_style": "solid",
    "variant_swatch_border_width": 1, "variant_swatch_border_opacity": 20,
    "palette_variant_background": BG, "palette_variant_text": FG, "palette_variant_border": C2,
    "palette_selected_variant_background": FG, "palette_selected_variant_text": BG,
    "palette_selected_variant_border": FG, "variant_button_border_width": 1,
    "variant_button_radius": 0, "variant_button_width": "equal-width-buttons",
}
(OUT / "settings_data.json").write_text(
    json.dumps({"current": settings, "presets": {}}, ensure_ascii=False, indent=2), encoding="utf8")

LOGO_CSS = (".header-logo { font-family: var(--font-heading--family); font-weight: 400; "
            "font-size: 1.5rem; letter-spacing: 0.38em; text-transform: uppercase; padding-inline-start: 0.38em; } "
            "@media screen and (max-width: 749px) { .header-logo { font-size: 1.2rem; letter-spacing: 0.3em; } }")

header = {
    "type": "header", "name": "t:names.header",
    "sections": {
        "header_announcements_9jGBFp": {
            "type": "header-announcements",
            "blocks": {"announcement_BxgCk9": {"type": "_announcement", "settings": {
                "text": "Envío gratis a península · Devolución en 14 días",
                "font": "var(--font-body--family)", "font_size": "0.75rem", "weight": "400",
                "letter_spacing": "loose", "case": "uppercase", "text_color": "#FFFFFF"},
                "blocks": {}}},
            "block_order": ["announcement_BxgCk9"],
            "name": "t:names.announcement_bar",
            "settings": {"speed": 5, "section_width": "full-width", "background_color": GREEN,
                         "divider_width": 0, "padding-block-start": 9, "padding-block-end": 9},
        },
        "header_section": {
            "type": "header",
            "blocks": {
                "header-logo": {"type": "_header-logo", "static": True, "settings": {
                    "hide_logo_on_home_page": False, "padding-block-start": 0, "padding-block-end": 0},
                    "blocks": {}},
                "header-menu": {"type": "_header-menu", "static": True, "settings": {
                    "menu": "main-menu", "type_font_primary_size": "0.75rem", "menu_font_style": "inverse",
                    "type_font_primary_link": "body", "type_case_primary_link": "uppercase",
                    "menu_style": "featured_products", "featured_products_aspect_ratio": "4 / 5",
                    "featured_collections_aspect_ratio": "16 / 9", "image_border_radius": 0,
                    "navigation_bar": False, "drawer_accordion": False,
                    "drawer_accordion_expand_first": False, "drawer_dividers": False},
                    "blocks": {}},
            },
            "custom_css": [LOGO_CSS],
            "settings": {
                "logo_position": "center", "menu_position": "left", "menu_row": "top",
                "show_search": True, "search_position": "right", "search_row": "top",
                "show_country": False, "country_selector_style": False, "show_language": False,
                "localization_font": "body", "localization_font_size": "0.75rem",
                "localization_position": "right", "localization_row": "top",
                "section_width": "page-width", "section_height": "standard",
                "enable_sticky_header": "always", "divider_width": 1, "divider_size": "full-width",
                "divider_color": LINE, "border_width": 0,
                "actions_display_style": "icon", "actions_font_size": "0.75rem",
                "actions_font": "body", "actions_text_case": "uppercase",
                "background_color_top": BG,
                "enable_transparent_header_home": False, "enable_transparent_header_product": False,
                "enable_transparent_header_collection": False,
            },
        },
    },
    "order": ["header_announcements_9jGBFp", "header_section"],
}
(OUT / "header-group.json").write_text(json.dumps(header, ensure_ascii=False, indent=2), encoding="utf8")


def text_block(html, preset, align="left"):
    return {"type": "text", "settings": {
        "text": html, "width": "100%", "max_width": "normal", "alignment": align, "type_preset": preset,
        "font": "var(--font-body--family)", "font_size": "1rem", "line_height": "normal",
        "letter_spacing": "normal", "case": "none", "wrap": "pretty", "background": False,
        "background_color": "#00000026", "corner_radius": 0, "padding-block-start": 0,
        "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}}


footer = {
    "type": "footer", "name": "t:names.footer",
    "sections": {
        "footer_m9NzUG": {
            "type": "footer",
            "blocks": {
                "group_H6VpwJ": {"type": "group", "settings": {
                    "content_direction": "column", "vertical_on_mobile": True,
                    "horizontal_alignment": "flex-start", "vertical_alignment": "center",
                    "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start",
                    "vertical_alignment_flex_direction_column": "center", "gap": 6, "width": "fill",
                    "custom_width": 100, "width_mobile": "fill", "custom_width_mobile": 100,
                    "height": "fit", "custom_height": 100, "background_media": "none",
                    "video_position": "cover", "background_image_position": "cover", "border": "none",
                    "border_width": 1, "border_opacity": 100, "border_radius": 0, "toggle_overlay": False,
                    "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top",
                    "open_in_new_tab": False, "padding-block-start": 0, "padding-block-end": 0,
                    "padding-inline-start": 0, "padding-inline-end": 0},
                    "blocks": {
                        "text_LWt8Pz": text_block("<h2>Cartas de Lunerie</h2>", "h4"),
                        "text_f9CFLH": text_block("<p>Piezas nuevas y fechas de envío para regalar. Pocas veces al mes.</p>", "rte"),
                    },
                    "block_order": ["text_LWt8Pz", "text_f9CFLH"]},
                "email_signup_crihX7": {"type": "email-signup", "settings": {
                    "width": "fill", "custom_width": 100, "heading_preset": "h3", "border_style": "all",
                    "input_style": "custom", "border_width": 1, "border_radius": 0,
                    "input_background_color": BG, "input_text_color": FG, "input_border_color": C2,
                    "input_type_preset": "paragraph", "style_class": "button-unstyled",
                    "display_type": "arrow", "label": "Tu email", "integrated_button": True,
                    "button_type_preset": "paragraph", "padding-block-start": 0, "padding-block-end": 0,
                    "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
            },
            "block_order": ["group_H6VpwJ", "email_signup_crihX7"],
            "name": "t:names.footer",
            "settings": {"section_width": "page-width", "gap": 20, "background_color": MIST,
                         "padding-block-start": 40, "padding-block-end": 30},
        },
        "footer_utilities_jLGE8U": {
            "type": "footer-utilities",
            "blocks": {
                "footer_copyright_jweRK8": {"type": "footer-copyright", "settings": {
                    "show_powered_by": False, "font_size": "0.75rem", "case": "none"}, "blocks": {}},
                "footer_policy_list_VCdnpa": {"type": "footer-policy-list", "settings": {
                    "font_size": "0.75rem", "case": "none"}, "blocks": {}},
            },
            "block_order": ["footer_copyright_jweRK8", "footer_policy_list_VCdnpa"],
            "name": "t:names.utilities",
            "settings": {"section_width": "page-width", "gap": 24, "divider_thickness": 1,
                         "divider_color": LINE, "background_color": MIST,
                         "padding-block-start": 20, "padding-block-end": 40},
        },
    },
    "order": ["footer_m9NzUG", "footer_utilities_jLGE8U"],
}
(OUT / "footer-group.json").write_text(json.dumps(footer, ensure_ascii=False, indent=2), encoding="utf8")


def group(blocks, align="center", gap=8):
    """Columna de bloques (los ajustes que no se ponen toman el valor por defecto del tema)."""
    return {"type": "group", "settings": {
        "content_direction": "column", "horizontal_alignment_flex_direction_column": align,
        "gap": gap, "width": "fill"},
        "blocks": blocks, "block_order": list(blocks)}


# Bolitas de color (como Calné): los botones de la opción Color cuyo valor empieza por Dorado / Plateado /
# Oro rosa se pintan como círculos. Shopify no deja enlazar los colores estándar por API (10-oct), por eso va
# por CSS y vale para cualquier producto con esos nombres. «Color: valor» lo pone tema/codigo/snippets/
# variant-main-picker.liquid, que además incluye estas reglas con {% render 'lunerie-bolitas' %} (el CSS
# personalizado de una sección no admite más de 500 caracteres). Si se añade otro metal, añadirlo en BOLITAS.
BOLITAS = {"Dorado": "#D4AF5F", "Plateado": "#C9CDD0", "Oro rosa": "#D8A48F"}
_sel = ", ".join(f'input[value^="{v}"]' for v in BOLITAS)
SWATCH_CSS = (
    f".variant-option--buttons:has({_sel}) {{ display: flex; flex-wrap: wrap; gap: 12px; }} "
    f".variant-option__button-label:has({_sel}) {{ flex: 0 0 auto; width: 40px; height: 40px; min-width: 40px; "
    f"padding: 0; border-radius: 50%; border: 1px solid {LINE}; box-shadow: inset 0 0 0 4px #FFFFFF; "
    f"font-size: 0; overflow: hidden; }} "
    f".variant-option__button-label:has({_sel}) .variant-option__button-label__pill, "
    f".variant-option__button-label:has({_sel}) .variant-option__button-label__text {{ display: none; }} "
    f".variant-option__button-label:has({_sel}):has(input:checked) {{ border: 2px solid {INK}; }} "
    + " ".join(f'.variant-option__button-label:has(input[value^="{v}"]) {{ background: {c} !important; }}'
               for v, c in BOLITAS.items()))

# ---------- Inicio: pieza destacada (reloj Lune) · portada sin foto (fondo niebla) · las piezas · tres promesas ----------
# Cuando haya fotos propias: en el editor, Portada → Fondo → Imagen.
index = {
    "sections": {
        "portada": {
            "type": "section",
            "blocks": {
                "antetitulo": text_block("<p>Joyas y relojes para regalar</p>", "h6", "center"),
                "titulo": text_block("<h1>Para llevar cerca.</h1>", "h1", "center"),
                "boton": {"type": "button", "settings": {
                    "label": "Ver las piezas", "link": "shopify://collections/all",
                    "style_class": "button", "width": "fit-content"}, "blocks": {}},
            },
            "block_order": ["antetitulo", "titulo", "boton"],
            "settings": {
                "content_direction": "column", "horizontal_alignment_flex_direction_column": "center",
                "vertical_alignment_flex_direction_column": "center", "gap": 20,
                "section_width": "full-width", "section_height": "medium", "background_color": MIST,
                "padding-block-start": 64, "padding-block-end": 64},
        },
        # Pieza anclada en el inicio: ficha completa (fotos, precio, variantes, comprar)
        "destacado": {
            "type": "featured-product-information",
            "blocks": {
                "media-gallery": {"type": "_featured-product-information-carousel", "static": True, "settings": {
                    "constrain_to_viewport": True, "media_fit": "cover", "media_radius": 0,
                    "extend_media": False, "hide_variants": True, "slideshow_controls_style": "thumbnails",
                    "slideshow_mobile_controls_style": "dots", "thumbnail_position": "bottom",
                    "thumbnail_width": 56}, "blocks": {}},
                "product-details": {"type": "_product-details", "static": True, "settings": {
                    "gap": 24, "sticky_details_desktop": False,
                    "padding-block-start": 24, "padding-block-end": 24},
                    "blocks": {
                        "cabecera": group({
                            "titulo": {"type": "product-title", "settings": {"type_preset": "h2"}, "blocks": {}},
                            "precio": {"type": "price", "settings": {
                                "show_sale_price_first": True, "show_installments": False,
                                "show_tax_info": False, "type_preset": "paragraph"}, "blocks": {}},
                        }, align="flex-start", gap=10),
                        "variantes": {"type": "variant-picker", "settings": {
                            "variant_style": "buttons", "show_swatches": True}, "blocks": {}},
                        "comprar": {"type": "buy-buttons", "settings": {"stacking": True,
                            "show_pickup_availability": False},
                            "blocks": {
                                "quantity": {"type": "quantity", "static": True, "settings": {
                                    "border_width": 1, "border_radius": 0}, "blocks": {}},
                                "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {
                                    "style_class": "button"}, "blocks": {}},
                                "accelerated-checkout": {"type": "accelerated-checkout", "static": True,
                                    "settings": {}, "blocks": {}},
                            }, "block_order": []},
                        "ver_ficha": {"type": "button", "settings": {
                            "label": "Ver la pieza", "link": "{{ closest.product.url }}",
                            "style_class": "link", "width": "fit-content"}, "blocks": {}},
                    },
                    "block_order": ["cabecera", "variantes", "comprar", "ver_ficha"]},
            },
            "block_order": [],
            "settings": {
                "product": "reloj-lune", "content_width": "content-center-aligned",
                "desktop_media_position": "left", "equal_columns": True, "limit_details_width": True,
                "gap": 48, "background_color": BG, "padding-block-start": 56, "padding-block-end": 24},
        },
        "piezas": {
            "type": "product-list",
            "blocks": {
                "static-header": {"type": "_product-list-content", "static": True, "settings": {
                    "content_direction": "row", "horizontal_alignment": "space-between",
                    "vertical_alignment": "flex-end", "align_baseline": True},
                    "blocks": {
                        "titulo": {"type": "_product-list-text", "settings": {
                            "text": "<h2>Las piezas</h2>", "type_preset": "h3"}, "blocks": {}},
                        "ver_todo": {"type": "_product-list-button", "settings": {
                            "label": "Ver todo", "style_class": "link"}, "blocks": {}},
                    },
                    "block_order": ["titulo", "ver_todo"]},
                "static-product-card": {"type": "_product-card", "static": True,
                    "settings": {"product_card_gap": 6},
                    "blocks": {
                        "foto": {"type": "_product-card-gallery", "settings": {"image_ratio": "adapt"}, "blocks": {}},
                        "nombre": {"type": "product-title", "settings": {"type_preset": "rte"}, "blocks": {}},
                        "precio": {"type": "price", "settings": {"type_preset": "paragraph"}, "blocks": {}},
                    },
                    "block_order": ["foto", "nombre", "precio"]},
            },
            "settings": {
                "collection": "all", "layout_type": "grid", "max_products": 6, "columns": 3,
                "mobile_columns": "2", "columns_gap": 16, "rows_gap": 32, "section_width": "page-width",
                "gap": 32, "background_color": BG, "padding-block-start": 64, "padding-block-end": 48},
        },
        "promesas": {
            "type": "section",
            "blocks": {
                "envio": group({
                    "t": text_block("<h3>Envío gratis</h3>", "h6", "center"),
                    "p": text_block("<p>A península, con seguimiento por email.</p>", "rte", "center")}),
                "devolucion": group({
                    "t": text_block("<h3>14 días para devolverlo</h3>", "h6", "center"),
                    "p": text_block("<p>Si no te convence, nos lo devuelves. Salvo piezas personalizadas.</p>", "rte", "center")}),
                "garantia": group({
                    "t": text_block("<h3>Garantía de 3 años</h3>", "h6", "center"),
                    "p": text_block("<p>Si falla, te lo reparamos o te lo cambiamos.</p>", "rte", "center")}),
            },
            "block_order": ["envio", "devolucion", "garantia"],
            "settings": {
                "content_direction": "row", "vertical_on_mobile": True, "horizontal_alignment": "space-between",
                "vertical_alignment": "flex-start", "gap": 32, "section_width": "page-width",
                "border": "solid", "border_width": 1, "border_color": LINE,
                "padding-block-start": 48, "padding-block-end": 48},
        },
    },
    "order": ["destacado", "portada", "piezas", "promesas"],
}
(OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf8")


# ---------- Ficha de producto (estructura de la de Calné, con las reglas de la marca) ----------
# De Calné se copia el orden: migas · título · precio · línea · ventajas con icono · color · botón ancho ·
# caja de oferta · tres iconos · desplegables. NO se copia: precio tachado, «stock limitado», «oferta solo hoy»,
# «100 % resistente al agua», 2 años de garantía ni 100 días (en España: 14 días y 3 años; el reloj no es sumergible).
def row(heading, html, abierto=False):
    return {"type": "_accordion-row", "settings": {"heading": heading, "icon": "none", "open_by_default": abierto},
            "blocks": {"texto": text_block(html, "rte")}, "block_order": ["texto"]}


def small(bloque, size="0.875rem"):
    """Texto en tamaño propio (preset «custom»)."""
    bloque["settings"].update({"type_preset": "custom", "font_size": size})
    return bloque


def color(bloque, c, ancho="fit-content"):
    bloque["settings"].update({"text_color": c, "width": ancho})
    return bloque


def liquid(codigo):
    """Bloque de Liquid/HTML libre (para lo que los bloques del tema no permiten: animaciones, iconos propios)."""
    return {"type": "custom-liquid", "settings": {"custom_liquid": codigo}, "blocks": {}}


ROJO = "#B3261E"
# Urgencia de Navidad: bolita roja que late (sin animación si el móvil pide «reducir movimiento»).
# FECHA A CONFIRMAR con el plazo real del proveedor ([PLAZO]).
NAVIDAD = liquid(
    '<p class="lu-urgencia"><span class="lu-punto" aria-hidden="true"></span>'
    'Para Navidad, pídelo antes del 1 de diciembre</p>'
    "<style>.lu-urgencia,.lu-regalo{font-family:var(--font-body--family);font-weight:var(--font-body--weight)}"
    ".lu-urgencia{display:flex;align-items:center;gap:12px;margin:0;font-size:1rem;color:" + ROJO + "}"
    ".lu-punto{position:relative;flex:0 0 9px;width:9px;height:9px;margin-inline:4px 5px;border-radius:50%;"
    "background:" + ROJO + "}"
    ".lu-punto::after{content:'';position:absolute;inset:0;border-radius:50%;background:" + ROJO + ";"
    "animation:lu-latido 1.6s ease-out infinite}"
    "@keyframes lu-latido{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.6);opacity:0}}"
    "@media (prefers-reduced-motion:reduce){.lu-punto::after{animation:none;opacity:0}}</style>")

# Caja de regalo con icono de regalo (Horizon no trae ese icono: SVG propio, trazo fino como los demás)
REGALO = liquid(
    '<p class="lu-regalo"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="3.5" y="8.5" width="17" height="4" rx=".6"/><path d="M5 12.5v8h14v-8M12 8.5v12"/>'
    '<path d="M12 8.5C10.2 4.6 6.6 4.7 6.9 7c.2 1.4 2.8 1.5 5.1 1.5M12 8.5c1.8-3.9 5.4-3.8 5.1-1.5-.2 1.4-2.8 1.5-5.1 1.5"/>'
    '</svg>Llega en su caja de regalo</p>'
    "<style>.lu-regalo{display:flex;align-items:center;gap:12px;margin:0;font-size:1rem}"
    ".lu-regalo svg{flex:0 0 18px}</style>")


def icon_text(icono, html, ancho=18):
    """Fila icono + texto (las ventajas debajo del precio)."""
    return {"type": "group", "settings": {
        "content_direction": "row", "vertical_on_mobile": False, "horizontal_alignment": "flex-start",
        "vertical_alignment": "center", "gap": 12, "width": "fill"},
        "blocks": {
            "icono": {"type": "icon", "settings": {"icon": icono, "width": ancho, "icon_color": INK}, "blocks": {}},
            "texto": small(text_block(html, "paragraph"), "1rem"),
        }, "block_order": ["icono", "texto"]}


def icon_col(icono, html):  # (sin uso ahora; para una fila de iconos en columnas)
    """Columna icono encima de texto (la fila de tres promesas)."""
    return {"type": "group", "settings": {
        "content_direction": "column", "horizontal_alignment_flex_direction_column": "center",
        "gap": 8, "width": "fill"},
        "blocks": {
            "icono": {"type": "icon", "settings": {"icon": icono, "width": 22, "icon_color": INK}, "blocks": {}},
            "texto": small(text_block(html, "paragraph", "center")),
        }, "block_order": ["icono", "texto"]}


# Puntos dorados en las listas · sin selector de cantidad (como Calné; la cantidad se cambia en la cesta) ·
# (Shopify no deja usar `content` en el CSS personalizado: por eso ::marker y no ::before)
PRODUCT_CSS = (f"ul {{ padding-inline-start: 1.1em; }} ul li::marker {{ color: {GOLD}; }} "
               ".quantity-selector-wrapper { display: none; }")

migas = {
    "type": "section",
    "blocks": {"migas": text_block(
        '<p><a href="/">Inicio</a> › {{ closest.product.title }}</p>', "paragraph")},
    "block_order": ["migas"],
    "custom_css": [".text-block p { font-size: 0.75rem; letter-spacing: 0.04em; } "
                   ".text-block a { color: inherit; text-decoration: none; }"],
    "settings": {"content_direction": "column", "section_width": "page-width", "gap": 0,
                 "padding-block-start": 20, "padding-block-end": 0},
}

ficha = {
    "type": "product-information",
    "blocks": {
        "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
            "media_presentation": "carousel", "icons_style": "arrow",
            "slideshow_controls_style": "thumbnails", "slideshow_mobile_controls_style": "thumbnails",
            "thumbnail_position": "bottom", "thumbnail_width": 60, "thumbnail_radius": 0,
            "aspect_ratio": "1/1.25", "media_radius": 0, "extend_media": False,
            "zoom": True, "hide_variants": False}, "blocks": {}},
        "product-details": {"type": "_product-details", "static": True, "settings": {
            "gap": 20, "sticky_details_desktop": True,
            "padding-block-start": 8, "padding-block-end": 24},
            "blocks": {
                "titulo": {"type": "product-title", "settings": {
                    "type_preset": "custom", "font": "var(--font-heading--family)", "font_size": "1.5rem",
                    "case": "uppercase", "letter_spacing": "loose", "line_height": "tight",
                    "width": "100%"}, "blocks": {}},
                "precio": {"type": "price", "settings": {
                    "show_sale_price_first": True, "show_installments": False, "show_tax_info": False,
                    "type_preset": "custom", "font_size": "1.125rem", "width": "100%"}, "blocks": {}},
                "linea": {"type": "_divider", "settings": {"thickness": 1, "divider_color": C2,
                    "padding-block-start": 4, "padding-block-end": 4}, "blocks": {}},
                # Las líneas de Calné, en versión verdadera:
                #   «Limited stock» (escasez inventada)  → fecha límite real para Navidad (punto dorado)
                #   «100 % Waterproof & Everlasting»     → pila puesta + caja de regalo (no es sumergible)
                #   «Order before 23:59…»                → envío gratis con seguimiento
                #   «2-Year Warranty + 100-Days»         → 3 años (ley española) + 14 días
                "ventajas": {"type": "group", "settings": {
                    "content_direction": "column", "gap": 12, "width": "fill"},
                    "blocks": {
                        "navidad": NAVIDAD,
                        "regalo": REGALO,
                        "envio": icon_text("truck", "<p>Envío gratis a península, con seguimiento</p>"),
                        "garantia": icon_text("star", "<p>Garantía de 3 años + 14 días para devolverlo</p>"),
                    }, "block_order": ["navidad", "regalo", "envio", "garantia"]},
                "variantes": {"type": "variant-picker", "settings": {
                    "variant_style": "buttons", "show_swatches": True}, "blocks": {}},
                "comprar": {"type": "buy-buttons", "settings": {"stacking": True,
                    "show_pickup_availability": False, "gift_card_form": True},
                    "blocks": {
                        "quantity": {"type": "quantity", "static": True, "settings": {
                            "border_width": 1, "border_radius": 0}, "blocks": {}},
                        "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {
                            "style_class": "button"}, "blocks": {}},
                        "accelerated-checkout": {"type": "accelerated-checkout", "static": True,
                            "settings": {}, "blocks": {}},
                    }, "block_order": []},
                # Caja de oferta en verde con texto blanco, como Calné (Edu lo prefirió el 10-oct aunque la regla
                # de marca era «verde solo en lo que se pulsa»). Sin «solo hoy».
                # OJO: el descuento «2.º por 19,95 €» hay que crearlo en Descuentos antes de abrir la tienda.
                "oferta": {"type": "group", "settings": {
                    "content_direction": "column", "gap": 6, "width": "fill", "background_color": GREEN,
                    "padding-block-start": 18, "padding-block-end": 18,
                    "padding-inline-start": 20, "padding-inline-end": 20},
                    "blocks": {
                        "t": color(small(text_block("<p><strong>SEGUNDO RELOJ POR 19,95 €</strong></p>",
                                                    "paragraph"), "1.125rem"), "#FFFFFF", "100%"),
                        "p": color(text_block("<p>Añade dos a la cesta: el descuento se aplica solo al pagar. "
                                              "Uno para ti y otro para regalar.</p>", "paragraph"), "#FFFFFF", "100%"),
                    }, "block_order": ["t", "p"]},
                "detalles": {"type": "accordion", "settings": {
                    "icon": "plus", "dividers": True, "divider_color": C2, "type_preset": "h6"},
                    "blocks": {
                        "descripcion": {"type": "_accordion-row", "settings": {
                            "heading": "Descripción", "icon": "none", "open_by_default": False},
                            "blocks": {"texto": {"type": "product-description", "settings": {
                                "width": "100%", "type_preset": "rte"}, "blocks": {}}},
                            "block_order": ["texto"]},
                        "medida": row("Ajustar la correa",
                                      "<p>La correa mide 18 cm. Si tu muñeca es más fina (menos de 16 cm), quita "
                                      "uno o dos eslabones con el extractor que va en la caja: son 2 minutos.</p>"),
                        "agua": row("¿Se puede mojar?",
                                    "<p>No. No es sumergible: quítatelo para lavarte las manos, ducharte o nadar. "
                                    "Una gota de lluvia no le pasa nada.</p>"),
                        "envio": row("Envío", "<p>Gratis a península, con número de seguimiento por email. "
                                     "Plazo de entrega: [PLAZO] días laborables.</p>"
                                     "<p>Por ahora no enviamos a Canarias, Ceuta ni Melilla.</p>"),
                        "devoluciones": row("Devoluciones y garantía",
                                     "<p>Tienes 14 días desde que lo recibes para devolverlo: escríbenos "
                                     "y te explicamos cómo.</p><p>Las piezas personalizadas (con nombre o "
                                     "grabado) no admiten devolución porque se hacen solo para ti. Si llegan "
                                     "con un defecto o un error nuestro, las rehacemos.</p>"
                                     "<p>Todas tienen la garantía legal de 3 años.</p>"),
                        "cuidados": row("Cuidados",
                                     "<p>Ponte el perfume y la crema antes que la pieza, quítatela para hacer "
                                     "deporte y guárdala en su caja cuando no la lleves.</p>"),
                    },
                    "block_order": ["descripcion", "medida", "agua", "envio", "devoluciones", "cuidados"]},
            },
            "block_order": ["titulo", "precio", "linea", "ventajas", "variantes", "comprar", "oferta",
                            "detalles"]},
    },
    "block_order": [],
    "custom_css": [PRODUCT_CSS],
    "settings": {
        "content_width": "content-center-aligned", "desktop_media_position": "left",
        "equal_columns": False, "limit_details_width": True, "gap": 48,
        "enable_sticky_add_to_cart": True, "background_color": BG,
        "padding-block-start": 16, "padding-block-end": 48},
}

product = {
    "sections": {
        "migas": migas,
        "main": ficha,
        "recomendados": {
            "type": "product-recommendations",
            "blocks": {
                "titulo": text_block("<h2>También te puede gustar</h2>", "h4"),
                "static-product-card": {"type": "_product-card", "static": True,
                    "settings": {"product_card_gap": 6},
                    "blocks": {
                        "foto": {"type": "_product-card-gallery", "settings": {"image_ratio": "adapt"}, "blocks": {}},
                        "nombre": {"type": "product-title", "settings": {"type_preset": "rte"}, "blocks": {}},
                        "precio": {"type": "price", "settings": {"type_preset": "paragraph"}, "blocks": {}},
                    },
                    "block_order": ["foto", "nombre", "precio"]},
            },
            "block_order": ["titulo"],
            "settings": {
                "product": "{{ closest.product }}", "recommendation_type": "related", "layout_type": "grid",
                "max_products": 3, "columns": 3, "mobile_columns": "2", "columns_gap": 16, "rows_gap": 32,
                "section_width": "page-width", "gap": 28, "background_color": BG,
                "padding-block-start": 48, "padding-block-end": 64},
        },
    },
    "order": ["migas", "main", "recomendados"],
}
(OUT / "product.json").write_text(json.dumps(product, ensure_ascii=False, indent=2), encoding="utf8")

(OUT / "codigo" / "snippets").mkdir(parents=True, exist_ok=True)
(OUT / "codigo" / "snippets" / "lunerie-bolitas.liquid").write_text(
    "{%- comment -%} Generado por tema/build.py (BOLITAS): bolitas de color en el selector de variantes {%- endcomment -%}\n"
    "<style>" + SWATCH_CSS + "</style>\n", encoding="utf8")

# ---------- Carrito: aviso «Añade un segundo reloj por 19,95 €» ----------
# Sale cuando hay un número impar de relojes Lune en la cesta (el descuento automático va por parejas).
# Un botón por color (con su bolita); al pulsar se añade y se va a /cart, donde ya aparece el descuento.
OFERTA_PRODUCTO, OFERTA_PRECIO = "reloj-lune", "19,95&nbsp;€"
_bolita = "".join(f"{{%- if v.title contains '{n}' -%}}{{%- assign c = '{col}' -%}}{{%- endif -%}}"
                  for n, col in BOLITAS.items())
UPSELL = (
    "{%- comment -%} Generado por tema/build.py: aviso del segundo reloj en la cesta {%- endcomment -%}\n"
    "{%- assign lu_qty = 0 -%}{%- assign lu_prod = nil -%}"
    "{%- for item in cart.items -%}{%- if item.product.handle == '" + OFERTA_PRODUCTO + "' -%}"
    "{%- assign lu_qty = lu_qty | plus: item.quantity -%}{%- assign lu_prod = item.product -%}"
    "{%- endif -%}{%- endfor -%}"
    "{%- assign lu_resto = lu_qty | modulo: 2 -%}\n"
    "{%- if lu_resto == 1 and lu_prod -%}\n"
    '<div class="lu-upsell">\n'
    '  <p class="lu-upsell__t">Añade un segundo reloj por ' + OFERTA_PRECIO + "</p>\n"
    '  <p class="lu-upsell__p">Uno para ti y otro para regalar. Elige el color:</p>\n'
    "  {%- for v in lu_prod.variants -%}{%- if v.available -%}{%- assign c = '" + LINE + "' -%}" + _bolita + "\n"
    '  <form class="lu-upsell__fila" action="{{ routes.cart_add_url }}" method="post">\n'
    '    <input type="hidden" name="id" value="{{ v.id }}">'
    '<input type="hidden" name="quantity" value="1">'
    '<input type="hidden" name="return_to" value="{{ routes.cart_url }}">\n'
    '    <span class="lu-upsell__bolita" style="background: {{ c }}"></span>'
    '<span class="lu-upsell__color">{{ v.title }}</span>\n'
    '    <button type="submit" class="lu-upsell__btn">Añadir · ' + OFERTA_PRECIO + "</button>\n"
    "  </form>\n"
    "  {%- endif -%}{%- endfor -%}\n"
    "</div>\n"
    "<style>"
    ".lu-upsell{margin:12px 0;padding:16px 18px;background:" + GREEN + ";color:#fff;display:grid;gap:10px}"
    ".lu-upsell p{margin:0}"
    ".lu-upsell__t{font-weight:500;font-size:1.0625rem;letter-spacing:.02em;text-transform:uppercase}"
    ".lu-upsell__p{font-size:.875rem;opacity:.9}"
    ".lu-upsell__fila{display:flex;align-items:center;gap:10px;margin:0;padding-top:10px;"
    "border-top:1px solid rgba(255,255,255,.2)}"
    ".lu-upsell__bolita{flex:0 0 22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 2px #fff;"
    "border:1px solid rgba(255,255,255,.6)}"
    ".lu-upsell__color{flex:1;font-size:.875rem}"
    ".lu-upsell__btn{appearance:none;border:0;background:#fff;color:" + GREEN + ";font:inherit;font-size:.75rem;"
    "letter-spacing:.12em;text-transform:uppercase;padding:10px 14px;cursor:pointer;white-space:nowrap}"
    ".lu-upsell__btn:focus-visible{outline:2px solid #fff;outline-offset:2px}"
    "</style>\n"
    # Añadir con fetch (como el resto del tema) y luego ir a la cesta; sin JS, el formulario normal hace lo mismo
    "<script>document.addEventListener('submit',function(e){"
    "var f=e.target.closest&&e.target.closest('.lu-upsell__fila');if(!f)return;"
    "e.preventDefault();f.querySelector('button').disabled=true;"
    "fetch('{{ routes.cart_add_url }}.js',{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})"
    ".then(function(){location.href='{{ routes.cart_url }}'}).catch(function(){f.submit()})});</script>\n"
    "{%- endif -%}\n")
(OUT / "codigo" / "snippets" / "lunerie-segundo-reloj.liquid").write_text(UPSELL, encoding="utf8")

# Copia en tema/tienda/ (el tema publicado bajado con `shopify theme pull`, fuera de git) para subirlo con la CLI
TIENDA = OUT / "tienda"
# password.json y cart.json no los genera build.py: son plantillas del tema con los textos en español
DESTINO = {"password.json": "templates", "cart.json": "templates", "settings_data.json": "config", "header-group.json": "sections", "footer-group.json": "sections",
           "index.json": "templates", "product.json": "templates"}
if TIENDA.exists():
    # código del tema modificado (tema/codigo/<carpeta>/<fichero>), p. ej. snippets/variant-main-picker.liquid
    for f in (OUT / "codigo").rglob("*.liquid"):
        (TIENDA / f.relative_to(OUT / "codigo")).write_text(f.read_text(encoding="utf8"), encoding="utf8")
    for nombre, carpeta in DESTINO.items():
        (TIENDA / carpeta / nombre).write_text((OUT / nombre).read_text(encoding="utf8"), encoding="utf8")
print("ok")
