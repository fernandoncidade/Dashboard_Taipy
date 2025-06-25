import pandas as pd
import locale
from babel.numbers import format_currency

TRANSLATIONS = {
    "pt-BR": {
        "title": "Dashboard de Vendas",
        "header": "Dashboard de Desempenho de Vendas",
        "warning": "⚠️ **Aviso**: Dados não disponíveis. Verifique o caminho do arquivo CSV.",
        "filter_from": "Filtrar De:",
        "filter_to": "Até:",
        "filter_category": "Filtrar por Categoria:",
        "key_metrics": "Métricas Principais",
        "total_revenue": "Receita Total",
        "total_orders": "Total de Pedidos",
        "avg_order_value": "Valor Médio do Pedido",
        "top_category": "Categoria Principal",
        "visualizations": "Visualizações",
        "revenue_over_time": "Receita ao Longo do Tempo",
        "revenue_by_category": "Receita por Categoria",
        "top_products": "Melhores Produtos",
        "all_categories": "Todas as Categorias",
        "raw_data": "Dados Brutos",
        "language": "Idioma",
        "columns": {
            "order_id": "ID do Pedido",
            "order_date": "Data do Pedido",
            "customer_id": "ID do Cliente",
            "customer_name": "Nome do Cliente",
            "product_id": "ID do Produto",
            "product_names": "Nome do Produto",
            "categories": "Categorias",
            "quantity": "Quantidade",
            "price": "Preço",
            "revenue": "Receita"
        },
        "axes": {
            "order_date": "Data do Pedido",
            "revenue": "Receita (R$)",
            "categories": "Categorias",
            "product_names": "Produtos"
        }
    },
    "en-US": {
        "title": "Sales Dashboard",
        "header": "Sales Performance Dashboard",
        "warning": "⚠️ **Warning**: No data available. Please check the CSV file path.",
        "filter_from": "Filter From:",
        "filter_to": "To:",
        "filter_category": "Filter by Category:",
        "key_metrics": "Key Metrics",
        "total_revenue": "Total Revenue",
        "total_orders": "Total Orders",
        "avg_order_value": "Average Order Value",
        "top_category": "Top Category",
        "visualizations": "Visualizations",
        "revenue_over_time": "Revenue Over Time",
        "revenue_by_category": "Revenue by Category",
        "top_products": "Top Products",
        "all_categories": "All Categories",
        "raw_data": "Raw Data",
        "language": "Language",
        "columns": {
            "order_id": "Order ID",
            "order_date": "Order Date",
            "customer_id": "Customer ID",
            "customer_name": "Customer Name",
            "product_id": "Product ID",
            "product_names": "Product Name",
            "categories": "Categories",
            "quantity": "Quantity",
            "price": "Price",
            "revenue": "Revenue"
        },
        "axes": {
            "order_date": "Order Date",
            "revenue": "Revenue ($)",
            "categories": "Categories",
            "product_names": "Products"
        }
    },
    "es-ES": {
        "title": "Tablero de Ventas",
        "header": "Tablero de Rendimiento de Ventas",
        "warning": "⚠️ **Advertencia**: No hay datos disponibles. Compruebe la ruta del archivo CSV.",
        "filter_from": "Filtrar Desde:",
        "filter_to": "Hasta:",
        "filter_category": "Filtrar por Categoría:",
        "key_metrics": "Métricas Clave",
        "total_revenue": "Ingreso Total",
        "total_orders": "Total de Pedidos",
        "avg_order_value": "Valor Promedio del Pedido",
        "top_category": "Categoría Principal",
        "visualizations": "Visualizaciones",
        "revenue_over_time": "Ingresos a lo Largo del Tiempo",
        "revenue_by_category": "Ingresos por Categoría",
        "top_products": "Mejores Productos",
        "all_categories": "Todas las Categorías",
        "raw_data": "Datos Brutos",
        "language": "Idioma",
        "columns": {
            "order_id": "ID del Pedido",
            "order_date": "Fecha del Pedido",
            "customer_id": "ID del Cliente",
            "customer_name": "Nombre del Cliente",
            "product_id": "ID del Producto",
            "product_names": "Nombre del Producto",
            "categories": "Categorías",
            "quantity": "Cantidad",
            "price": "Precio",
            "revenue": "Ingresos"
        },
        "axes": {
            "order_date": "Fecha del Pedido",
            "revenue": "Ingresos (€)",
            "categories": "Categorías",
            "product_names": "Productos"
        }
    },
    "fr-FR": {
        "title": "Tableau de Bord des Ventes",
        "header": "Tableau de Bord de Performance des Ventes",
        "warning": "⚠️ **Avertissement**: Aucune donnée disponible. Veuillez vérifier le chemin du fichier CSV.",
        "filter_from": "Filtrer De:",
        "filter_to": "À:",
        "filter_category": "Filtrer par Catégorie:",
        "key_metrics": "Indicateurs Clés",
        "total_revenue": "Revenu Total",
        "total_orders": "Total des Commandes",
        "avg_order_value": "Valeur Moyenne des Commandes",
        "top_category": "Meilleure Catégorie",
        "visualizations": "Visualisations",
        "revenue_over_time": "Revenus au Fil du Temps",
        "revenue_by_category": "Revenus par Catégorie",
        "top_products": "Meilleurs Produits",
        "all_categories": "Toutes les Catégories",
        "raw_data": "Données Brutes",
        "language": "Langue",
        "columns": {
            "order_id": "ID de Commande",
            "order_date": "Date de Commande",
            "customer_id": "ID Client",
            "customer_name": "Nom du Client",
            "product_id": "ID Produit",
            "product_names": "Nom du Produit",
            "categories": "Catégories",
            "quantity": "Quantité",
            "price": "Prix",
            "revenue": "Revenu"
        },
        "axes": {
            "order_date": "Date de Commande",
            "revenue": "Revenu (€)",
            "categories": "Catégories",
            "product_names": "Produits"
        }
    },
    "it-IT": {
        "title": "Dashboard delle Vendite",
        "header": "Dashboard delle Performance di Vendita",
        "warning": "⚠️ **Avviso**: Nessun dato disponibile. Controllare il percorso del file CSV.",
        "filter_from": "Filtra Da:",
        "filter_to": "A:",
        "filter_category": "Filtra per Categoria:",
        "key_metrics": "Metriche Chiave",
        "total_revenue": "Ricavi Totali",
        "total_orders": "Totale Ordini",
        "avg_order_value": "Valore Medio dell'Ordine",
        "top_category": "Categoria Principale",
        "visualizations": "Visualizzazioni",
        "revenue_over_time": "Ricavi nel Tempo",
        "revenue_by_category": "Ricavi per Categoria",
        "top_products": "Migliori Prodotti",
        "all_categories": "Tutte le Categorie",
        "raw_data": "Dati Grezzi",
        "language": "Lingua",
        "columns": {
            "order_id": "ID Ordine",
            "order_date": "Data Ordine",
            "customer_id": "ID Cliente",
            "customer_name": "Nome Cliente",
            "product_id": "ID Prodotto",
            "product_names": "Nome Prodotto",
            "categories": "Categorie",
            "quantity": "Quantità",
            "price": "Prezzo",
            "revenue": "Ricavi"
        },
        "axes": {
            "order_date": "Data Ordine",
            "revenue": "Ricavi (€)",
            "categories": "Categorie",
            "product_names": "Prodotti"
        }
    },
    "de-DE": {
        "title": "Verkaufs-Dashboard",
        "header": "Verkaufsleistungs-Dashboard",
        "warning": "⚠️ **Warnung**: Keine Daten verfügbar. Bitte überprüfen Sie den CSV-Dateipfad.",
        "filter_from": "Filtern Von:",
        "filter_to": "Bis:",
        "filter_category": "Nach Kategorie filtern:",
        "key_metrics": "Schlüsselkennzahlen",
        "total_revenue": "Gesamtumsatz",
        "total_orders": "Gesamtbestellungen",
        "avg_order_value": "Durchschnittlicher Bestellwert",
        "top_category": "Wichtigste Kategorie",
        "visualizations": "Visualisierungen",
        "revenue_over_time": "Umsatz im Zeitverlauf",
        "revenue_by_category": "Umsatz nach Kategorie",
        "top_products": "Beste Produkte",
        "all_categories": "Alle Kategorien",
        "raw_data": "Rohdaten",
        "language": "Sprache",
        "columns": {
            "order_id": "Bestell-ID",
            "order_date": "Bestelldatum",
            "customer_id": "Kunden-ID",
            "customer_name": "Kundenname",
            "product_id": "Produkt-ID",
            "product_names": "Produktname",
            "categories": "Kategorien",
            "quantity": "Menge",
            "price": "Preis",
            "revenue": "Umsatz"
        },
        "axes": {
            "order_date": "Bestelldatum",
            "revenue": "Umsatz (€)",
            "categories": "Kategorien",
            "product_names": "Produkte"
        }
    },
}

