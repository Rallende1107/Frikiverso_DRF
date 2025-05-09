default_movie_genres = [
    {'name': 'Action', 'name_esp': 'Acción', 'is_active': True, 'explicit': False, 'description': 'Películas con escenas de lucha, persecuciones y mucha adrenalina.',},
    {'name': 'Adventure', 'name_esp': 'Aventura', 'is_active': True, 'explicit': False, 'description': 'Películas con viajes emocionantes y exploración de lugares desconocidos.',},
    {'name': 'Comedy', 'name_esp': 'Comedia', 'is_active': True, 'explicit': False, 'description': 'Películas diseñadas para hacer reír al público.',},
    {'name': 'Drama', 'name_esp': 'Drama', 'is_active': True, 'explicit': False, 'description': 'Películas que exploran conflictos emocionales y situaciones de la vida real.',},
    {'name': 'Science Fiction', 'name_esp': 'Ciencia Ficción', 'is_active': True, 'explicit': False, 'description': 'Películas con elementos científicos y tecnológicos especulativos.',},
    {'name': 'Fantasy', 'name_esp': 'Fantasía', 'is_active': True, 'explicit': False, 'description': 'Películas con elementos mágicos, criaturas míticas y mundos imaginarios.',},
    {'name': 'Horror', 'name_esp': 'Terror', 'is_active': True, 'explicit': False, 'description': 'Películas que buscan asustar, causar miedo y repulsión.',},
    {'name': 'Thriller', 'name_esp': 'Suspenso', 'is_active': True, 'explicit': False, 'description': 'Películas que generan tensión e incertidumbre en el espectador.',},
    {'name': 'Animation', 'name_esp': 'Animación', 'is_active': True, 'explicit': False, 'description': 'Películas creadas mediante la técnica de animación.',},
    {'name': 'Romance', 'name_esp': 'Romance', 'is_active': True, 'explicit': False, 'description': 'Películas centradas en relaciones amorosas y emocionales.',},
    {'name': 'Crime', 'name_esp': 'Crimen', 'is_active': True, 'explicit': False, 'description': 'Películas que giran en torno a actividades delictivas y sus consecuencias.',},
    {'name': 'Mystery', 'name_esp': 'Misterio', 'is_active': True, 'explicit': False, 'description': 'Películas que presentan enigmas y secretos que deben ser resueltos.',},
    {'name': 'Historical', 'name_esp': 'Histórico', 'is_active': True, 'explicit': False, 'description': 'Películas basadas en eventos o personajes del pasado.',},
    {'name': 'Western', 'name_esp': 'Oeste', 'is_active': True, 'explicit': False, 'description': 'Películas ambientadas en el Viejo Oeste americano.',},
    {'name': 'Family', 'name_esp': 'Familiar', 'is_active': True, 'explicit': False, 'description': 'Películas aptas para ser disfrutadas por toda la familia.',},
    {'name': 'Melodrama', 'name_esp': 'Melodrama', 'is_active': False, 'explicit': False, 'description': '',}
]

default_movie_types = [
    {'name': 'Documentary', 'name_esp': 'Documental', 'description': 'Películas que presentan hechos reales con fines informativos o de análisis.', 'is_active': True,},
    {'name': 'Animated Feature Film', 'name_esp': 'Largometraje Animado', 'description': 'Películas de animación de larga duración.', 'is_active': True,},
    {'name': 'Live-Action Feature Film', 'name_esp': 'Largometraje de Acción Real', 'description': 'Películas con actores reales.', 'is_active': True,},
    {'name': 'Short Film', 'name_esp': 'Cortometraje', 'description': 'Películas de corta duración.', 'is_active': True,},
    {'name': 'TV Movie', 'name_esp': 'Película para Televisión', 'description': 'Películas producidas para ser emitidas en televisión.', 'is_active': True,},
    {'name': 'Direct-to-Video', 'name_esp': 'Directo a Video', 'description': 'Películas lanzadas directamente en formato de video.', 'is_active': True,},
    {'name': 'Independent Film', 'name_esp': 'Película Independiente', 'description': 'Películas producidas fuera de los grandes estudios.', 'is_active': True,},
    {'name': 'Experimental Film', 'name_esp': 'Película Experimental', 'description': 'Películas que desafían las convenciones narrativas y formales.', 'is_active': True,},
]

