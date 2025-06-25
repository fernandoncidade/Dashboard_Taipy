from taipy.gui import Gui, navigate
import pandas as pd
import datetime
import os
import taipy.gui.builder as tgb

from translations import (
    TRANSLATIONS, COLUMN_MAPPINGS, SUPPORTED_LANGUAGES, LANGUAGE_NAMES, 
    ALL_CATEGORIES_VALUES, translate, translate_column, translate_axis, 
    translate_dataframe_columns, detect_csv_language, map_columns_to_standard,
    is_all_categories, format_axis_value, get_chart_options,
    CURRENCY_SYMBOLS, CURRENCY_LOCALES, format_currency
)

csv_file_path = r"C:\Users\ferna\WORK\Projetos_Python\Dashboard_Taipy\dados_vendas.csv"

selected_language = "pt-BR"
chart_options = []
selected_category = ""
selected_tab = ""
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2023, 12, 31)
raw_data = pd.DataFrame()
categories = ["All Categories"]
revenue_data = pd.DataFrame(columns=["order_date", "revenue"])
category_data = pd.DataFrame(columns=["categories", "revenue"])
top_products_data = pd.DataFrame(columns=["product_names", "revenue"])
total_revenue = "$0.00"
total_orders = 0
avg_order_value = "$0.00"
top_category = "N/A"
translated_raw_data = pd.DataFrame()
time_chart_options = "{}"
category_chart_options = "{}"
product_chart_options = "{}"

x_label_date = ""
y_label_revenue = ""
x_label_categories = ""
x_label_products = ""

def load_data(state):
    try:
        header_df = pd.read_csv(csv_file_path, nrows=0)
        detected_lang = detect_csv_language(header_df.columns)

        df = pd.read_csv(csv_file_path, low_memory=False)

        df = map_columns_to_standard(df, detected_lang)

        if "order_date" in df.columns:
            df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

        print(f"Data loaded successfully: {df.shape[0]} rows")

        all_categories_text = translate("all_categories", state.selected_language)
        state.categories = [all_categories_text] + (df["categories"].dropna().unique().tolist() if "categories" in df.columns else [])

        if "order_date" in df.columns and not df.empty:
            state.start_date = df["order_date"].min().date()
            state.end_date = df["order_date"].max().date()

        return df

    except Exception as e:
        print(f"Error loading CSV: {e}")
        print("Creating empty DataFrame with sample structure...")

        empty_df = pd.DataFrame(columns=[
            "order_id", "order_date", "categories", "product_names", 
            "quantity", "price", "revenue"
        ])

        all_categories_text = translate("all_categories", state.selected_language)
        state.categories = [all_categories_text]
        state.start_date = datetime.date(2020, 1, 1)
        state.end_date = datetime.date(2023, 12, 31)

        return empty_df

def update_translations(state):
    state.chart_options = [
        translate("revenue_over_time", state.selected_language),
        translate("revenue_by_category", state.selected_language),
        translate("top_products", state.selected_language),
    ]

    if not state.selected_tab or state.selected_tab not in state.chart_options:
        state.selected_tab = state.chart_options[0]

    all_categories_text = translate("all_categories", state.selected_language)
    if state.selected_category == "" or is_all_categories(state.selected_category):
        state.selected_category = all_categories_text

    if state.categories and is_all_categories(state.categories[0]):
        state.categories[0] = all_categories_text

    state.x_label_date = translate_axis("order_date", state.selected_language)
    state.y_label_revenue = translate_axis("revenue", state.selected_language)
    state.x_label_categories = translate_axis("categories", state.selected_language)
    state.x_label_products = translate_axis("product_names", state.selected_language)

