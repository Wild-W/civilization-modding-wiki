---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FRIENDLY_TERRITORY_COMBAT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FRIENDLY_TERRITORY_COMBAT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="FRIENDLY_TERRITORY_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FRIENDLY_TERRITORY_COMBAT",
		"MODIFIER_PLAYER_UNIT_ADJUST_FRIENDLY_TERRITORY_COMBAT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FRIENDLY_TERRITORY_COMBAT",
		"Amount",
		35
	);
	
```