COLUMN_MAPPINGS = {
    "pt-BR": {
        "order_id": ["id_pedido", "order_id"],
        "order_date": ["data_pedido", "order_date"],
        "customer_id": ["id_cliente", "customer_id"],
        "customer_name": ["nome_cliente", "customer_name"],
        "product_id": ["id_produto", "product_id"],
        "product_names": ["nomes_produtos", "product_names"],
        "categories": ["categorias", "categories"],
        "quantity": ["quantidade", "quantity"],
        "price": ["preco", "price"],
        "revenue": ["receita", "revenue"],
    },
    "en-US": {
        "order_id": ["order_id"],
        "order_date": ["order_date"],
        "customer_id": ["customer_id"],
        "customer_name": ["customer_name"],
        "product_id": ["product_id"],
        "product_names": ["product_names"],
        "categories": ["categories"],
        "quantity": ["quantity"],
        "price": ["price"],
        "revenue": ["revenue"],
    },
    "es-ES": {
        "order_id": ["id_pedido", "order_id"],
        "order_date": ["fecha_pedido", "order_date"],
        "customer_id": ["id_cliente", "customer_id"],
        "customer_name": ["nombre_cliente", "customer_name"],
        "product_id": ["id_producto", "product_id"],
        "product_names": ["nombres_productos", "product_names"],
        "categories": ["categorias", "categories"],
        "quantity": ["cantidad", "quantity"],
        "price": ["precio", "price"],
        "revenue": ["ingresos", "revenue"],
    },
    "fr-FR": {
        "order_id": ["id_commande", "order_id"],
        "order_date": ["date_commande", "order_date"],
        "customer_id": ["id_client", "customer_id"],
        "customer_name": ["nom_client", "customer_name"],
        "product_id": ["id_produit", "product_id"],
        "product_names": ["noms_produits", "product_names"],
        "categories": ["categories", "categories"],
        "quantity": ["quantite", "quantity"],
        "price": ["prix", "price"],
        "revenue": ["revenu", "revenue"],
    },
    "it-IT": {
        "order_id": ["id_ordine", "order_id"],
        "order_date": ["data_ordine", "order_date"],
        "customer_id": ["id_cliente", "customer_id"],
        "customer_name": ["nome_cliente", "customer_name"],
        "product_id": ["id_prodotto", "product_id"],
        "product_names": ["nomi_prodotti", "product_names"],
        "categories": ["categorie", "categories"],
        "quantity": ["quantita", "quantity"],
        "price": ["prezzo", "price"],
        "revenue": ["ricavo", "revenue"],
    },
    "de-DE": {
        "order_id": ["bestellung_id", "order_id"],
        "order_date": ["bestelldatum", "order_date"],
        "customer_id": ["kunde_id", "customer_id"],
        "customer_name": ["kundenname", "customer_name"],
        "product_id": ["produkt_id", "product_id"],
        "product_names": ["produktnamen", "product_names"],
        "categories": ["kategorien", "categories"],
        "quantity": ["menge", "quantity"],
        "price": ["preis", "price"],
        "revenue": ["umsatz", "revenue"],
    },
}

