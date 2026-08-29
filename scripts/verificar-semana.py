#!/usr/bin/env python3
"""Autograder del bootcamp: comprueba el estado real de tu proyecto de DaVinci Resolve.

Lee el `checks.json` de una semana y evalua cada comprobacion contra Resolve a traves
del puente HTTP local del servidor MCP (resolve-mcp). No modifica nada: solo lee.

Uso:
    python scripts/verificar-semana.py --doctor      # comprueba el entorno
    python scripts/verificar-semana.py 01            # todas las comprobaciones de la semana 01
    python scripts/verificar-semana.py 01 --check frame-rate
    python scripts/verificar-semana.py 01 --list     # solo lista los ids

Requisitos:
    - DaVinci Resolve 21 abierto, con tu proyecto del bootcamp cargado.
    - El puente cargado dentro de Resolve: Workspace > Scripts > Utility > resolve_bridge
    - Ejecutarlo con el interprete de Python que alcance 127.0.0.1 en la maquina donde
      corre Resolve. En WSL eso significa el Python de Windows, por ejemplo:
        "/mnt/c/Program Files/Python312/python.exe" scripts/verificar-semana.py --doctor
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
URL_POR_DEFECTO = "http://127.0.0.1:8777/rpc"
VERSION_ESPERADA = "21."

VERDE, ROJO, AMARILLO, GRIS, FIN = "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m"
if os.name == "nt" and not os.environ.get("WT_SESSION"):
    VERDE = ROJO = AMARILLO = GRIS = FIN = ""


class ErrorPuente(RuntimeError):
    """El puente no responde, o responde un error."""


# --------------------------------------------------------------------------- puente


def _leer_config() -> tuple[str, str]:
    """Devuelve (url, token). Las variables de entorno tienen precedencia."""
    url = os.environ.get("RESOLVE_BRIDGE_URL")
    ruta_token = os.environ.get("RESOLVE_BRIDGE_TOKEN_FILE")

    if not (url and ruta_token):
        candidatas = []
        if os.environ.get("RESOLVE_MCP_CONFIG"):
            candidatas.append(pathlib.Path(os.environ["RESOLVE_MCP_CONFIG"]))
        if os.environ.get("LOCALAPPDATA"):
            candidatas.append(pathlib.Path(os.environ["LOCALAPPDATA"]) / "resolve-mcp" / "config.json")
        candidatas.append(pathlib.Path.home() / ".config" / "resolve-mcp" / "config.json")
        for c in candidatas:
            if c.is_file():
                cfg = json.loads(c.read_text(encoding="utf-8"))
                url = url or cfg.get("bridge_url")
                ruta_token = ruta_token or cfg.get("token_file")
                break

    url = url or URL_POR_DEFECTO
    if not ruta_token:
        base = os.environ.get("LOCALAPPDATA") or str(pathlib.Path.home() / ".local" / "share")
        ruta_token = str(pathlib.Path(base) / "resolve-mcp" / "bridge_token")

    p = pathlib.Path(ruta_token)
    if not p.is_file():
        raise ErrorPuente(
            f"No encuentro el token del puente en {p}.\n"
            "Arranca el puente dentro de Resolve: Workspace > Scripts > Utility > resolve_bridge,\n"
            "o exporta RESOLVE_BRIDGE_TOKEN_FILE con la ruta correcta."
        )
    return url, p.read_text(encoding="utf-8").strip()


def rpc(op: str, args: dict | None = None, timeout: int = 30) -> dict:
    """Llama una operacion del puente y devuelve su `result`."""
    url, token = _leer_config()
    cuerpo = {"op": op}
    cuerpo.update(args or {})
    req = urllib.request.Request(
        url,
        data=json.dumps(cuerpo).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
    )
    try:
        respuesta = json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise ErrorPuente(
            f"No puedo hablar con el puente en {url}: {exc}\n"
            "Comprueba que Resolve esta abierto y que ejecutas este script con el Python\n"
            "de la maquina donde corre Resolve (en WSL, el Python de Windows)."
        ) from exc
    if not respuesta.get("ok"):
        raise ErrorPuente(f"El puente rechazo la operacion '{op}': {respuesta.get('error')}")
    return respuesta.get("result") or {}


# --------------------------------------------------------------------------- checks


def evaluar(expresion: str, resultado: dict) -> bool:
    """Evalua la expresion de un check con `r` ligado al resultado de la operacion.

    ponytail: `eval` sobre un literal del propio repo, no sobre entrada del usuario.
    Si algun dia los checks vinieran de fuera, esto necesita un parser de verdad.
    """
    entorno = {"__builtins__": {"len": len, "any": any, "all": all, "sorted": sorted,
                                "int": int, "float": float, "str": str, "abs": abs}}
    return bool(eval(expresion, entorno, {"r": resultado}))  # noqa: S307


def carpeta_semana(numero: str) -> pathlib.Path:
    coincidencias = sorted((RAIZ / "bootcamp").glob(f"week-{numero}-*"))
    if not coincidencias:
        raise SystemExit(f"{ROJO}No existe la semana {numero} en bootcamp/{FIN}")
    return coincidencias[0]


def cargar_checks(numero: str) -> dict:
    ruta = carpeta_semana(numero) / "checks.json"
    if not ruta.is_file():
        raise SystemExit(f"{ROJO}La semana {numero} todavia no tiene checks.json{FIN}")
    return json.loads(ruta.read_text(encoding="utf-8"))


def correr_semana(numero: str, solo: str | None, listar: bool) -> int:
    datos = cargar_checks(numero)
    checks = datos.get("checks", [])
    if solo:
        checks = [c for c in checks if c["id"] == solo]
        if not checks:
            raise SystemExit(f"{ROJO}No hay ningun check con id '{solo}' en la semana {numero}{FIN}")

    print(f"\n{GRIS}Semana {datos.get('semana', numero)} — {datos.get('titulo', '')}{FIN}\n")

    if listar:
        for c in checks:
            print(f"  {c['id']:<28} {c['descripcion']}")
        return 0

    fallos = 0
    for c in checks:
        try:
            resultado = rpc(c["op"], c.get("args"))
            ok = evaluar(c["expr"], resultado)
        except ErrorPuente as exc:
            print(f"  {AMARILLO}!{FIN} {c['descripcion']}\n    {GRIS}{exc}{FIN}")
            fallos += 1
            continue
        except Exception as exc:  # expresion mal escrita o forma inesperada
            print(f"  {AMARILLO}!{FIN} {c['descripcion']}\n    {GRIS}check '{c['id']}' roto: {exc}{FIN}")
            fallos += 1
            continue

        if ok:
            print(f"  {VERDE}OK{FIN}  {c['descripcion']}")
        else:
            fallos += 1
            print(f"  {ROJO}KO{FIN}  {c['descripcion']}")
            print(f"      {GRIS}{c['pista']}{FIN}")

    total = len(checks)
    print()
    if fallos:
        print(f"{ROJO}{fallos} de {total} comprobaciones sin superar.{FIN}\n")
        return 1
    print(f"{VERDE}Las {total} comprobaciones pasan.{FIN}\n")
    return 0


# --------------------------------------------------------------------------- doctor


def doctor() -> int:
    problemas = 0

    def linea(ok: bool, texto: str, pista: str = "") -> None:
        nonlocal problemas
        print(f"  {VERDE}OK{FIN}  {texto}" if ok else f"  {ROJO}KO{FIN}  {texto}")
        if not ok:
            problemas += 1
            if pista:
                print(f"      {GRIS}{pista}{FIN}")

    print(f"\n{GRIS}Comprobando el entorno del bootcamp{FIN}\n")

    try:
        estado = rpc("ping", timeout=10)
    except ErrorPuente as exc:
        print(f"  {ROJO}KO{FIN}  El puente de Resolve no responde")
        print(f"      {GRIS}{exc}{FIN}\n")
        return 1

    linea(True, f"Puente vivo (version {estado.get('bridge_version', '?')})")

    version = str(estado.get("resolve_version", ""))
    linea(
        version.startswith(VERSION_ESPERADA),
        f"DaVinci Resolve {version or 'desconocido'}",
        "Este bootcamp se escribio contra Resolve 21. Con otra version, menus y ajustes cambian de sitio.",
    )
    linea(
        estado.get("api_health") == "ok",
        "La API de scripting responde",
        "Reinicia Resolve y vuelve a lanzar el puente desde Workspace > Scripts > Utility.",
    )

    proyecto = estado.get("project")
    linea(bool(proyecto), f"Proyecto abierto: {proyecto or 'ninguno'}",
         "Abre tu proyecto del bootcamp antes de verificar una semana.")

    aviso = (estado.get("bridge_check") or {}).get("status")
    if aviso and aviso != "OK":
        print(f"  {AMARILLO}!{FIN}  El puente esta desincronizado con el servidor MCP")
        print(f"      {GRIS}{(estado.get('bridge_check') or {}).get('action', '')}{FIN}")

    raiz_medios = os.environ.get("BC_MEDIOS")
    if raiz_medios:
        linea(pathlib.Path(raiz_medios).is_dir(), f"Pack de medios en {raiz_medios}",
             "Revisa docs/pack-de-medios.md y descarga el pack antes de las practicas.")
    else:
        print(f"  {AMARILLO}!{FIN}  Variable BC_MEDIOS sin definir (opcional)")
        print(f"      {GRIS}Apuntala a tu carpeta del pack de medios para que el doctor la compruebe.{FIN}")

    print()
    if problemas:
        print(f"{ROJO}{problemas} problema(s) que arreglar antes de seguir.{FIN}\n")
        return 1
    print(f"{VERDE}Entorno listo.{FIN}\n")
    return 0


# --------------------------------------------------------------------------- cli


def main() -> int:
    p = argparse.ArgumentParser(description="Autograder del bootcamp DaVinci Resolve 21.")
    p.add_argument("semana", nargs="?", help="numero de semana con dos digitos, p.ej. 01")
    p.add_argument("--doctor", action="store_true", help="comprueba el entorno y sale")
    p.add_argument("--check", metavar="ID", help="ejecuta solo la comprobacion con ese id")
    p.add_argument("--list", action="store_true", help="lista las comprobaciones sin ejecutarlas")
    args = p.parse_args()

    if args.doctor:
        return doctor()
    if not args.semana:
        p.print_help()
        return 2
    return correr_semana(args.semana.zfill(2), args.check, args.list)


if __name__ == "__main__":
    sys.exit(main())
