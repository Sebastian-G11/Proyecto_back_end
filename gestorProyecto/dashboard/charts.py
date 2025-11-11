from collections import defaultdict
from dimensiones.service import dimensiones_service
from acciones.service import acciones_service
from actividades.service import actividades_service
import plotly.graph_objs as go
from django.db.models import Count
from django.db.models.functions import TruncMonth

def presupuesto_dimensiones():
    """
    Tipo: Gráfico de barras agrupadas
    Datos: Presupuesto anual vs presupuesto reajustado por dimensión
    Query: Sumar presupuestos de acciones agrupados por dimensión
    """
    dimensiones = dimensiones_service.get_suma_presupuestos()
    print(dimensiones)

    nombres = [d['nombre'] for d in dimensiones]
    presupuestos_anuales = [d['total_anual'] or 0 for d in dimensiones]
    presupuestos_reajustados = [d['total_reajustado'] or 0 for d in dimensiones]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Presupuesto Anual',
        x=nombres,
        y=presupuestos_anuales,
        marker={'color': "#e1402b" },
        text=[f'${val:,.0f}' for val in presupuestos_anuales],
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        name='Presupuesto Reajustado',
        x=nombres,
        y=presupuestos_reajustados,
        marker={'color': "#57b5e4" },
        text=[f'${val:,.0f}' for val in presupuestos_reajustados],
        textposition='auto'
    ))

    fig.update_layout(
        title = 'Presupuesto por Dimensión: Anual vs Reajustado',
        xaxis_title = 'Dimensiones',
        yaxis_title = 'Presupuesto ($)',
        barmode='group',
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='white',
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig.to_html(full_html=False, include_plotlyjs='cdn')



def acciones_por_estado():
    """
    Tipo: Gráfico de pastel (pie chart)
    Datos: Cantidad de acciones por estado (En Planificación, En Ejecución, Finalizada, etc.)
    Query: Count de acciones agrupadas por estado
    """
    acciones_por_estado = acciones_service.get_acciones_agrupadas_por_estado()
    nombres = [a['nombre'] for a in acciones_por_estado]
    totales = [a['total_acciones'] for a in acciones_por_estado]

    fig = go.Figure(data=[
        go.Pie(
            labels=nombres,
            values=totales,
            hole=0.4,  # Donut chart
            marker={
                'colors': ['#57b5e4', '#e1402b', '#2ecc71', '#f39c12', '#9b59b6'],
                'line': {'color': 'white', 'width': 2}
            },
            textinfo='label+percent+value',
            textfont={'size': 14, 'color': 'white'},
            hovertemplate='<b>%{label}</b><br>Acciones: %{value}<br>Porcentaje: %{percent}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title='Distribución de Acciones por Estado',
        paper_bgcolor='white',
        height=400,
        font={'family': 'Segoe UI, sans-serif', 'size': 12},
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def progreso_actividades():
    """
    Tipo: Barra horizontal apilada
    Datos: Porcentaje de actividades por estado dentro de cada dimensión
    Query: Count de actividades por estado y dimensión (through acción)
    """
    data = actividades_service.get_actividades_agrupadas_por_accion()

    datos_por_dimension = defaultdict(lambda: defaultdict(int))
    dimensiones_set = set()
    estados_set = set()

    for item in data:
        dimension = item["accion__dimension__nombre"]
        estado = item["estado__nombre"]
        total = item["total_actividades"]
    
        datos_por_dimension[dimension][estado] += total
        dimensiones_set.add(dimension)
        estados_set.add(estado)
    
    dimensiones = sorted(dimensiones_set)
    estados = sorted(estados_set)
    
    fig = go.Figure()

    colores = {
        'Pendiente': "#e2d467",     
        'En Progreso': '#57b5e4',  
        'Completado': '#2ecc71',     
        'Cancelada': '#e1402b',     
    }
    

    for estado in estados:
        valores = [datos_por_dimension[dim][estado] for dim in dimensiones]

        fig.add_trace(go.Bar(
            name=estado,
            x=valores,
            y=dimensiones,
            orientation='h',
            marker={'color': colores.get(estado, '#95a5a6')},
            text=valores,
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>%{fullData.name}: %{x} actividades<extra></extra>'
        ))
    
    fig.update_layout(
        title='Progreso de Actividades por Dimensión',
        xaxis_title='Cantidad de Actividades',
        yaxis_title='Dimensión',
        barmode='stack',  
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='white',
        height=400,
        hovermode='y unified',
        font={'family': 'Segoe UI, sans-serif', 'size': 12},
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title_text='Estado'
        )
    )
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')


def evolucion_temporal_acciones():
    """
    Tipo: Gráfico de línea temporal
    Datos: Cantidad de acciones creadas por mes
    Query: Count de acciones agrupadas por mes/año
    """
    
    acciones_por_mes = acciones_service.get_acciones_por_mes()
    
    fechas = [item['mes'] for item in acciones_por_mes]
    totales = [item['total'] for item in acciones_por_mes]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=fechas,
        y=totales,
        mode='lines+markers',
        name='Acciones Creadas',
        line={'color': '#57b5e4', 'width': 3},
        marker={'size': 8, 'color': '#e1402b'},
        fill='tozeroy',
        fillcolor='rgba(87, 181, 228, 0.2)',
        hovertemplate='<b>%{x}</b><br>Acciones: %{y}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Evolución Temporal de Acciones Creadas',
        xaxis_title='Mes',
        yaxis_title='Cantidad de Acciones',
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='white',
        height=400,
        hovermode='x unified',
        font={'family': 'Segoe UI, sans-serif', 'size': 12},
        xaxis={
            'tickangle': -45,
            'showgrid': True,
            'gridcolor': '#e9ecef',
            'tickformat': '%b %Y',
            'dtick': 'M1'
        },
        yaxis={
            'showgrid': True,
            'gridcolor': '#e9ecef'
        }
    )
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')