SUPPORTED_LANGUAGES = ["pt-BR", "en-US", "es-ES", "fr-FR", "it-IT", "de-DE"]
LANGUAGE_NAMES = {
    "pt-BR": "Português (Brasil)",
    "en-US": "English (US)",
    "es-ES": "Español",
    "fr-FR": "Français",
    "it-IT": "Italiano",
    "de-DE": "Deutsch"
}

ALL_CATEGORIES_VALUES = ["Todas as Categorias", "All Categories", "Todas las Categorías", 
                         "Toutes les Catégories", "Tutte le Categorie", "Alle Kategorien"]

def translate_column(column_name, lang):
    if lang in TRANSLATIONS and "columns" in TRANSLATIONS[lang] and column_name in TRANSLATIONS[lang]["columns"]:
        return TRANSLATIONS[lang]["columns"][column_name]

    if "columns" in TRANSLATIONS["en-US"] and column_name in TRANSLATIONS["en-US"]["columns"]:
        return TRANSLATIONS["en-US"]["columns"][column_name]

    return column_name

def translate_axis(axis_name, lang):
    if lang in TRANSLATIONS and "axes" in TRANSLATIONS[lang] and axis_name in TRANSLATIONS[lang]["axes"]:
        return TRANSLATIONS[lang]["axes"][axis_name]

    if "axes" in TRANSLATIONS["en-US"] and axis_name in TRANSLATIONS["en-US"]["axes"]:
        return TRANSLATIONS["en-US"]["axes"][axis_name]

    return axis_name

