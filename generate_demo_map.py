import folium
import os
import webbrowser
import time

# Coordenadas de exemplo (centro de São Paulo)
center = [-23.534564, -46.654302]

m = folium.Map(location=center, zoom_start=13)

# Pontos de exemplo (paradas simuladas)
paradas_exemplo = [
    {"np": "Parada A", "py": -23.534564, "px": -46.654302},
    {"np": "Parada B", "py": -23.525799, "px": -46.679251},
    {"np": "Parada C", "py": -23.526523, "px": -46.673588},
    {"np": "Parada D", "py": -23.535317, "px": -46.653005},
]

for p in paradas_exemplo:
    folium.Marker(location=[p["py"], p["px"]], popup=p["np"]).add_to(m)

output = 'paradas_demo.html'
m.save(output)
path = os.path.abspath(output)
print(f'Demo map saved to {path}')

# Abrir automaticamente no navegador padrão
time.sleep(0.2)
webbrowser.open(f'file://{path}')