default_movie_roles = [
    {'name': 'Lead', 'name_esp': 'Principal', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'El actor o actriz que interpreta al personaje central de la película.',},
    {'name': 'Supporting', 'name_esp': 'Actor de Reparto', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un actor o actrizque interpreta un personaje secundario importante.',},
    {'name': 'Cameo', 'name_esp': 'Cameo', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Una aparición breve de una persona famosa en la película.',},
    {'name': 'Voice Actor', 'name_esp': 'Actor de Voz', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un actor que proporciona la voz de un personaje animado o digital.',},
    {'name': 'Narrator', 'name_esp': 'Narrador', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'La voz en off que cuenta parte de la historia.',},
    {'name': 'Extra', 'name_esp': 'Extra Destacado', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un extra con una participación ligeramente más notable.',},
    {'name': 'Director', 'name_esp': 'Director', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la visión creativa general de la película.',},
    {'name': 'Screenwriter', 'name_esp': 'Guionista', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que escribe el guion de la película.',},
    {'name': 'Producer', 'name_esp': 'Productor', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la gestión y financiación de la película.',},
    {'name': 'Cinematographer', 'name_esp': 'Director de Fotografía', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la filmación y el aspecto visual de la película.',},
    {'name': 'Film Editor', 'name_esp': 'Montajista', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que ensambla las diferentes tomas para crear la película final.',},
    {'name': 'Production Designer', 'name_esp': 'Diseñador de Producción', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del aspecto visual del set y los escenarios.',},
    {'name': 'Costume Designer', 'name_esp': 'Diseñador de Vestuario', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del vestuario de los personajes.',},
    {'name': 'Composer', 'name_esp': 'Compositor', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que escribe la música original para la película.',},
    {'name': 'Sound Designer', 'name_esp': 'Diseñador de Sonido', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del diseño y la mezcla del sonido de la película.',},
    {'name': 'Art Director', 'name_esp': 'Director de Arte', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la supervisión de los aspectos visuales de la película.',},
    {'name': 'Casting Director', 'name_esp': 'Director de Casting', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de seleccionar a los actores para los roles.',},
    {'name': 'Visual Effects Supervisor', 'name_esp': 'Supervisor de Efectos Visuales', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la creación de los efectos visuales.',},
    # Roles de Casting
    {'name': 'Lead', 'name_esp': 'Principal', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'El actor o actriz que interpreta al personaje central de la película.',},
    {'name': 'Supporting', 'name_esp': 'Actor de Reparto', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un actor o actrizque interpreta un personaje secundario importante.',},
    {'name': 'Cameo', 'name_esp': 'Cameo', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Una aparición breve de una persona famosa en la película.',},
    {'name': 'Voice Actor', 'name_esp': 'Actor de Voz', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un actor que proporciona la voz de un personaje animado o digital.',},
    {'name': 'Narrator', 'name_esp': 'Narrador', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'La voz en off que cuenta parte de la historia.',},
    {'name': 'Extra', 'name_esp': 'Extra Destacado', 'role_cast': True, 'role_staff': False, 'is_active': True, 'description': 'Un extra con una participación ligeramente más notable.',},
    {'name': 'Director', 'name_esp': 'Director', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la visión creativa general de la película.',},
    {'name': 'Screenwriter', 'name_esp': 'Guionista', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que escribe el guion de la película.',},
    {'name': 'Producer', 'name_esp': 'Productor', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la gestión y financiación de la película.',},
    {'name': 'Cinematographer', 'name_esp': 'Director de Fotografía', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la filmación y el aspecto visual de la película.',},
    {'name': 'Film Editor', 'name_esp': 'Montajista', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que ensambla las diferentes tomas para crear la película final.',},
    {'name': 'Production Designer', 'name_esp': 'Diseñador de Producción', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del aspecto visual del set y los escenarios.',},
    {'name': 'Costume Designer', 'name_esp': 'Diseñador de Vestuario', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del vestuario de los personajes.',},
    {'name': 'Composer', 'name_esp': 'Compositor', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona que escribe la música original para la película.',},
    {'name': 'Sound Designer', 'name_esp': 'Diseñador de Sonido', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable del diseño y la mezcla del sonido de la película.',},
    {'name': 'Art Director', 'name_esp': 'Director de Arte', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la supervisión de los aspectos visuales de la película.',},
    {'name': 'Casting Director', 'name_esp': 'Director de Casting', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de seleccionar a los actores para los roles.',},
    {'name': 'Visual Effects Supervisor', 'name_esp': 'Supervisor de Efectos Visuales', 'role_cast': False, 'role_staff': True, 'is_active': True, 'description': 'La persona responsable de la creación de los efectos visuales.',},
]

default_movie_ratings = [
    {'acronym': 'G', 'name': 'General Audiences.', 'name_esp': 'Audiencia General.', 'is_active': True, 'description': 'Se admiten todas las edades. \nNo se permite que los niños vean nada que pueda ofender a los padres.',},
    {'acronym': 'PG', 'name': 'Parental Guidance Suggested.', 'name_esp': 'Guía Paterna Sugerida.', 'is_active': True, 'description': 'Algunos materiales pueden no ser adecuados para niños.\nSe recomienda a los padres que brinden \'orientación parental\'. Puede contener material que a los padres no les guste para sus hijos pequeños.',},
    {'acronym': 'PG-13', 'name': 'Parents Strongly Cautioned', 'name_esp': 'Guía Paterna Estricta', 'is_active': True, 'description': 'Algunos materiales pueden ser inapropiados para niños menores de 13 años.\nSe recomienda a los padres que tengan cuidado. Algunos materiales pueden ser inapropiados para preadolescentes.',},
    {'acronym': 'R', 'name': 'Restricted', 'name_esp': 'Restringido', 'is_active': True, 'description': 'Los menores de 17 años deben ir acompañados de un padre o tutor adulto.\nContiene material para adultos.\nSe recomienda a los padres que se informen más sobre la película antes de llevar a sus hijos pequeños con ellos.',},
    {'acronym': 'NC-17', 'name': 'Adults Only', 'name_esp': 'Solo Adultos', 'is_active': True, 'description': 'No Apta para Menores de 17 años.\nContiene material explícito para adultos.',},
]


