---
name: sin-ventanas-terminal
description: "REGLA FIJA de Edu — ejecutar SIEMPRE los comandos dentro de VS Code (Bash/PowerShell de Claude, en segundo plano si son largos); nunca abrirle ventanas de terminal"
metadata:
  node_type: memory
  type: feedback
  originSessionId: db3362aa-899c-4a4e-add4-74b1773822e0
  modified: 2026-11-02T20:31:34.420Z
---

**Siempre** ejecutar los comandos desde VS Code con las herramientas de Claude (Bash/PowerShell); los largos o que
se quedan corriendo (p. ej. `shopify theme dev`, servidores, esperas) con `run_in_background` y vigilarlos con su
log o con `curl`. **Nunca** `Start-Process powershell`, `cmd /c start` ni nada que abra una ventana nueva de terminal.
Los navegadores para capturas, en modo headless y oculto (`-WindowStyle Hidden`).

**Why:** Edu lo pidió el 10-oct-2026 («lanza los comandos en el visual studio, no me abras una terminal») y lo
confirmó como regla permanente: «ejecuta siempre así, memorízalo».

**How to apply:** en todo comando de cualquier tarea. Si algo exige de verdad interacción humana (login en el
navegador de Shopify CLI o GitHub, una contraseña nueva), avisar antes en el chat y buscar primero la variante no
interactiva (flags como `--store-password`, ficheros en `.claude/`). Ver [[lunerie-vista-previa]].

**Lo que funcionó (2-nov):** un menú interactivo o un «press any key» se maneja con una consola invisible
(`pywinpty`, ya instalado): `tema/login_cli.py` hace el login de Shopify CLI así y solo se abre el navegador. Si la
CLI de temas falla, `tema/subir_api.py` sube los ficheros por la Admin API sin login.
