"""
Generate all simulated datasets for Formacion Docente BI - FACES UC.
Run: python scripts/generate_datasets.py
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

np.random.seed(42)

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'datasets')

CARRERAS = ['Economia', 'Administracion', 'Contaduria', 'Relaciones Industriales']
DEPARTAMENTOS = ['Economia', 'Administracion', 'Contaduria', 'Relaciones Industriales', 'Matematica', 'Estadistica']
PERIODOS = [f"{y}-{s}" for y in range(2015, 2026) for s in ['I', 'II']]
PAISES_LATAM = ['Venezuela', 'Colombia', 'Brasil', 'Argentina', 'Chile', 'Peru', 'Mexico', 'Ecuador', 'Bolivia', 'Uruguay']

# ============================================================
# 1. UNIVERSIDAD
# ============================================================

def gen_matricula_faces():
    """~2000 rows: enrollment data by career, period, gender."""
    rows = []
    for periodo in PERIODOS:
        year = int(periodo.split('-')[0])
        for carrera in CARRERAS:
            base = {'Economia': 90, 'Administracion': 120, 'Contaduria': 100, 'Relaciones Industriales': 70}[carrera]
            # Declining trend post-2017 (Venezuelan crisis)
            if year >= 2018:
                base = int(base * max(0.4, 1 - 0.08 * (year - 2017)))
            n = np.random.poisson(base)
            for _ in range(n):
                genero = np.random.choice(['F', 'M'], p=[0.58, 0.42])
                edad = int(np.clip(np.random.normal(20 if year < 2018 else 22, 3), 17, 45))
                tipo_ingreso = np.random.choice(['Regular', 'Equivalencia', 'Reingreso'], p=[0.80, 0.12, 0.08])
                sede = np.random.choice(['Barbula', 'La Morita'], p=[0.72, 0.28])
                # Higher dropout post-crisis
                if year >= 2018:
                    estatus = np.random.choice(['Activo', 'Retirado', 'Egresado'], p=[0.55, 0.35, 0.10])
                else:
                    estatus = np.random.choice(['Activo', 'Retirado', 'Egresado'], p=[0.70, 0.15, 0.15])
                rows.append({
                    'periodo': periodo,
                    'carrera': carrera,
                    'genero': genero,
                    'edad': edad,
                    'tipo_ingreso': tipo_ingreso,
                    'sede': sede,
                    'estatus': estatus,
                })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'universidad', 'matricula_faces.csv'), index=False)
    print(f"  matricula_faces.csv: {len(df)} rows")
    return df


def gen_rendimiento_academico():
    """~3000 rows: academic performance with sociodemographic factors."""
    rows = []
    for i in range(3000):
        carrera = np.random.choice(CARRERAS, p=[0.25, 0.30, 0.25, 0.20])
        semestre = np.random.randint(1, 11)
        genero = np.random.choice(['F', 'M'], p=[0.58, 0.42])
        edad = int(np.clip(np.random.normal(20 + semestre * 0.5, 2.5), 17, 40))
        trabaja = np.random.choice([True, False], p=[0.45, 0.55])
        beca = np.random.choice([True, False], p=[0.15, 0.85])

        # GPA influenced by factors
        base_promedio = np.random.normal(13.5, 2.5)
        if trabaja:
            base_promedio -= np.random.uniform(0.5, 1.5)
        if beca:
            base_promedio += np.random.uniform(0.3, 1.0)
        if semestre > 6:
            base_promedio += 0.5  # survivors bias
        promedio = round(np.clip(base_promedio, 5.0, 20.0), 1)

        materias_inscritas = np.random.randint(4, 8)
        tasa_aprobacion = np.clip(0.5 + (promedio - 10) * 0.05, 0.2, 1.0)
        materias_aprobadas = int(np.clip(np.random.binomial(materias_inscritas, tasa_aprobacion), 0, materias_inscritas))
        materias_reprobadas = materias_inscritas - materias_aprobadas

        asistencia_pct = round(np.clip(np.random.normal(75 if trabaja else 85, 12), 30, 100), 1)

        rows.append({
            'estudiante_id': f"EST-{i+1:04d}",
            'carrera': carrera,
            'semestre': semestre,
            'genero': genero,
            'edad': edad,
            'promedio': promedio,
            'materias_inscritas': materias_inscritas,
            'materias_aprobadas': materias_aprobadas,
            'materias_reprobadas': materias_reprobadas,
            'asistencia_pct': asistencia_pct,
            'beca': beca,
            'trabaja': trabaja,
        })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'universidad', 'rendimiento_academico.csv'), index=False)
    print(f"  rendimiento_academico.csv: {len(df)} rows")
    return df


def gen_presupuesto_facultad():
    """~120 rows: monthly budget execution time series."""
    rows = []
    partidas = ['Personal', 'Materiales', 'Servicios', 'Equipos', 'Mantenimiento']
    for year in range(2015, 2026):
        for month in range(1, 13):
            for partida in partidas:
                base = {'Personal': 800000, 'Materiales': 150000, 'Servicios': 120000,
                        'Equipos': 200000, 'Mantenimiento': 100000}[partida]
                # Hyperinflation effect post-2017 (simplified, values in "adjusted" units)
                if year >= 2018:
                    base = base * max(0.3, 1 - 0.1 * (year - 2017))
                presupuestado = round(base * np.random.uniform(0.9, 1.1), 2)
                # Execution rate drops during crisis
                exec_rate = np.clip(np.random.normal(0.85 if year < 2018 else 0.60, 0.15), 0.2, 1.0)
                ejecutado = round(presupuestado * exec_rate, 2)
                fuente = np.random.choice(['Ordinario', 'Propio', 'Especial'], p=[0.65, 0.25, 0.10])
                rows.append({
                    'anio': year,
                    'mes': month,
                    'partida': partida,
                    'presupuestado': presupuestado,
                    'ejecutado': ejecutado,
                    'fuente': fuente,
                })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'universidad', 'presupuesto_facultad.csv'), index=False)
    print(f"  presupuesto_facultad.csv: {len(df)} rows")
    return df


def gen_encuesta_docente():
    """~200 rows: faculty survey on job satisfaction and profile."""
    rows = []
    for i in range(200):
        depto = np.random.choice(DEPARTAMENTOS)
        antiguedad = int(np.clip(np.random.exponential(12), 1, 40))
        dedicacion = np.random.choice(['Tiempo Completo', 'Medio Tiempo', 'Contratado'],
                                       p=[0.45, 0.30, 0.25])
        genero = np.random.choice(['F', 'M'], p=[0.52, 0.48])
        edad = int(np.clip(np.random.normal(45, 10), 28, 72))
        formacion = np.random.choice(['Licenciatura', 'Maestria', 'Doctorado', 'Especialidad'],
                                      p=[0.15, 0.45, 0.25, 0.15])

        # Satisfaction scores (1-5 Likert)
        base_sat = np.random.normal(3.2, 0.8)
        if dedicacion == 'Tiempo Completo':
            base_sat += 0.3
        if antiguedad > 20:
            base_sat -= 0.2

        sat_general = int(np.clip(round(base_sat + np.random.normal(0, 0.5)), 1, 5))
        sat_salarial = int(np.clip(round(base_sat - 0.8 + np.random.normal(0, 0.5)), 1, 5))
        sat_infraestructura = int(np.clip(round(base_sat - 0.5 + np.random.normal(0, 0.5)), 1, 5))
        sat_desarrollo = int(np.clip(round(base_sat + 0.2 + np.random.normal(0, 0.5)), 1, 5))

        publicaciones = int(np.clip(np.random.poisson(3 if formacion in ['Doctorado', 'Maestria'] else 1), 0, 30))
        carga_horaria = int(np.clip(np.random.normal(16 if dedicacion == 'Tiempo Completo' else 10, 4), 4, 30))

        rows.append({
            'docente_id': f"DOC-{i+1:03d}",
            'departamento': depto,
            'genero': genero,
            'edad': edad,
            'antiguedad': antiguedad,
            'dedicacion': dedicacion,
            'formacion': formacion,
            'satisfaccion_general': sat_general,
            'satisfaccion_salarial': sat_salarial,
            'satisfaccion_infraestructura': sat_infraestructura,
            'satisfaccion_desarrollo': sat_desarrollo,
            'publicaciones': publicaciones,
            'carga_horaria': carga_horaria,
        })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'universidad', 'encuesta_docente.csv'), index=False)
    print(f"  encuesta_docente.csv: {len(df)} rows")
    return df


# ============================================================
# 2. ECONOMIA
# ============================================================

def gen_indicadores_bcv():
    """~120 rows: monthly macroeconomic indicators (simplified/adjusted)."""
    rows = []
    for year in range(2015, 2026):
        for month in range(1, 13):
            # Simplified indicators (in adjusted units to be plottable)
            t = (year - 2015) * 12 + month

            # Inflation: low 2015-2016, explosive 2017-2021, stabilizing 2022+
            if year <= 2016:
                inflacion = round(np.random.uniform(3, 8), 1)
            elif year <= 2021:
                inflacion = round(np.random.uniform(15, 50) * (1 + 0.3 * (year - 2017)), 1)
            else:
                inflacion = round(np.random.uniform(5, 20), 1)

            # Exchange rate (indexed, base 2015=1)
            if year <= 2017:
                tipo_cambio = round(1.0 + (t / 36) * np.random.uniform(0.8, 1.2), 2)
            else:
                tipo_cambio = round(5 + (year - 2018) * 3 + np.random.normal(0, 1), 2)

            # Monetary liquidity (index)
            liquidez = round(100 + t * 8 + np.random.normal(0, 20), 1)

            # International reserves (billions USD)
            reservas = round(np.clip(20 - (year - 2015) * 1.5 + np.random.normal(0, 1), 5, 25), 1)

            # GDP quarterly (only generate for months 3, 6, 9, 12)
            pib_trimestral = None
            if month in [3, 6, 9, 12]:
                base_pib = 80 if year <= 2017 else max(40, 80 - (year - 2017) * 6)
                pib_trimestral = round(base_pib + np.random.normal(0, 3), 1)

            rows.append({
                'fecha': f"{year}-{month:02d}-01",
                'inflacion_mensual': inflacion,
                'tipo_cambio_indice': tipo_cambio,
                'liquidez_monetaria_indice': liquidez,
                'reservas_internacionales_mmusd': reservas,
                'pib_trimestral_indice': pib_trimestral,
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'economia', 'indicadores_bcv.csv'), index=False)
    print(f"  indicadores_bcv.csv: {len(df)} rows")
    return df


def gen_inflacion_latam():
    """~300 rows: annual inflation comparison across LATAM countries."""
    rows = []
    # Base inflation ranges by country (approximate)
    country_params = {
        'Venezuela': (50, 30), 'Argentina': (25, 15), 'Brasil': (5, 2),
        'Colombia': (4, 1.5), 'Chile': (3, 1), 'Peru': (3, 1),
        'Mexico': (4, 1.5), 'Ecuador': (2, 1), 'Bolivia': (3, 1.5),
        'Uruguay': (8, 2),
    }
    pib_base = {
        'Venezuela': 12000, 'Argentina': 10000, 'Brasil': 9000,
        'Colombia': 6500, 'Chile': 15000, 'Peru': 7000,
        'Mexico': 10000, 'Ecuador': 6000, 'Bolivia': 3500,
        'Uruguay': 17000,
    }
    for year in range(2000, 2026):
        for pais in PAISES_LATAM:
            base, std = country_params[pais]
            if pais == 'Venezuela' and year >= 2017:
                inflacion = round(np.clip(np.random.normal(base * (1 + (year - 2017) * 2), std * 5), 20, 1000), 1)
            elif pais == 'Argentina' and year >= 2018:
                inflacion = round(np.clip(np.random.normal(base * 2, std), 15, 150), 1)
            else:
                inflacion = round(np.clip(np.random.normal(base, std), 0.5, 200), 1)

            pib_pc = round(pib_base[pais] * (1 + (year - 2000) * 0.02) + np.random.normal(0, 500), 0)
            if pais == 'Venezuela' and year >= 2015:
                pib_pc = round(pib_base[pais] * max(0.3, 1 - (year - 2015) * 0.08) + np.random.normal(0, 300), 0)

            desempleo = round(np.clip(np.random.normal(8, 3), 2, 35), 1)
            if pais == 'Venezuela' and year >= 2016:
                desempleo = round(np.clip(np.random.normal(15 + (year - 2016) * 2, 3), 8, 40), 1)

            rows.append({
                'pais': pais,
                'anio': year,
                'inflacion_anual': inflacion,
                'pib_per_capita_usd': int(pib_pc),
                'desempleo_pct': desempleo,
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'economia', 'inflacion_latam.csv'), index=False)
    print(f"  inflacion_latam.csv: {len(df)} rows")
    return df


def gen_comercio_exterior():
    """~500 rows: monthly trade data by product and destination."""
    productos = ['Petroleo', 'Minerales', 'Agricultura', 'Manufactura', 'Quimicos']
    paises_destino = ['China', 'India', 'Estados Unidos', 'Colombia', 'Brasil', 'Turquia', 'Espana', 'Italia']
    rows = []
    for year in range(2015, 2026):
        for month in range(1, 13):
            # ~4 entries per month
            n_entries = np.random.randint(3, 6)
            for _ in range(n_entries):
                producto = np.random.choice(productos, p=[0.55, 0.12, 0.10, 0.13, 0.10])
                pais = np.random.choice(paises_destino)

                # Oil dominates exports, declining over time
                if producto == 'Petroleo':
                    base_valor = np.random.uniform(500, 2000)
                    if year >= 2017:
                        base_valor *= max(0.3, 1 - 0.1 * (year - 2017))
                else:
                    base_valor = np.random.uniform(20, 200)

                valor_fob = round(base_valor * np.random.uniform(0.8, 1.2), 2)
                volumen = round(valor_fob * np.random.uniform(0.5, 2.0), 1)

                rows.append({
                    'anio': year,
                    'mes': month,
                    'pais_destino': pais,
                    'producto': producto,
                    'valor_fob_musd': valor_fob,
                    'volumen_miles_tm': volumen,
                })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'economia', 'comercio_exterior.csv'), index=False)
    print(f"  comercio_exterior.csv: {len(df)} rows")
    return df


# ============================================================
# 3. EMPRESARIAL
# ============================================================

def gen_ventas_retail():
    """~5000 rows: daily retail sales over 2 years."""
    categorias = ['Alimentos', 'Bebidas', 'Limpieza', 'Cuidado Personal', 'Electronica', 'Hogar']
    tiendas = [f"Tienda-{i:02d}" for i in range(1, 11)]
    regiones = ['Central', 'Occidente', 'Oriente', 'Andes', 'Capital']
    tienda_region = {t: np.random.choice(regiones) for t in tiendas}

    rows = []
    start = datetime(2023, 1, 1)
    for day in range(730):  # 2 years
        date = start + timedelta(days=day)
        # ~7 transactions per day
        n_trans = np.random.poisson(7)
        for _ in range(n_trans):
            tienda = np.random.choice(tiendas)
            categoria = np.random.choice(categorias, p=[0.30, 0.15, 0.15, 0.12, 0.13, 0.15])

            base_price = {'Alimentos': 15, 'Bebidas': 8, 'Limpieza': 12,
                          'Cuidado Personal': 18, 'Electronica': 150, 'Hogar': 45}[categoria]
            cantidad = np.random.randint(1, 10) if categoria != 'Electronica' else np.random.randint(1, 3)

            # Weekend boost
            if date.weekday() >= 5:
                cantidad = int(cantidad * 1.3)

            # Seasonal: December boost
            if date.month == 12:
                cantidad = int(cantidad * 1.5)

            ingreso = round(base_price * cantidad * np.random.uniform(0.9, 1.1), 2)
            margen = np.random.uniform(0.15, 0.40)
            costo = round(ingreso * (1 - margen), 2)

            rows.append({
                'fecha': date.strftime('%Y-%m-%d'),
                'tienda': tienda,
                'region': tienda_region[tienda],
                'categoria': categoria,
                'cantidad': cantidad,
                'ingreso': ingreso,
                'costo': costo,
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'empresarial', 'ventas_retail.csv'), index=False)
    print(f"  ventas_retail.csv: {len(df)} rows")
    return df


def gen_rrhh_nomina():
    """~500 rows: HR/payroll data."""
    departamentos_emp = ['Ventas', 'Produccion', 'Administracion', 'RRHH', 'Logistica', 'TI', 'Finanzas']
    cargos = {
        'Ventas': ['Ejecutivo', 'Supervisor', 'Gerente'],
        'Produccion': ['Operario', 'Supervisor', 'Jefe de Planta'],
        'Administracion': ['Asistente', 'Coordinador', 'Gerente'],
        'RRHH': ['Analista', 'Coordinador', 'Gerente'],
        'Logistica': ['Almacenista', 'Coordinador', 'Gerente'],
        'TI': ['Desarrollador', 'Analista', 'Gerente'],
        'Finanzas': ['Contador', 'Analista', 'Gerente'],
    }
    rows = []
    for i in range(500):
        depto = np.random.choice(departamentos_emp)
        cargo = np.random.choice(cargos[depto])
        genero = np.random.choice(['F', 'M'], p=[0.48, 0.52])
        edad = int(np.clip(np.random.normal(38, 10), 22, 65))
        antiguedad = int(np.clip(np.random.exponential(6), 0, min(35, edad - 22)))

        # Salary based on cargo level
        nivel = cargos[depto].index(cargo)
        base_salario = 800 + nivel * 600 + antiguedad * 30
        salario = round(base_salario * np.random.uniform(0.9, 1.15), 2)

        evaluacion = round(np.clip(np.random.normal(3.5 + nivel * 0.3, 0.7), 1, 5), 1)
        ausencias = int(np.clip(np.random.poisson(3 if evaluacion < 3 else 1), 0, 20))

        rows.append({
            'empleado_id': f"EMP-{i+1:04d}",
            'departamento': depto,
            'cargo': cargo,
            'genero': genero,
            'edad': edad,
            'antiguedad': antiguedad,
            'salario_mensual_usd': salario,
            'evaluacion_desempeno': evaluacion,
            'ausencias_anuales': ausencias,
        })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'empresarial', 'rrhh_nomina.csv'), index=False)
    print(f"  rrhh_nomina.csv: {len(df)} rows")
    return df


def gen_estados_financieros():
    """~200 rows: simulated company financial statements."""
    sectores = ['Manufactura', 'Comercio', 'Servicios', 'Alimentos', 'Construccion']
    rows = []
    n_empresas = 20
    for emp_id in range(1, n_empresas + 1):
        sector = np.random.choice(sectores)
        for year in range(2015, 2026):
            # Size based on sector
            base_activos = np.random.uniform(5000, 50000)
            growth = 1 + np.random.normal(0.03, 0.05)
            if year >= 2017:
                growth *= max(0.7, 1 - 0.03 * (year - 2017))  # crisis effect

            activos = round(base_activos * growth ** (year - 2015), 2)
            ratio_deuda = np.clip(np.random.normal(0.45, 0.15), 0.1, 0.85)
            pasivos = round(activos * ratio_deuda, 2)
            patrimonio = round(activos - pasivos, 2)

            ingresos = round(activos * np.random.uniform(0.6, 1.5), 2)
            margen = np.clip(np.random.normal(0.25, 0.10), 0.05, 0.50)
            costos = round(ingresos * (1 - margen), 2)
            utilidad = round(ingresos - costos, 2)

            rows.append({
                'empresa_id': f"CIA-{emp_id:03d}",
                'anio': year,
                'sector': sector,
                'activos_musd': activos,
                'pasivos_musd': pasivos,
                'patrimonio_musd': patrimonio,
                'ingresos_musd': ingresos,
                'costos_musd': costos,
                'utilidad_neta_musd': utilidad,
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(BASE_DIR, 'empresarial', 'estados_financieros.csv'), index=False)
    print(f"  estados_financieros.csv: {len(df)} rows")
    return df


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print("Generating datasets...\n")

    print("[Universidad]")
    gen_matricula_faces()
    gen_rendimiento_academico()
    gen_presupuesto_facultad()
    gen_encuesta_docente()

    print("\n[Economia]")
    gen_indicadores_bcv()
    gen_inflacion_latam()
    gen_comercio_exterior()

    print("\n[Empresarial]")
    gen_ventas_retail()
    gen_rrhh_nomina()
    gen_estados_financieros()

    print("\nDone! All datasets generated.")
