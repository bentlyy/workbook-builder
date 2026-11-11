# -*- coding: utf-8 -*-
import os, html
BASE = r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS_DIR = os.path.join(BASE, "units")
os.makedirs(UNITS_DIR, exist_ok=True)

def e(s): return html.escape(str(s), quote=False)
def c(s): return f"<code>{e(s)}</code>"
def b(cls="md"): return f'<span class="blank {cls}"></span>'
def ln(): return '<span class="line"></span>'

def render_unit_html(u):
    out=[f'<section class="unit" id="u{u["n"]}">',f'<h2>Unidad {u["n"]}. {e(u["title"])}</h2>',f'<p class="context">{e(u["context"])}</p>']
    for i,ex in enumerate(u["exercises"],1):
        out.append('<div class="exercise">')
        out.append(f'<h3>Ejercicio {i}. {e(ex["title"])}</h3>')
        out.append(f'<p class="inst">{e(ex["inst"])}</p>')
        if ex.get("example"): out.append(f'<div class="example"><strong>Ejemplo:</strong> {ex["example"]}</div>')
        if ex.get("pre"): out.append(f'<pre>{e(ex["pre"])}</pre>')
        if ex.get("items"):
            out.append("<ol class='items'>")
            for it in ex["items"]: out.append(f"<li>{it}</li>")
            out.append("</ol>")
        if ex.get("lines"):
            for _ in range(ex["lines"]): out.append('<span class="line"></span>')
        out.append('</div>')
    out.append('</section>')
    return "\n".join(out)

def render_ans(u):
    out=[f'<p class="u">Unidad {u["n"]}. {e(u["title"])}</p>']
    for i,ex in enumerate(u["exercises"],1):
        ans = ex.get("ans",[]); ans = " ".join(str(a) for a in ans) if isinstance(ans,list) else str(ans)
        out.append(f'<p><strong>Ej. {i}:</strong> {e(ans)}</p>')
    return "\n".join(out)

