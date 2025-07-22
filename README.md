# CalculadoraPaypal
App para calcular comisiones de paypal


# 💸 Calculadora de Comisión PayPal

Aplicación gráfica desarrollada en **Python con Tkinter**, diseñada para calcular fácilmente la comisión aplicada por PayPal en transacciones típicas. El programa permite calcular el monto neto recibido o determinar cuánto se debe enviar para obtener una cantidad específica libre de comisiones.

---

## 📦 Características

- Cálculo de comisión estándar: **5.4 % + 0.30 USD**
- Interfaz gráfica simple, clara y responsiva
- Modo dual:
  - Desde monto enviado → muestra comisión y neto recibido
  - Desde monto deseado → muestra cuánto se debe enviar y comisión estimada
- Validación en tiempo real del campo de entrada
- Compatible con Windows (.py o .exe con PyInstaller)
- Ícono personalizado incluido (`calc.ico`)

---

## 🧮 Fórmulas utilizadas

| Cálculo                       | Fórmula                                                  |
|------------------------------|-----------------------------------------------------------|
| Comisión                     | `monto * 0.054 + 0.30`                                   |
| Neto recibido                | `monto_bruto - comisión`                                 |
| Monto necesario para neto X  | `(monto_neto + 0.30) / (1 - 0.054)`                      |

---

## 🚀 Cómo ejecutar

### ✅ Desde Python (modo desarrollador)

1. Asegúrate de tener Python instalado (recomendado: 3.7+)
2. Coloca `calc.ico` en la misma carpeta que `calc.py`
3. Ejecuta:

```bash
python calc.py

📄 Licencia
Este software puede ser usado y modificado libremente para fines educativos y personales. No se ofrece garantía de exactitud en tarifas financieras.