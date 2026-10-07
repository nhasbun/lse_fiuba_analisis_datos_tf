# Características Principales

## Variables

- Categóricas nominales: ['IUCR', 'Primary Type', 'Description', 'FBI Code', 'Location Description', 'Block', 'Location', 'Beat', 'District', 'Ward', 'Community Area']
- Cuantitativas continuas: ['X Coordinate', 'Y Coordinate', 'Latitude', 'Longitude']
- Temporales: ['Date', 'Year', 'Updated On']
- Categóricas binarias: ['Arrest', 'Domestic']

Algunas variables como Beat, District, Ward y Community Area son representadas con números pero no tiene valor numérico, representan barrios o comunas.
Year es una variable redundante dado que el dataset es específicamente del año 2015.

## Variable 'Primary Type'

El tipo de crimen tiene una distribución asimétrica. El top 3 incluye el 50.9% de los crímenes y el top 10 incluye del 91.7%.

| Tipo de delito             | %del total |
| -------------------------- | ---------- |
| THEFT                      | 21.65      |
| BATTERY                    | 18.47      |
| CRIMINAL DAMAGE            | 10.83      |
| NARCOTICS                  | 9.04       |
| OTHER OFFENSE              | 6.63       |
| ASSAULT                    | 6.44       |
| DECEPTIVE PRACTICE         | 6.23       |
| BURGLARY                   | 4.98       |
| MOTOR VEHICLE THEFT        | 3.80       |
| ROBBERY                    | 3.64       |
| CRIMINAL TRESPASS          | 2.42       |
| WEAPONS VIOLATION          | 1.27       |
| OFFENSE INVOLVING CHILDREN | 0.95       |
| PUBLIC PEACE VIOLATION     | 0.91       |
| PROSTITUTION               | 0.50       |

## Variables 'Arrest' y 'Domestic'

Ciertas categorías de delito como apuestas, narcóticos, prostitución, violación de ley de licor y armas casi siempre tienen arrestos porque el delito es "reactivo": se ficha cuándo ya hubo un arresto.

Tasa de arresto global (%): 26.5%
Porcentaje de casos domésticos: 18.5%

| Tipi de delito                    |  Media | Tamaño |
| :-------------------------------- | -----: | -----: |
| GAMBLING                          | 100.00 |    310 |
| NON-CRIMINAL                      | 100.00 |      1 |
| PUBLIC INDECENCY                  | 100.00 |     14 |
| NARCOTICS                         |  99.97 | 23,939 |
| PROSTITUTION                      |  99.85 |  1,322 |
| LIQUOR LAW VIOLATION              |  99.66 |    292 |
| CONCEALED CARRY LICENSE VIOLATION |  97.06 |     34 |
| INTERFERENCE WITH PUBLIC OFFICER  |  95.80 |  1,308 |
| WEAPONS VIOLATION                 |  79.76 |  3,364 |
| PUBLIC PEACE VIOLATION            |  77.66 |  2,422 |
| OBSCENITY                         |  71.43 |     49 |
| CRIMINAL TRESPASS                 |  68.68 |  6,401 |
| HOMICIDE                          |  44.42 |    502 |

## Estacionalidad/Fecha y hora

Hay una notable conexión entre la estacionalidad y la tasa de delitos cometidos: el mínimo es en febrero (mes más corto del año, es pleno invierno) y el máximo es en agosto (mes largo, es pleno verano).
Hay poca variabilidad en cuánto al día de la semana en que ocurre el crimen. Por hora, parece haber un pico al mediodía y continuar alto hasta la medianoche mientras que baja a la madrugada.
Sin embargo, dado que la hora puede ser la hora en la que el crimen queda registrado y no necesariamente el horario en que ocurrió el crimen algunos horarios pueden estar inflados.

## Locación

Chicago se encuentra dividido geográficamente por "community areas", similares a barrios.
Hay mucha varianza según la zona. Notese la diferencia entre las áreas con máxima cantidad de delitos (17,436) vs. el mínimo (258).

## Cantidad de crímenes por día

Aunque no es una variable del dataset, es una variable interesante para analizar dado que no hay verdaderas variables númericas discretas.
La media, mediana y mediana cortada son muy similares y el sentro de distribución es estable.
El desvío estandar es casi el doble del MAD. El desvío se ve afectado por unos pocos días outliers (ver sección Outliers) y por eso el MAD describe mejor las dispersión al ser más robusto.
Hay una asimetría positiva moderada, con una cola derecha de días con muchos registros. La curtosis indica colas pesadas, los outliers son más que en una distribución normal.

| Metrica           |    Valor |
| :---------------- | -------: |
| Media             |   725.78 |
| Mediana           |   732.00 |
| Moda              |   745.00 |
| Media cortada 5%  |   726.32 |
| Desvío estándar   |    92.76 |
| Varianza          | 8,603.63 |
| IQR               |   105.00 |
| IQR / rango       |     0.12 |
| MAD               |    52.00 |
| Asimetría         |     0.37 |
| Curtosis (exceso) |     4.42 |

