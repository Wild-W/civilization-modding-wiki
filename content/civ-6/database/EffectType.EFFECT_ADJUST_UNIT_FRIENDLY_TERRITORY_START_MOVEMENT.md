---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FRIENDLY_TERRITORY_START_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FRIENDLY_TERRITORY_START_MOVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="LOGISTICS_FRIENDLYTERRITORYMOVEMENTBONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LOGISTICS_FRIENDLYTERRITORYMOVEMENTBONUS",
		"MODIFIER_PLAYER_UNITS_ADJUST_FRIENDLY_TERRITORY_START_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LOGISTICS_FRIENDLYTERRITORYMOVEMENTBONUS",
		"Amount",
		1
	);
	
```

