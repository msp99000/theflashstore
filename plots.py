import plotly.express as px
import plotly.graph_objects as go
from backend import *
import streamlit as st


''' ----- BEST SELLING ITEMS -----'''

@st.cache(show_spinner=False)
def plot_best_selling_items():
    fig = px.bar(
        y=best_selling_items().keys(),
        x=best_selling_items().values(),
        orientation="h",
        template="plotly_white",
    )

    fig.update_traces(
        textposition='outside',
        texttemplate='%{x:.2s}',
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_layout(
        height=200,
        width=750,
        xaxis_title="<b>Item</b>",
        yaxis_title="<b>Quantity</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )
    return fig


''' ----- LEAST SELLING ITEMS -----'''

@st.cache(show_spinner=False)
def plot_least_selling_items():
    fig = px.bar(
        y=least_selling_items().keys(),
        x=least_selling_items().values(),
        orientation="h",
        template="plotly_white",
    )

    fig.update_traces(
        textposition='outside',
        texttemplate='%{x:.2s}',
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_layout(
        height=200,
        width=750,
        xaxis_title="<b>Item</b>",
        yaxis_title="<b>Quantity</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )
    return fig




@st.cache(show_spinner=False)
def items_sunburst_plot():
    fig = px.sunburst(
        item_data,
        path=["category", 'sub_category', 'name'],
        color_discrete_sequence=px.colors.qualitative.Dark24,
        template="plotly_white",
        height=650,
        width=650,
    )

    fig.update_traces(textinfo="label+percent parent")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=16, color="#000000"),
    )

    return fig



@st.cache()
def gender_plot():
    fig = px.pie(
        data_frame = store,
        names = 'gender',
        height = 500,
        width = 500
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=16, color="#000000"),
    )

    return fig



@st.cache()
def cust_items_sunburst():
    fig = px.sunburst(
        store,
        path=["category", 'sub_category', 'name', 'gender'],
        color_discrete_sequence=px.colors.qualitative.Dark24,
        template="plotly_white",
        height=650,
        width=650,
    )

    fig.update_traces(textinfo="label+percent parent")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=16, color="#000000"),
    )

    return fig




def bar_plot_dob():
    fig = px.bar(
        bar_plot(),
        x='Year',
        y='Count',
        height = 500,
        width = 500
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=16, color="#000000"),
    )

    fig.update_traces(
        textposition='outside',
    )

    return fig


def item_count_plot():
    fig = px.bar(
        item_count(),
        y='name',
        x='item_count',
        height = 1000,
        width = 600,
        orientation='h'
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textposition='outside',
        texttemplate='%{x:.2s}',
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Count</b>",
        yaxis_title="<b>Items</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig



def plot_year_cust_count():
    fig = px.bar(
        year_cust_count(),
        x='year',
        y='customer_count',
        height = 500,
        width = 650
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textposition='outside',
        # texttemplate='%{x:.2s}',
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Year</b>",
        yaxis_title="<b>Customer Count</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig




def plot_sales_by_age():
    fig = px.bar(
        sales_by_age(),
        y='age',
        x='total_sales',
        height=350,
        width=750,
        orientation='h'
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textposition='outside',
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Sales</b>",
        yaxis_title="<b>Customer Age</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig


def category_sunburst():

    fig = px.sunburst(
        store,
        path=['category', 'sub_category', 'customer_age'],
        color_discrete_sequence=px.colors.qualitative.Dark24,
        template="plotly_white",
        height=650,
        width=650,
    )

    fig.update_traces(textinfo="label+percent parent")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=16, color="#000000"),
    )

    return fig



def plot_per_customer_sales():
    fig = px.line(
        per_customer_sales(),
        x='name',
        y='total_sales',
        height=350,
        width=650,
        orientation='h',
        markers=True
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Customers</b>",
        yaxis_title="<b>Sales</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig



def plot_sales_per_hour():
    fig = px.line(
        sales_per_hour(),
        x='hour',
        y='total_sales',
        height=350,
        width=650,
        orientation='h',
        markers=True
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Hours</b>",
        yaxis_title="<b>Sales</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig



def plot_sales_per_item():
    fig = px.line(
        sales_per_item(),
        x='item_name',
        y='total_sales',
        height=700,
        width=650,
        orientation='h',
        markers=True
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    fig.update_traces(
        textfont=dict(
            family='Arial',
            size=12,
            color='#000000'
        ),
    )

    fig.update_layout(
        xaxis_title="<b>Items</b>",
        yaxis_title="<b>Sales</b>",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
        margin=dict(l=4, r=4, t=4, b=4),
        font=dict(family="Arial", size=14, color="#000000"),
    )

    return fig