## Variables categóricas - Entropía de Shannon

A la hora de realizar la codificación, hay que tener en cuenta la cardinalidad y distribución de las variables.
Variables como 'Block' presentan una cardinalidad muy alta, y en menor escala 'Description', 'IUCR', 'Beat', 'Location' y 'Descriptio' también tienen cardinalidad alta. Esto descartaría One-Hot encoding para estas variables.
Las variables geográficas tienen entropía cercana a 1, lo cuál muestra que los delitos están repartidos entre muchas zonas. 'Location Description' y 'Description' presentan la menor entropía.

| Variable                 | Cardinalidad | Moda             | Prop. Moda | Rango Frecuencia | Entropía | Entropía Max | Entropía Norm |
| :----------------------- | :----------: | :--------------- | :--------: | :--------------: | :------: | :----------: | :-----------: |
| **Primary Type**         |      32      | THEFT            |   0.217    |      57,354      |   3.49   |     5.00     |     0.70      |
| **Description**          |     342      | SIMPLE           |   0.103    |      27,417      |   5.47   |     8.42     |     0.65      |
| **IUCR**                 |     329      | 0820             |   0.093    |      24,678      |   5.63   |     8.36     |     0.67      |
| **FBI Code**             |      26      | 06               |   0.217    |      57,349      |   3.57   |     4.70     |     0.76      |
| **Location Description** |     140      | STREET           |   0.230    |      60,754      |   4.08   |     7.13     |     0.57      |
| **District**             |      23      | 11               |   0.074    |      19,528      |   4.40   |     4.52     |     0.97      |
| **Beat**                 |     274      | 421              |   0.009    |      2,250       |   7.99   |     8.10     |     0.99      |
| **Ward**                 |      50      | 28.0             |   0.050    |      10,833      |   5.45   |     5.64     |     0.97      |
| **Community Area**       |      77      | 25.0             |   0.066    |      17,178      |   5.82   |     6.27     |     0.93      |
| **Block**                |    27,523    | 001XX N STATE ST |   0.003    |       768        |  13.89   |    14.75     |     0.94      |
| **Domestic**             |      2       | False            |   0.815    |     166,884      |   0.69   |     1.00     |     0.69      |
| **Arrest**               |      2       | False            |   0.735    |     124,746      |   0.83   |     1.00     |     0.83      |

# Nulos y faltantes

Se notan nulos en las variables de data geográfica (coordenadas, longitud, latitud). Estos valores también faltan en las mismas filas, lo cuál significa que estas filas en específico no tienen ningún dato geográfico específico (más allá de la descripción del lugar).
Al analizar la descripción de locaciones de estas filas con datos faltantes se ve que en más del 50% de los casos se trata de departamentos y residencias. También hay una correlación muy fuerte entre el tipo de delito y las coordenadas faltantes: en la mayoría de los casos, son crímenes sexuales y delitos contra menores.
Esto puede deberse a un anonimato con propósito ya que se intenta ocultar la identidad de las víctimas y la mayoría de los crímenes sexuales (especialmente contra menores) suelen ocurrir en el hogar.

Por otro lado, "DECEPTIVE PRACTIVE" (se refiere a fraude) también carece de locación porque es más dificil identificar dónde ocurrió el crimen (ya que suelen ser crímenes online/telefónicos y robos de identidad).
Ej: entrar en la cuenta bancaria de alguien con sus datos

Coordenadas faltantes por tipo (Total = 2.6% de los datos)

| Tipo de delito             | Media | Tamaño |
| :------------------------- | ----: | -----: |
| CRIMINAL SEXUAL ASSAULT    | 0.419 |    148 |
| OFFENSE INVOLVING CHILDREN | 0.176 |  2,527 |
| SEX OFFENSE                | 0.173 |  1,054 |
| DECEPTIVE PRACTICE         | 0.146 | 16,502 |
| OBSCENITY                  | 0.143 |     49 |
| CRIM SEXUAL ASSAULT        | 0.101 |  1,319 |
| NARCOTICS                  | 0.097 | 23,939 |
| INTIMIDATION               | 0.057 |    123 |
| STALKING                   | 0.052 |    155 |
| OTHER OFFENSE              | 0.016 | 17,566 |
| THEFT                      | 0.011 | 57,355 |
| WEAPONS VIOLATION          | 0.009 |  3,364 |
| MOTOR VEHICLE THEFT        | 0.006 | 10,068 |
| BURGLARY                   | 0.006 | 13,184 |
| KIDNAPPING                 | 0.005 |    190 |

Los nulos en 'Ward' y 'Community Area' se concentran en un mismo distrito (Jefferson Park). Sin embargo, cuentan con datos de coordenadas lo cuál los hace recuperables.
Aunque parece una haber una relación con el distrito, es posible que sean faltantes MCAR y que simplemente se olvidó de asignarles datos geográficos puntuales.

