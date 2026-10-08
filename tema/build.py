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


# ---------- Inicio: portada sin foto (fondo niebla) · las piezas · tres promesas ----------
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
    "order": ["portada", "piezas", "promesas"],
}
(OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf8")


# ---------- Ficha de producto (como la maqueta de la página de marca) ----------
def row(heading, html):
    return {"type": "_accordion-row", "settings": {"heading": heading, "icon": "none"},
            "blocks": {"texto": text_block(html, "rte")}, "block_order": ["texto"]}


# Puntos dorados en las listas de la ficha (garantías y descripción)
# (Shopify no deja usar `content` en el CSS personalizado: por eso ::marker y no ::before)
PRODUCT_CSS = f"ul {{ padding-inline-start: 1.1em; }} ul li::marker {{ color: {GOLD}; }}"

product = {
    "sections": {
        "main": {
            "type": "product-information",
            "blocks": {
                "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
                    "media_presentation": "carousel", "icons_style": "arrow",
                    "slideshow_controls_style": "thumbnails", "slideshow_mobile_controls_style": "dots",
                    "thumbnail_position": "bottom", "thumbnail_width": 56, "thumbnail_radius": 0,
                    "aspect_ratio": "1/1.25", "media_radius": 0, "extend_media": False,
                    "zoom": True, "hide_variants": True}, "blocks": {}},
                "product-details": {"type": "_product-details", "static": True, "settings": {
                    "gap": 24, "sticky_details_desktop": True,
                    "padding-block-start": 24, "padding-block-end": 24},
                    "blocks": {
                        "cabecera": group({
                            "titulo": text_block("<h1>{{ closest.product.title }}</h1>", "h2"),
                            "precio": {"type": "price", "settings": {
                                "show_sale_price_first": True, "show_installments": False,
                                "show_tax_info": False, "type_preset": "paragraph"}, "blocks": {}},
                        }, align="flex-start", gap=10),
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
                        "garantias": text_block(
                            "<ul><li>Envío gratis a península, con seguimiento</li>"
                            "<li>Devolución en 14 días · garantía legal de 3 años</li>"
                            "<li>Pago con tarjeta, Apple Pay o Google Pay</li></ul>", "rte"),
                        "descripcion": text_block("{{ closest.product.description }}", "rte"),
                        "detalles": {"type": "accordion", "settings": {
                            "icon": "plus", "dividers": True, "divider_color": C2, "type_preset": "h6"},
                            "blocks": {
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
                                             "<p>Quítatelo para lavarte las manos, ducharte, nadar o hacer deporte. "
                                             "Ponte el perfume y la crema antes que la pieza, y guárdala en su caja "
                                             "cuando no la lleves.</p>"),
                            },
                            "block_order": ["envio", "devoluciones", "cuidados"]},
                    },
                    "block_order": ["cabecera", "variantes", "comprar", "garantias", "descripcion", "detalles"]},
            },
            "block_order": [],
            "custom_css": [PRODUCT_CSS],
            "settings": {
                "content_width": "content-center-aligned", "desktop_media_position": "left",
                "equal_columns": True, "limit_details_width": True, "gap": 48,
                "enable_sticky_add_to_cart": True, "background_color": BG,
                "padding-block-start": 24, "padding-block-end": 48},
        },
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
    "order": ["main", "recomendados"],
}
(OUT / "product.json").write_text(json.dumps(product, ensure_ascii=False, indent=2), encoding="utf8")

# Copia en tema/tienda/ (el tema publicado bajado con `shopify theme pull`, fuera de git) para subirlo con la CLI
TIENDA = OUT / "tienda"
DESTINO = {"settings_data.json": "config", "header-group.json": "sections", "footer-group.json": "sections",
           "index.json": "templates", "product.json": "templates"}
if TIENDA.exists():
    for nombre, carpeta in DESTINO.items():
        (TIENDA / carpeta / nombre).write_text((OUT / nombre).read_text(encoding="utf8"), encoding="utf8")
print("ok")
