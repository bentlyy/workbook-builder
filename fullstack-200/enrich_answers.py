import os
base=r'C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200\units'
for i in range(1,21):
    p=os.path.join(base,f'u{i:02d}_ans.html')
    s=open(p,encoding='utf-8').read()
    if 'Guía de corrección detallada' in s:
        continue
    extra = (
        f'\n<div class="ans-detail"><p><strong>Guía de corrección detallada U{i}:</strong></p>\n<ul>\n'
        '<li><strong>Completar/transformar:</strong> aceptar sinónimos técnicos correctos y variantes equivalentes (sintaxis, orden, comillas) si respetan semántica, tipos y seguridad.</li>\n'
        '<li><strong>Corregir:</strong> identificar error + causa + arreglo válido; "Correcto" solo si no hay fallo. Valorar explicación breve.</li>\n'
        '<li><strong>Elegir:</strong> además de la opción, reconocer por qué los distractores fallan (seguridad, contrato, consistencia, rendimiento).</li>\n'
        '<li><strong>Escenarios/casos/RCA:</strong> incluir contexto y supuestos, ≥3 hallazgos/riesgos con causa y evidencia, decisiones con trade-offs, pasos ordenados, verificación (tests/métricas/logs) y mitigación/rollback.</li>\n'
        '<li><strong>Producción/diseño:</strong> contrato claro (entradas/salidas/errores), manejo de bordes y errores, seguridad (authn/authz, validación, secretos, tenant), observabilidad y criterios de aceptación medibles.</li>\n'
        '<li><strong>Rúbrica (0-2):</strong> corrección técnica, seguridad y manejo de bordes, calidad de pruebas/verificación, claridad y operabilidad. 0=incorrecto, 1=parcial, 2=correcto y justificado.</li>\n'
        '</ul></div>\n'
    )
    open(p,'w',encoding='utf-8').write(s+extra)
print('enriched')
