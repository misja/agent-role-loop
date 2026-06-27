---
orphan: true
---

# Projectconventies voor het onderwijsmateriaal

Dit document bindt de conventies die gelden voor al het materiaal onder
`teaching/`. Het herhaalt die conventies niet; het wijst ze aan en legt vast dat
ze gelden, zodat de toepassing niet afhangt van wie een taak schrijft.

## Welke conventies gelden

Voor al het werk onder `teaching/` gelden:

- de schrijfwijzer (`teaching/schrijfwijzer.md`) voor register, terminologie en
  opmaak;
- de begrippenlijst (`teaching/begrippen.md`) voor de vaste termen.

## Scope

Deze conventies gelden uitsluitend voor `teaching/`. Niet-teaching-werk in deze
repository (`core/`, `adapters/`) valt er bewust buiten en houdt zijn eigen,
generieke en vendor-neutrale conventies. `core/` blijft taal-agnostisch en
Engelstalig.

## Hoe de conventie geborgd is

De afspraak is dat elk teaching-werkitem het volgende als vast acceptatiecriterium
opneemt:

> Voldoet aan de conventies in `teaching/conventies.md`.

Daarmee kan de gate niet groen zonder dat eraan getoetst is, ongeacht hoe het werk
wordt uitgevoerd. De teaching-werkitem-template (`teaching/_werkitem-template.md`)
heeft dit criterium al ingevuld. Een bouwende rol leest dit document daarnaast in
als onderdeel van de geldende projectconventies, zodat het materiaal er meteen aan
voldoet in plaats van achteraf. De generieke rol vraagt al om de geldende
conventies; dit document vult die voor teaching-werk concreet in.

## Een nieuwe conventie toevoegen

Komt er een conventie bij die voor `teaching/` moet gelden, voeg haar dan hier toe.
Dit document is de plek waar de gelding wordt vastgelegd; de inhoud van de conventie
hoort in haar eigen document.