# Datos duplicados e inconsistentes

Todos los casos de Case Number repetido se deben a casos de homicidio dónde cada fila representa a una víctima. Son repetidos por diseño: un mismo caso con varias víctimas.

CRIMINAL SEXUAL ASSAULT y CRIM SEXUAL ASSAULT figuran como dos categorías distintas de delito pero referencian un mismo crimen. Esto se debe a que la categoría parece haber sido renombrada entre 2020 y 2021. Lo ideal sería unificarlos o utilizar solo el IUCR al tratar con el tipo de crimen de ahora en adelante.

También hay casos de descripciones de locaciones repetidas por insonsistencia de datos:
EJ: 'VACANT LOT / LAND' y 'VACANT LOT/LAND' o 'SCHOOL, PRIVATE, GROUNDS' y 'SCHOOL - PRIVATE GROUNDS'
Lo ideal sería normalizar las descripciones para poder agruparlas correctamente.

También figura un mismo valor de 'Beat' perteneciendo a distintos distritos para 46 filas. Esto es corregible aunque se debería analizar si se debe a que esos beats fueron re-organizados a otro distrito o si fue un error.

Hay 9 filas que tienen distritos inválidos. Chicago cuenta con 22 distritos policiales. Es posible que estos registros con distrito policial no existente se deban a que se utilizó otra definición de distrito

Hay un caso de delito tipo 'NON-CRIMINAL' que puede considerarase eliminar dado que no es relevante a las actividades criminales.

# Outliers

En algunos casos parece ser que cuándo la fecha/hora real se desconocen en casos dónde es difícil saber con exactitud (fraudes, abuso sexual o abusos de menores) se registra el crimen a la hora 00:00 en el primer día del mes.
Se puede ver como un valor "por defecto" para llenar la planilla en vez de un dato real.
La hipótesis está potencialmente validada por el IQR, que muestra que el mayor outlier en fechas es el primer día del primer mes del año.
Es posible que enero también sea un mes default para agrupar crímenes o que los crímenes que ocurren en el periodo de fiestas se registren un mismo día.

El barrio de Austin tiene una mayor densidad de crimen comparado con otros barrios.
Sin embargo, en el 2015 era el área más poblada de Chicago al igual que una de las más pobres y con mayor desempleo, lo cuál puede explicar la densidad de crímenes superior.

# Resumen de calidad de datos

| Variable Afectada                            | Valores Afectados |       Tipo de Anomalía       | Razones / Causalidad                                                                                                      |
| :------------------------------------------- | :---------------: | :--------------------------: | :------------------------------------------------------------------------------------------------------------------------ |
| **Coordenadas** _(X, Y, Lat, Lon, Location)_ |   7,001 (2.6%)    | MAR o MNAR _(según el caso)_ | Oculto por privacidad en delitos sexuales/menores (hogar como locación principal) o por locación física ambigua (fraude). |
| **Location Description**                     |    620 (0.2%)     |       MAR/Estructural        | El 99% son casos de fraude que carecen de un lugar físico de ocurrencia.                                                  |
| **Community Area**                           |        14         |        Aparente MCAR         | Falla puntual de geocodificación específicamente concentrada en los Beats 1614 y 1654.                                    |
| **Ward**                                     |         2         |        Aparente MCAR         | Falla puntual y aislada de geocodificación.                                                                               |
| **Hora 00:00 y día 1 del mes**               |   aprox. 2,900    |          MNAR o MAR          | **Faltante encubierto:** Valor asignado por defecto por el sistema cuando la fecha u hora real es desconocida.            |
| **Case Number repetido**                     |        27         |          Por diseño          | Comportamiento esperado: los homicidios se representan con una fila individual por cada víctima.                          |
| **CRIM vs CRIMINAL SEXUAL ASSAULT**          |       1,467       |    Error de consistencia     | Problema de migración: la categoría fue renombrada formalmente entre los años 2020 y 2021.                                |
| **Location Description** _(Categorías)_      |  140 categorías   |    Error de consistencia     | Duplicidad de etiquetas: misma categoría registrada con distinta puntuación o sintaxis.                                   |
| **District inválido**                        |         9         |            Error             | Inconsistencia en la carga: se utilizaron códigos de distritos no policiales.                                             |

# Análisis ML

Una problemática interesante para analizar sería detectar, dado un delito reportado, si el mismo terminará en un arresto o no. Esto puede ayudar a analizar que características de un delito son las más relevantes a la hora de que se produzca un arresto (y en qué casos y qué zonas hay una tasa más baja de resolción).
La variable target en este caso sería 'Arrest', una variable binaria. Sería un problema de clasificación dónde las categorías son: delito que terminó en arresto y delito que no terminó en arresto.

# Preprocesamiento (TODO, lo haría en notebook separado)

Eliminar columnas irrelevantes:
'Updated On': posterior al hecho
'ID' y 'Case Number': identificadores
'Year': redundante dado que es un valor constante
