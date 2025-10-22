"""
Minimal dashboard for CodeWords Auto-Improvement project.

This module defines a simple dashboard using FastAPI. In the future, this could be replaced by a full web interface or React front-end.
"""

from fastapi import FastAPI
from .versioning import VersionManager

app = FastAPI()

@app.get("/dashboard")
def read_dashboard():
    """
    Returns basic information about the system, such as available versions.
    """
    vm = VersionManager()
    versions = vm.list_versions()
    return {
        "message": "CodeWords Dashboard",
        "versions": versions,
    }