u13 = {
"n":13,"title":"PostgreSQL y modelado relacional",
"context":"Una base de datos relacional bien modelada garantiza integridad, consistencia y rendimiento a medida que la aplicación crece. PostgreSQL ofrece tipos ricos, restricciones, índices y transacciones que, usados correctamente, evitan errores de datos difíciles de corregir después. Esta unidad practica diseño de tablas, claves primarias/foráneas, constraints, normalización básica e índices, con foco en escenarios típicos de sistemas SaaS y multi-tenant.",
"exercises":[
 {"title":"Completar: conceptos de modelado relacional","inst":"Completa con el término correcto.","example":"Ejemplo: Una clave primaria identifica de forma única cada fila de una tabla.",
  "items":[f"Una {b('md')} (PK) identifica un registro de manera única y no debe ser nula.",f"Una {b('md')} (FK) referencia la PK de otra tabla para asegurar integridad {b('md')}.",f"La restricción {c('NOT NULL')} impide valores nulos y {c('UNIQUE')} impide valores {b('md')}.",f"Una relación uno-a-muchos (1:N) se implementa colocando la FK en la tabla del lado {b('md')}.",f"Una relación muchos-a-muchos (N:M) requiere una tabla {b('md')} (junction).",f"La normalización busca reducir {b('md')} y anomalías de actualización/inserción/borrado."],
  "ans":["1) clave primaria 2) clave foránea / referencial 3) duplicados 4) muchos 5) intermedia 6) redundancia"]},
 {"title":"Completar: constraints, tipos e índices","inst":"Completa los conceptos.",
  "items":[f"{c('CHECK')} permite validar una condición a nivel de {b('md')} (ej. precio >= 0).",f"{c('DEFAULT')} asigna un valor {b('md')} cuando no se proporciona.",f"Un índice acelera búsquedas pero añade costo en {b('md')} (insert/update/delete).",f"Un índice compuesto sobre {c('(tenant_id, created_at)')} beneficia consultas que filtran por {b('lg')}.",f"Usar {c('timestamptz')} para fechas con zona evita problemas de {b('md')}.",f"{c('ON DELETE CASCADE')} elimina filas hijas al borrar el {b('md')} (usar con cuidado)."],
  "ans":["1) columna/tabla 2) por defecto 3) escrituras 4) tenant_id y fecha 5) zonas horarias 6) padre"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Usar texto libre sin FK para relacionar tablas con relación clara. → {ln()}",f"Guardar fechas como varchar en formatos inconsistentes. → {ln()}",f"Definir PK compuesta o surrogate key según necesidades del modelo. → {ln()}",f"No indexar columnas usadas frecuentemente en filtros/joins. → {ln()}",f"Permitir que todas las columnas sean NULL sin necesidad. → {ln()}",f"Usar transacciones para operaciones que deben ser atómicas. → {ln()}"],
  "ans":["a) Error b) Error c) Correcto d) Omisión riesgosa e) Mala práctica f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Usuario-pedidos: ({c('1:N')} / {c('N:M')} / {c('1:1')}).",f"Productos-etiquetas: ({c('1:N')} / {c('N:M con tabla intermedia')}).",f"Email único por tenant: ({c('UNIQUE(email)')} global / {c('UNIQUE(tenant_id,email)')}).",f"Dinero: ({c('float')} / {c('numeric/decimal')}).",f"Borrado lógico: ({c('deleted_at/active')} / {c('hard delete siempre')}).",f"Consulta por {c('tenant_id')} y fecha: índice ({c('(tenant_id, created_at)')} / {c('(description)')})."],
  "ans":["1) 1:N 2) N:M 3) UNIQUE(tenant_id,email) 4) numeric 5) deleted_at 6) (tenant_id, created_at)"]},
 {"title":"Elegir/decisión de diseño","inst":"Selecciona la mejor decisión.",
  "items":[f"Auditoría: ({c('no registrar')} / {c('timestamps/actor/tabla auditoría')}).",f"IDs públicos: ({c('considerar UUID/seguros')} / {c('asumir secuencial siempre')}).",f"Multi-tenant: ({c('tenant_id + aislamiento')} / {c('mezclar sin tenant')}).",f"Cascadas: ({c('con criterio')} / {c('CASCADE en todo')}).",f"JSON en PG: ({c('jsonb cuando aporta')} / {c('para todo')}).",f"Migraciones: ({c('versionadas')} / {c('manuales ad-hoc')})."],
  "ans":["1) auditoría 2) considerar según caso 3) tenant_id + aislamiento 4) con criterio 5) jsonb cuando aporta 6) versionadas"]},
 {"title":"Transformar: mejorar modelo","inst":"Transforma según se indique.",
  "pre":"CREATE TABLE orders (\n  id serial,\n  user_email text,\n  total float,\n  created text\n);",
  "items":[f"Añade PK y tipos adecuados. {ln()}{ln()}",f"Relaciona con users mediante user_id FK. {ln()}",f"Añade CHECK total >= 0. {ln()}",f"Índice para (user_id, created_at). {ln()}",f"Normaliza email repetido: {ln()}",f"Añade tenant_id para multi-tenant: {ln()}"],
  "ans":["1) id PK, numeric, timestamptz 2) user_id FK 3) CHECK(total>=0) 4) CREATE INDEX 5) tabla users + FK 6) tenant_id y constraints/índices"]},
 {"title":"Reordenar/relacionar: diseño y consultas","inst":"Ordena o relaciona.",
  "items":[f"Diseño: (a) entidades (b) relaciones (c) constraints/índices (d) validar casos. → {ln()}",f"1)PK 2)FK 3)UNIQUE 4)CHECK con A)regla B)unicidad C)identidad D)referencia. → {ln()}",f"1)1:N 2)N:M 3)1:1 con A)intermedia B)FK lado N C)FK única. → {ln()}",f"Normalización: (a) detectar redundancia (b) separar (c) claves (d) revisar. → {ln()}",f"1)índice 2)transacción 3)constraint con A)integridad B)atomicidad C)lectura. → {ln()}",f"Consulta segura: (a) parámetros (b) ejecutar (c) manejar (d) recursos. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-C,2-D,3-B,4-A 3) 1-B,2-A,3-C 4) a,b,c,d 5) 1-C,2-B,3-A 6) a,b,c,d"]},
 {"title":"Escenario: base de datos para SaaS de gestión clínica","inst":"Responde al escenario.","example":"Escenario: modelo para tenants (clínicas), pacientes, citas y profesionales. Aislamiento por clínica, búsquedas por fecha/paciente e historial consistente.",
  "items":[f"Entidades principales y relaciones (4): {ln()}{ln()}",f"Cómo garantizas aislamiento por tenant: {ln()}",f"Restricción para evitar doble cita de un profesional (idea): {ln()}{ln()}",f"Índices probables para agenda diaria: {ln()}",f"Consideración para diagnóstico sensible: {ln()}{ln()}",f"Estrategia de borrado con historial: {ln()}"],
  "ans":["1) tenants,patients,professionals,appointments 2) tenant_id + filtros/constraints 3) unique(professional_id,start_time) 4) (tenant_id,date) 5) controles acceso/cifrado/cumplimiento 6) soft delete"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"DDL simplificado tenants y users con FK y unique por tenant. {ln()}{ln()}{ln()}{ln()}",f"Índice para (tenant_id,email): {ln()}",f"3 reglas de modelado por defecto. {ln()}{ln()}{ln()}"],
  "ans":["1) PKs, FK tenant_id, UNIQUE(tenant_id,email) 2) índice/constraint compuesto 3) integridad, tipos adecuados, migraciones versionadas"]
  }
]
}

u14 = {
"n":14,"title":"SQL práctico y Prisma ORM",
"context":"Consultar y modificar datos correctamente es tan importante como modelarlos bien. SQL permite expresar consultas precisas, agregaciones y transacciones, mientras que un ORM como Prisma aporta productividad y tipado en aplicaciones TypeScript. Esta unidad practica SELECT/JOIN/WHERE, agregaciones, transacciones y patrones de uso seguro de Prisma en servicios backend.",
"exercises":[
 {"title":"Completar: consultas SQL básicas","inst":"Completa con la cláusula o concepto correcto.","example":"Ejemplo: SELECT filtra columnas y WHERE filtra filas.",
  "items":[f"Filtrar filas: {b('sm')} ; ordenar: {b('lg')}.",f"Paginación offset: {b('sm')} y {b('sm')}.",f"{c('LEFT JOIN')} devuelve todas las filas de la tabla {b('md')}.",f"Contar: {c('COUNT(*)')} ; agrupar: {b('sm')}.",f"Filtrar agregaciones: {b('sm')} (no WHERE).",f"Consultas parametrizadas evitan inyección {b('md')}."],
  "ans":["1) WHERE/ORDER BY 2) LIMIT/OFFSET 3) izquierda 4) GROUP BY 5) HAVING 6) SQL"]},
 {"title":"Completar: transacciones y Prisma","inst":"Completa los conceptos.",
  "items":[f"Transacción: operaciones {b('md')} (todo o nada).",f"{c('prisma.$transaction')} ejecuta operaciones de forma {b('md')}.",f"{c('schema.prisma')} define modelos, campos y {b('md')}.",f"{c('findMany')} soporta where, orderBy, take y {b('sm')}.",f"{c('select')}/{c('include')} controlan qué se {b('md')}.",f"Migraciones versionan cambios del {b('md')}."],
  "ans":["1) atómicas 2) transaccional 3) relaciones 4) skip 5) retorna 6) esquema/BD"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Concatenar input en SQL: {c('`... ${id}`')}. → {ln()}",f"Usar transacción para débito y crédito juntos. → {ln()}",f"{c('SELECT *')} siempre en alto tráfico. → {ln()}",f"{c('findUnique')} por campo unique. → {ln()}",f"Ignorar error de constraint única y devolver éxito. → {ln()}",f"{c('include')} indiscriminado de relaciones grandes. → {ln()}"],
  "ans":["a) Error b) Correcto c) Mala práctica d) Correcto e) Error f) Mala práctica"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Un registro por id único: ({c('findUnique')} / {c('findMany')}).",f"Actualizar varios: ({c('updateMany')} / {c('update')}).",f"OR de condiciones: ({c('where:{OR:[...]}')} / {c('OR sin array')}).",f"Conteo: ({c('count')} / {c('sum')}).",f"Paginación grandes tablas: ({c('cursor a menudo')} / {c('offset enorme siempre')}).",f"Crear y retornar: ({c('create')} / {c('delete')})."],
  "ans":["1) findUnique 2) updateMany 3) OR array 4) count 5) cursor 6) create"]},
 {"title":"Elegir/decisión de acceso a datos","inst":"Selecciona la mejor decisión.",
  "items":[f"Consulta repetida: ({c('extraer a repo')} / {c('duplicar')}).",f"Cargar relación: ({c('select/include específico')} / {c('todo')}).",f"Operación crítica multi-paso: ({c('transacción')} / {c('suelta')}).",f"No encontrado: ({c('controlar caso')} / {c('ignorar')}).",f"Concurrencia en stock: ({c('transacción/condición')} / {c('sin control')}).",f"Conexiones: ({c('configurar pool')} / {c('ignorar')})."],
  "ans":["1) extraer 2) específico 3) transacción 4) controlar 5) control concurrencia 6) configurar"]},
 {"title":"Transformar: consultas seguras","inst":"Transforma según se indique.",
  "items":[f"SQL concatenado → parametrizado: {ln()}{ln()}",f"Prisma: órdenes de tenant paginadas desc: {ln()}{ln()}",f"Añadir filtro status paid: {ln()}",f"Crear user y profile en transacción: {ln()}{ln()}",f"Select solo id,email: {ln()}",f"Idea para evitar stock negativo: {ln()}{ln()}"],
  "ans":["1) parámetros/placeholders 2) findMany where/orderBy/take/skip 3) where:{status:'paid'} 4) $transaction([...]) 5) select:{id:true,email:true} 6) transacción+condición/lock"]},
 {"title":"Reordenar/relacionar: consulta y transacción","inst":"Ordena o relaciona.",
  "items":[f"Paginada: (a) validar (b) where (c) order/take/skip (d) meta. → {ln()}",f"1)WHERE 2)JOIN 3)GROUP BY 4)HAVING con A)agrupa B)agregada C)filtra D)combina. → {ln()}",f"Tx: (a) iniciar (b) ops (c) commit/rollback (d) error. → {ln()}",f"1)findUnique 2)findMany 3)update 4)delete con A)lista B)borra C)uno D)modifica. → {ln()}",f"1)N+1 2)overfetch 3)inyección con A)de más B)repetidas C)inseguro. → {ln()}",f"Optimizar: (a) medir (b) índices (c) ajustar select (d) verificar. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-C,2-D,3-A,4-B 3) a,b,c,d 4) 1-C,2-A,3-D,4-B 5) 1-B,2-A,3-C 6) a,b,c,d"]},
 {"title":"Escenario: reportes y actualización de stock","inst":"Responde al escenario.","example":"Escenario: reportes de ventas por tenant y actualización de stock al confirmar órdenes. Hay consultas lentas y stock negativo por concurrencia.",
  "items":[f"Consulta conceptual ventas por día/tenant: {ln()}{ln()}",f"Índice útil para reporte: {ln()}",f"Cómo evitar stock negativo concurrente: {ln()}{ln()}",f"Resultado sin filas: {ln()}",f"Riesgo de N+1 al listar órdenes con items: {ln()}",f"2 prácticas seguras con Prisma: {ln()}{ln()}"],
  "ans":["1) group by fecha sum total 2) (tenant_id,created_at) 3) transacción y condición atómica 4) 200 array vacío 5) consultas repetidas; include/select adecuado 6) select acotado, parametrizado, repositorios"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Prisma: 10 últimas órdenes de tenant con id,total,createdAt. {ln()}{ln()}{ln()}",f"SQL parametrizado buscar usuario por email y tenant: {ln()}",f"3 reglas de acceso a datos en producción. {ln()}{ln()}{ln()}"],
  "ans":["1) findMany({where:{tenantId},orderBy:{createdAt:'desc'},take:10,select:{id:true,total:true,createdAt:true}}) 2) WHERE email=$1 AND tenant_id=$2 3) parametrizar, transacciones críticas, índices"]
  }
]
}

if __name__ == "__main__":
    for u in [u13,u14]:
        frag = render_unit_html(u); ans = render_ans(u)
        open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
        open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
        print(u['n'], len(frag), len(ans))
