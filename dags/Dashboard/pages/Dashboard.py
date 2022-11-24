import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback, State
import dash
from dash import dcc, html
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go




dash.register_page(__name__, path='/')

df = pd.read_csv("properties.csv")
df_cp = pd.read_csv("belgian-cities-geocoded.csv")
df_cp = df_cp[['postal', 'lat', 'lng']]
df_cp.rename(columns={'postal':'postal_code'}, inplace=True)
df = df.merge(df_cp, on='postal_code')
df = df.drop('Unnamed: 0', axis=1)
# df.to_csv('merged.csv', index=False)
df_corr = df[['price', 'province', 'type_of_property', 'number_of_bedrooms', 'surface', 'fully_equipped_kitchen', 'furnished', 'open_fire', 'terrace', 
'terrace_surface','garden', 'garden_surface', 'land_surface', 'number_of_facades', 'swimming_pool', 'state_of_the_building']]

cat_values = ['region', 'province', 'type_of_property', 'subtype_of_property', 'fully_equipped_kitchen', 'furnished', 'open_fire', 'terrace', 'garden', 'swimming_pool', 'state_of_the_building']
cont_values = ['number_of_bedrooms', 'surface', 'terrace_surface', 'garden_surface', 'land_surface', 'number_of_facades']

df_map = df.groupby(['region'])[['price', 'lat', 'lng']].mean()
df_map = df_map.reset_index()

fig = px.scatter_mapbox(
    data_frame=df_map,
    lat='lat',
    lon='lng',
    color='price',
    size='price',
    hover_data=['region', 'price'],
    color_continuous_scale=px.colors.sequential.thermal,
    size_max=40,
    template='plotly_dark',
    mapbox_style='carto-positron',

)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, clickmode= 'event+select')


# App layout
layout = html.Div([
    html.H1("Dashboard", style={'text-align': 'center'}),
    html.H2("Interactive map", style={'text-align': 'left'}),
    dcc.Graph(id='mean price map', figure=fig,style={'height': '80vh'}),
    html.Br(),
    html.H2("Correlations", style={'text-align': 'left'}),
    dcc.Dropdown(id='features' ,multi=True, value=df_corr.columns, options=[{'label': x, 'value': x} for x in df_corr.columns]),
    dcc.Graph(id='correlations', figure={},style={'height': '80vh'}),
    html.Br(),
])


@callback(Output(component_id='mean price map', component_property='figure'),Input(component_id='mean price map', component_property='clickData'), State('mean price map', 'figure'))
def show_map(region_chosen, figure):

    if region_chosen:
        print(f'click data: {region_chosen}')
        click_region = region_chosen['points'][0]['customdata'][0]
        df_region = df[df['region']==click_region]
        df_province = df_region.groupby(['province'])[['price', 'lat', 'lng']].mean()
        df_province = df_province.reset_index()
        print(df_province)
        figure = px.scatter_mapbox(
            data_frame=df_province,
            lat='lat',
            lon='lng',
            color='price',
            size='price',
            hover_data=['province', 'price'],
            color_continuous_scale=px.colors.sequential.thermal,
            size_max=40,
            template='plotly_dark',
            mapbox_style='open-street-map',
        )
        figure = figure.update_layout(overwrite=True, margin={"r": 0, "t": 0, "l": 0, "b": 0}, clickmode= 'event+select')

    return figure

@callback(Output(component_id='correlations', component_property='figure'),Input(component_id='features', component_property='value'))
def update_corr(corr_pick):
    df_correlations = df_corr[corr_pick].corr()
    x = list(df_correlations.columns)
    y = list(df_correlations.index)
    z = df_correlations.values

    fig_corr = ff.create_annotated_heatmap(
        z,
        x=x,
        y=y,
        annotation_text=np.around(z, decimals=2),
        hoverinfo='z',
        colorscale='Blues'
    )
    return fig_corr


