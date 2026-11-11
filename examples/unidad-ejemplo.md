# Ejemplo de unidad (mini)

## Unidad 2. Autenticación y autorización (JWT, RBAC)
**Contexto:** Distinguir identidad, sesión y permisos permite diseñar APIs seguras y mantenibles en aplicaciones multi-tenant.

### Ejercicio 1. Completa con el término correcto.
*Completa con: autenticación, autorización, RBAC, multi-tenant, refresh token, 2FA/TOTP.*
a) ____________: verificar quién es el usuario.  
b) ____________: determinar qué puede hacer.  
c) ____________: modelo donde un mismo despliegue sirve a varios clientes aislados.  

### Ejercicio 2. Corrige los errores (algunas pueden ser correctas).
a) Guardo el access token en `localStorage` sin considerar XSS. → __________________  
b) El servidor valida la firma del JWT antes de confiar en sus claims. → __________________  
c) Uso el mismo secreto JWT en desarrollo y producción. → __________________  

### Ejercicio 3. Elige la opción correcta.
a) Para rotar sesión sin re-login frecuente uso (access token corto + refresh / solo access largo).  
b) Un endpoint `DELETE /users/:id` debe comprobar (solo autenticación / autenticación y permisos sobre el recurso).  

## Solucionario (ejemplo)
- Ej 1: a) autenticación b) autorización c) multi-tenant
- Ej 2: a) Riesgo: preferir cookie `httpOnly`/mitigar XSS b) Correcta c) Error: secretos distintos por entorno
- Ej 3: a) access token corto + refresh b) autenticación y permisos sobre el recurso
