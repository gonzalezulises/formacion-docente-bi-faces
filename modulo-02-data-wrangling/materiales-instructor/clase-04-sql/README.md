# Clase 4 — Consultas SQL

> Materiales originales entregados por el instructor **Gabriel Gómez**.

## Archivos incluidos

| Archivo | Tipo | Uso |
|---------|------|-----|
| [`consultas_sql.docx`](consultas_sql.docx) | Documento | Guía de consultas + ejercicios |

Base de datos sugerida: **Northwind / W3Schools Northwind** (tablas `products`, `orderdetails`, `customers`, `orders`, `employees`, `shippers`). Puedes practicar en: https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

## Ejemplos guía

### 1. Nombre de producto, precio y cantidad (LEFT JOIN con subquery)

```sql
SELECT a.ProductName,
       a.Price,
       b.quantity
FROM products AS a
LEFT JOIN (
    SELECT quantity, ProductID
    FROM orderdetails
) AS b
  ON a.ProductID = b.ProductID;
```

### 2. Total a pagar por producto (SUM + GROUP BY)

```sql
SELECT a.ProductName,
       SUM(a.Price * b.quantity) AS 'Total'
FROM products AS a
LEFT JOIN orderdetails AS b
  ON a.ProductID = b.ProductID
GROUP BY a.ProductName;
```

### 3. Mismo total filtrando con HAVING

```sql
SELECT a.ProductName,
       SUM(a.Price * b.quantity) AS 'Total'
FROM products AS a
LEFT JOIN orderdetails AS b
  ON a.ProductID = b.ProductID
GROUP BY a.ProductName
HAVING SUM(a.Price * b.quantity) > 2000;
```

### 4. INSERT y UPDATE

```sql
-- Insertar un cliente nuevo
INSERT INTO customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('9', 'Paola Smith', 'Pau', 'Colinas del Sol', 'Masaya', 10147, 'Nic');

-- Actualizar nombre
UPDATE customers
SET CustomerName = 'Y Perez'
WHERE CustomerName = 'Oswaldo';
```

### 5. CTE (`WITH`) como subquery con nombre

```sql
WITH sales AS (
    SELECT od.ProductID,
           SUM(od.quantity) AS total_quantity
    FROM orderdetails od
    GROUP BY od.ProductID
)
SELECT p.ProductName,
       p.Price * s.total_quantity AS Total
FROM products p
LEFT JOIN sales s
  ON p.ProductID = s.ProductID
WHERE p.Price * s.total_quantity > 2000;
```

---

## Parte 1 — Ejercicios a resolver

1. Seleccionar **nombre del cliente**, **fecha de la orden** y **país del cliente**.
2. Seleccionar **nombre de empleado** y **fecha de orden**, ordenando de forma descendente.
3. Mostrar los **países que tienen más de 5 clientes**.
4. Mostrar **todos los clientes y sus órdenes**, aunque no tengan órdenes.
5. Mostrar todos los **envíos y su empresa transportista**.
6. Crear una lista de **órdenes por empleado**.
7. Mostrar nombre del cliente y cantidad de órdenes, **solo clientes con más de 2 órdenes**.

## Parte 2 — Corregir las siguientes consultas

### Query 1 (sintaxis / espacios faltantes)

```sql
SELECT CustomerName, OrderDateFROM Customers cJOIN Orders o
```

### Query 2 (falta GROUP BY)

```sql
SELECT Country, COUNT(*)FROM Customers
```

### Query 3 (orden incorrecto: WHERE antes de GROUP BY; debe ser HAVING)

```sql
SELECT Country, COUNT(*)
FROM Customers
GROUP BY Country
WHERE COUNT(*) > 5
```

### Query 4 (CTE sin GROUP BY)

```sql
WITH ordenes_cliente AS (
  SELECT CustomerID, COUNT(*) total
  FROM Orders
)
SELECT * FROM ordenes_cliente
```

---

Mapeo al notebook del repo: [`notebooks/02_03_sql_introductorio.ipynb`](../../notebooks/02_03_sql_introductorio.ipynb) y laboratorios [`lab_05_sql_ejercicios.ipynb`](../../laboratorios/lab_05_sql_ejercicios.ipynb) / [`lab_05_sql_soluciones.ipynb`](../../laboratorios/lab_05_sql_soluciones.ipynb).
