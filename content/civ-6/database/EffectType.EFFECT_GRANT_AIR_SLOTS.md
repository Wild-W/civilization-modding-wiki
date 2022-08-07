---
tags:
- EffectType
title: EFFECT_GRANT_AIR_SLOTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_AIR_SLOTS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="FLIGHT_DECK_BONUS_AIRCRAFT_SLOT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FLIGHT_DECK_BONUS_AIRCRAFT_SLOT",
		"MODIFIER_PLAYER_UNIT_GRANT_AIR_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FLIGHT_DECK_BONUS_AIRCRAFT_SLOT",
		"Amount",
		1
	);
	
```

