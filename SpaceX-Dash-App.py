# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px


# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# Create a dash application
app = dash.Dash(__name__)


# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#945F56',
                                               'fontSize': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                            options=[
                                                {'label': 'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                            ],
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                            ),
                                html.Br(),



                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),


                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                                id='payload-slider',
                                                min=0,
                                                max=10000,
                                                step=1000,
                                                value=[min_payload, max_payload],
                                                marks={
                                                    0: '0',
                                                    2000: '2k',
                                                    4000: '4k',
                                                    6000: '6k',
                                                    8000: '8k',
                                                    10000: '10k'
                                                },
                                                tooltip={"placement": "bottom", "always_visible": True}
                                              ),

                                #ADDITIONAL FEATURE:Booster Dropdown
                                html.Label("Booster Version:"),
                                dcc.Dropdown(
                                    id='booster-dropdown',
                                    options=[{'label': 'All Boosters', 'value': 'ALL'}] +
                                            [{'label': b, 'value': b} for b in spacex_df['Booster Version Category'].unique()],
                                    value='ALL',
                                    clearable=False,
                                    searchable=True
                                ),
                                html.Br(),
                                
                                
                                #ADDITIONAL FEATURE: Add KPI metrics for total success rate based on filtered metrics
                                html.Div(id='success-rate-output', style={'marginTop': '20px'}),


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])


# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output('success-pie-chart', 'figure'),
              Input('site-dropdown', 'value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df[spacex_df['class'] == 1],
                     names='Launch Site',
                     title='Total Success Launches By Site',
                     color='Launch Site',
                     color_discrete_map={
                        'CCAFS LC-40': '#945F56',
                        'VAFB SLC-4E': '#f39685',
                        'KSC LC-39A': '#f2dacf',
                        'CCAFS SLC-40': '#D6BCB7'
                      }
                    )
        return fig
    else:
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        outcome_counts = site_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        outcome_counts['Outcome'] = outcome_counts['Outcome'].map({1: 'Success', 0: 'Failure'})


        fig = px.pie(outcome_counts,
                     values='Count',
                     names='Outcome',
                     title=f'Total Success vs Failure for site {entered_site}',
                     color='Outcome',
                     color_discrete_map={
                       'Success': '#6a9c79',
                       'Failure': '#c0504d'
                      }
                    )
        return fig




# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'),
               Input('payload-slider', 'value'),
               Input('booster-dropdown', 'value')])
def get_scatter_chart(entered_site, entered_payload, entered_booster):
    low, high = entered_payload

    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                            (spacex_df['Payload Mass (kg)'] <= high)]
  
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
      
    if entered_booster != 'ALL':
        filtered_df = filtered_df[filtered_df['Booster Version Category'] == entered_booster]


    filtered_df['class_label'] = filtered_df['class'].map({0: 'Failure', 1: 'Success'})

    fig = px.scatter(filtered_df,
                     x='Payload Mass (kg)',
                     y='class_label',
                     color='Booster Version Category',
                     title="Correlation between Payload and Launch Success",
                     color_discrete_map={
                        'v1.0': '#945F56',
                        'v1.1': '#f39685',
                        'FT': '#f2dacf',
                        'B4': '#D6BCB7',
                        'B5': '#c0504d'
                      }
                    )
    fig.update_yaxes(title_text='Launch Result')
  
    return fig

# ADDITIONAL FEATURE: Callback for total success rate based on filtered metrics
@app.callback(
    Output('success-rate-output', 'children'),
    [
        Input('site-dropdown', 'value'),
        Input('payload-slider', 'value'),
        Input('booster-dropdown', 'value')
    ]
)
def update_payload_success_summary(entered_site, payload_range, entered_booster):
    low, high = payload_range

    # Apply payload filter
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    # Apply site filter
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    # Apply booster filter
    if entered_booster != 'ALL':
        filtered_df = filtered_df[filtered_df['Booster Version Category'] == entered_booster]

    # Handle cases with no launches
    total_launches = len(filtered_df)
    if total_launches == 0:
        return html.Div("No launches found for this selection.")

    # Final calculations
    successes = filtered_df['class'].sum()
    failures = total_launches - successes
    success_rate = (successes / total_launches) * 100

    # KPI Cards using CSS classes
    return html.Div(
        style={"display": "flex", "gap": "20px", "marginTop": "15px", "flexWrap": "wrap"},
        children=[

            html.Div([
                html.Div("Total Launches", className="kpi-label"),
                html.Div(f"{total_launches:,}", className="kpi-value")
            ], className="kpi-card"),

            html.Div([
                html.Div("Successes", className="kpi-label"),
                html.Div(f"{successes:,}", className="kpi-value")
            ], className="kpi-card"),

            html.Div([
                html.Div("Failures", className="kpi-label"),
                html.Div(f"{failures:,}", className="kpi-value")
            ], className="kpi-card"),

            html.Div([
                html.Div("Success Rate", className="kpi-label"),
                html.Div(f"{success_rate:.1f}%", className="kpi-value")
            ], className="kpi-card")
        ]
    )
