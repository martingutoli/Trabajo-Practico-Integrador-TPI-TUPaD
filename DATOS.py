#la forma mas simple una lista de diccionerios

paises = [
    {
        'nombre': 'Argentina',
        'poblacion': 45376763,
        'superficie': 2780400,
        'continente': 'América'
    },
    {
        'nombre': 'Brasil', 
        'poblacion': 213993437,
        'superficie': 8515767,
        'continente': 'América'
    },
    # ... más países
]


# Para búsquedas por nombre (exactas)
indice_nombres = {
    'argentina': {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'},
    'brasil': {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
}

# Para búsquedas por continente
indice_continentes = {
    'América': [
        {'nombre': 'Argentina',  'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'},
        {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
    ],
    'Europa': [
        {'nombre': 'Alemania', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'Europa'}       
    ]
}