def apply_changes(state):
    if state.raw_data.empty:
        state.revenue_data = pd.DataFrame(columns=["order_date", "revenue"])
        state.category_data = pd.DataFrame(columns=["categories", "revenue"])
        state.top_products_data = pd.DataFrame(columns=["product_names", "revenue"])
        state.total_revenue = "$0.00"
        state.total_orders = 0
        state.avg_order_value = "$0.00"
        state.top_category = "N/A"

        state.translated_raw_data = pd.DataFrame()
        return

    filtered_data = state.raw_data[
        (state.raw_data["order_date"] >= pd.to_datetime(state.start_date)) &
        (state.raw_data["order_date"] <= pd.to_datetime(state.end_date))
    ]

    if not is_all_categories(state.selected_category):
        filtered_data = filtered_data[filtered_data["categories"] == state.selected_category]

    state.revenue_data = filtered_data.groupby(pd.Grouper(key="order_date", freq="ME"))["revenue"].sum().reset_index()
    state.revenue_data.columns = ["order_date", "revenue"]

    state.category_data = filtered_data.groupby("categories")["revenue"].sum().reset_index()
    state.category_data.columns = ["categories", "revenue"]
    state.category_data = state.category_data.sort_values("revenue", ascending=False)

    state.top_products_data = (
        filtered_data.groupby("product_names")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state.top_products_data.columns = ["product_names", "revenue"]

    if not filtered_data.empty:
        currency_symbol = CURRENCY_SYMBOLS.get(state.selected_language, "$")
        revenue_value = filtered_data['revenue'].sum()

        try:
            locale_str = CURRENCY_LOCALES.get(state.selected_language, "en_US")
            state.total_revenue = format_currency(revenue_value, currency_symbol, locale=locale_str)

        except:
            state.total_revenue = f"{currency_symbol}{revenue_value:,.2f}"

        avg_value = filtered_data['revenue'].sum() / max(filtered_data['order_id'].nunique(), 1)

        try:
            state.avg_order_value = format_currency(avg_value, currency_symbol, locale=locale_str)

        except:
            state.avg_order_value = f"{currency_symbol}{avg_value:,.2f}"

    state.total_orders = filtered_data["order_id"].nunique()

    if not filtered_data.empty and "categories" in filtered_data.columns and not filtered_data["categories"].empty:
        try:
            state.top_category = filtered_data.groupby("categories")["revenue"].sum().idxmax()

        except:
            state.top_category = "N/A"

    else:
        state.top_category = "N/A"

    state.translated_raw_data = translate_dataframe_columns(state.raw_data, state.selected_language)

def on_init(state):
    state.raw_data = load_data(state)
    update_translations(state)

    state.time_chart_options = create_chart_options(state, "time", "order_date", "revenue")
    state.category_chart_options = create_chart_options(state, "bar", "categories", "revenue")
    state.product_chart_options = create_chart_options(state, "bar", "product_names", "revenue")

    try:
        apply_changes(state)

    except AttributeError as e:
        print(f"Aviso durante inicialização: {e}")
        pass

def on_change(state, var_name, var_value):
    if var_name == "selected_language":
        update_translations(state)
        state.time_chart_options = create_chart_options(state, "time", "order_date", "revenue")
        state.category_chart_options = create_chart_options(state, "bar", "categories", "revenue")
        state.product_chart_options = create_chart_options(state, "bar", "product_names", "revenue")
        apply_changes(state)
        navigate(state, to="", force=True)

    elif var_name in {"start_date", "end_date", "selected_category", "selected_tab"}:
        apply_changes(state)

def get_partial_visibility(tab_name, selected_tab):
    return "block" if tab_name == selected_tab else "none"

def create_chart_options(state, chart_type, x_axis_name=None, y_axis_name=None):
    if chart_type == "time":
        options = {
            "xAxis": {
                "type": "time",
                "locale": get_chart_options(state.selected_language)["date"]["locale"]
            },
            "yAxis": {
                "axisLabel": {
                    "formatter": "{value} " + CURRENCY_SYMBOLS.get(state.selected_language, "$")
                }
            }
        }

    elif chart_type == "bar":
        options = {
            "yAxis": {
                "axisLabel": {
                    "formatter": "{value} " + CURRENCY_SYMBOLS.get(state.selected_language, "$")
                }
            }
        }

    else:
        options = {}

    if x_axis_name:
        options.setdefault("xAxis", {})
        options["xAxis"]["name"] = translate_axis(x_axis_name, state.selected_language)

    if y_axis_name:
        options.setdefault("yAxis", {})
        options["yAxis"]["name"] = translate_axis(y_axis_name, state.selected_language)

    return options

with tgb.Page() as page:
    with tgb.part(class_name="language-selector"):
        with tgb.layout(columns="1 5"):
            tgb.text("{translate('language', selected_language)}:")
            tgb.selector(
                value="{selected_language}",
                lov=list(LANGUAGE_NAMES.keys()),
                lov_labels=[LANGUAGE_NAMES[lang] for lang in LANGUAGE_NAMES],
                dropdown=True,
                width="200px"
            )

    tgb.text("# {translate('header', selected_language)}", mode="md")

    with tgb.part(render="{len(raw_data) == 0}"):
        tgb.text("{translate('warning', selected_language)}", mode="md", class_name="alert-warning")

    with tgb.part(class_name="card filter-card"):
        with tgb.layout(columns="1 1 2"):
            with tgb.part():
                tgb.text("{translate('filter_from', selected_language)}")
                tgb.date("{start_date}")

            with tgb.part():
                tgb.text("{translate('filter_to', selected_language)}")
                tgb.date("{end_date}")

            with tgb.part():
                tgb.text("{translate('filter_category', selected_language)}")
                tgb.selector(
                    value="{selected_category}",
                    lov="{categories}",
                    dropdown=True,
                    width="300px"
                )

    tgb.text("## {translate('key_metrics', selected_language)}", mode="md")
    with tgb.layout(columns="1 1 1 1"):
        with tgb.part(class_name="metric-card"):
            tgb.text("### {translate('total_revenue', selected_language)}", mode="md")
            tgb.text("{total_revenue}", class_name="metric-value")

        with tgb.part(class_name="metric-card"):
            tgb.text("### {translate('total_orders', selected_language)}", mode="md")
            tgb.text("{total_orders}", class_name="metric-value")

        with tgb.part(class_name="metric-card"):
            tgb.text("### {translate('avg_order_value', selected_language)}", mode="md")
            tgb.text("{avg_order_value}", class_name="metric-value")

        with tgb.part(class_name="metric-card"):
            tgb.text("### {translate('top_category', selected_language)}", mode="md")
            tgb.text("{top_category}", class_name="metric-value")

    tgb.text("## {translate('visualizations', selected_language)}", mode="md")
    with tgb.part(style="width: 50%; margin-bottom: 20px;"):
        tgb.selector(
            value="{selected_tab}",
            lov="{chart_options}",
            dropdown=True,
            width="360px",
        )

    with tgb.part(render="{selected_tab == translate('revenue_over_time', selected_language)}"):
        tgb.chart(
            data="{revenue_data}",
            x="order_date",
            y="revenue",
            type="line",
            title="{translate('revenue_over_time', selected_language)}",
            x_label="{x_label_date}",
            y_label="{y_label_revenue}",
            options="{time_chart_options}"
        )

    with tgb.part(render="{selected_tab == translate('revenue_by_category', selected_language)}"):
        tgb.chart(
            data="{category_data}",
            x="categories",
            y="revenue",
            type="bar",
            title="{translate('revenue_by_category', selected_language)}",
            x_label="{x_label_categories}",
            y_label="{y_label_revenue}",
            options="{category_chart_options}"
        )

    with tgb.part(render="{selected_tab == translate('top_products', selected_language)}"):
        tgb.chart(
            data="{top_products_data}",
            x="product_names",
            y="revenue",
            type="bar",
            title="{translate('top_products', selected_language)}",
            x_label="{x_label_products}",
            y_label="{y_label_revenue}",
            options="{product_chart_options}"
        )

    tgb.text("## {translate('raw_data', selected_language)}", mode="md")
    tgb.table(data="{translated_raw_data}")

page.css = """
.language-selector {
    margin-bottom: 15px;
    text-align: right;
}
.filter-card {
    background-color: #f8f9fa;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
.metric-card {
    background-color: #f8f9fa;
    border-radius: 5px;
    padding: 15px;
    margin: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s;
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}
.metric-value {
    font-size: 1.5em;
    font-weight: bold;
    color: #007bff;
}
.alert-warning {
    background-color: #fff3cd;
    color: #856404;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 15px;
}
"""

Gui(page).run(
    title=translate("title", selected_language),
    dark_mode=False,
    debug=True,
    port="auto",
    allow_unsafe_werkzeug=True,
    async_mode="threading"
)
