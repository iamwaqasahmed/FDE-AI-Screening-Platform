"""One router per mock system."""

from __future__ import annotations

from serve.routers import booking, letters, ophthalmology, registry, vendor

ROUTERS = {
    "registry": registry.router,
    "booking": booking.router,
    "letters": letters.router,
    "ophthalmology": ophthalmology.router,
    "vendor": vendor.router,
}
