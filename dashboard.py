import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Chargement des données (Assurez-vous que le fichier CSV est dans le même dossier)
# Si vous ne l'avez pas encore, téléchargez-le et uploadez-le ici.
df = pd.read_csv('automobile-sales.csv')

# Initialisation de l'application Dash (TÂCHE 2.1)
app = dash.Dash(__name__)

# Mise en page de l'application (TÂCHES 2.2 et 2.3)
app.layout = html.Div(children=[
    html.H1("Tableau de bord des ventes automobiles", style={'textAlign': 'center'}),
    
    # Menu déroulant pour choisir le type de statistiques (TÂCHE 2.2)
    html.Div([
        html.Label("Sélectionnez le type de statistiques :"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Statistiques annuelles', 'value': 'Yearly Statistics'},
                {'label': 'Statistiques de la période de récession', 'value': 'Recession Period Statistics'}
            ],
            value='Yearly Statistics', # Valeur par défaut
            placeholder="Sélectionnez une option"
        )
    ], style={'width': '50%', 'margin': 'auto', 'padding': '20px'}),

    # Menu déroulant pour choisir l'année (TÂCHE 2.2)
    html.Div([
        html.Label("Sélectionnez l'année :"),
        dcc.Dropdown(
            id='dropdown-year',
            options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
            value=df['Year'].min(), # Valeur par défaut
            placeholder="Sélectionnez une année"
        )
    ], style={'width': '50%', 'margin': 'auto', 'padding': '20px'}),

    # Conteneur pour afficher les graphiques (TÂCHE 2.3)
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'})
])

# Fonction de rappel (Callback) pour mettre à jour les graphiques (TÂCHE 2.4)
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'),
     Input(component_id='dropdown-year', component_property='value')]
)
def update_output(statistics_type, selected_year):
    # Création d'une liste pour stocker les graphiques
    charts = []

    # Vérification du type de statistiques sélectionné
    if statistics_type == 'Recession Period Statistics':
        # Filtrer les données pour la récession
        recession_df = df[df['Recession'] == 1]
        
        # Graphique 1 : Ventes moyennes par type de véhicule pendant la récession (TÂCHE 2.5)
        fig1 = go.Figure(data=[
            go.Bar(x=recession_df['Vehicle_Type'], y=recession_df['Automobile_Sales'], name='Ventes')
        ])
        fig1.update_layout(title='Ventes moyennes par type de véhicule (Récession)', xaxis_title='Type de véhicule', yaxis_title='Ventes moyennes')
        charts.append(dcc.Graph(figure=fig1))

        # Graphique 2 : Dépenses publicitaires par type de véhicule pendant la récession (TÂCHE 2.5)
        fig2 = go.Figure(data=[
            go.Pie(labels=recession_df['Vehicle_Type'], values=recession_df['Advertising_Expenditure'], hole=.3)
        ])
        fig2.update_layout(title='Répartition des dépenses publicitaires (Récession)')
        charts.append(dcc.Graph(figure=fig2))

    elif statistics_type == 'Yearly Statistics':
        # Filtrer les données pour l'année sélectionnée
        yearly_df = df[df['Year'] == selected_year]

        # Graphique 1 : Ventes totales par mois pour l'année sélectionnée (TÂCHE 2.6)
        fig3 = go.Figure(data=[
            go.Scatter(x=yearly_df['Month'], y=yearly_df['Automobile_Sales'], mode='lines+markers', name='Ventes')
        ])
        fig3.update_layout(title=f'Ventes mensuelles pour l\'année {selected_year}', xaxis_title='Mois', yaxis_title='Ventes totales')
        charts.append(dcc.Graph(figure=fig3))

        # Graphique 2 : Ventes par type de véhicule pour l'année sélectionnée (TÂCHE 2.6)
        fig4 = go.Figure(data=[
            go.Bar(x=yearly_df['Vehicle_Type'], y=yearly_df['Automobile_Sales'], name='Ventes')
        ])
        fig4.update_layout(title=f'Ventes par type de véhicule pour l\'année {selected_year}', xaxis_title='Type de véhicule', yaxis_title='Ventes')
        charts.append(dcc.Graph(figure=fig4))

    return charts

# Exécution de l'application (TÂCHE 2.1)
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)