def translate_dataframe_columns(df, lang):
    if df.empty:
        return df

    translated_columns = {}
    for col in df.columns:
        translated_columns[col] = translate_column(col, lang)

    df_copy = df.copy()
    df_copy.columns = [translated_columns.get(col, col) for col in df.columns]
    return df_copy

def translate(key, lang):
    if lang in TRANSLATIONS and key in TRANSLATIONS[lang]:
        return TRANSLATIONS[lang][key]

    if key in TRANSLATIONS["en-US"]:
        return TRANSLATIONS["en-US"][key]

    return key

def detect_csv_language(columns):
    for lang in SUPPORTED_LANGUAGES:
        matches = 0
        required_matches = 3

        for std_col, possible_names in COLUMN_MAPPINGS[lang].items():
            if any(name in columns for name in possible_names):
                matches += 1

        if matches >= required_matches:
            print(f"Detected CSV language: {lang}")
            return lang

    print("Could not detect CSV language, defaulting to English")
    return "en-US"

def map_columns_to_standard(df, detected_lang):
    column_map = {}

    for std_col, possible_names in COLUMN_MAPPINGS[detected_lang].items():
        for name in possible_names:
            if name in df.columns:
                column_map[name] = std_col
                break

    if column_map:
        df = df.rename(columns=column_map)

    return df

def is_all_categories(category):
    return (category in ALL_CATEGORIES_VALUES or
            category in [translate("all_categories", lang) for lang in SUPPORTED_LANGUAGES])

CURRENCY_SYMBOLS = {
    "pt-BR": "R$",
    "en-US": "$",
    "es-ES": "€",
    "fr-FR": "€",
    "it-IT": "€",
    "de-DE": "€"
}

CURRENCY_LOCALES = {
    "pt-BR": "pt_BR",
    "en-US": "en_US",
    "es-ES": "es_ES",
    "fr-FR": "fr_FR",
    "it-IT": "it_IT",
    "de-DE": "de_DE"
}

def format_axis_value(value, axis_name, lang):
    if axis_name == "revenue" and isinstance(value, (int, float)):
        currency_symbol = CURRENCY_SYMBOLS.get(lang, "$")
        try:
            locale_str = CURRENCY_LOCALES.get(lang, "en_US")
            return format_currency(value, currency_symbol, locale=locale_str)

        except:
            return f"{currency_symbol}{value:,.2f}"

    if axis_name == "order_date" and hasattr(value, "strftime"):
        date_formats = {
            "pt-BR": "%d/%m/%Y",
            "en-US": "%m/%d/%Y",
            "es-ES": "%d/%m/%Y",
            "fr-FR": "%d/%m/%Y",
            "it-IT": "%d/%m/%Y",
            "de-DE": "%d.%m.%Y"
        }
        date_format = date_formats.get(lang, "%Y-%m-%d")
        return value.strftime(date_format)

    return value

def get_chart_options(lang):
    currency_symbol = CURRENCY_SYMBOLS.get(lang, "$")

    return {
        "revenue": {
            "format": f"{{value}} {currency_symbol}",
            "locale": CURRENCY_LOCALES.get(lang, "en_US")
        },
        "date": {
            "locale": CURRENCY_LOCALES.get(lang, "en_US").replace("_", "-")
        }
    }
