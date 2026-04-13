# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

"""Register e-invoice adapters on the shared ``omnexa_core`` IntegrationHub."""


def register_einvoice_adapters(hub):
	from omnexa_einvoice.einvoice_adapters import EgyptETAAdapter, SaudiZatcaAdapter

	hub.register(EgyptETAAdapter())
	hub.register(SaudiZatcaAdapter())
