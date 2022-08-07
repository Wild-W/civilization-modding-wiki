---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_HOLY_CITIES_COMBAT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_HOLY_CITIES_COMBAT_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="BYZANTIUM_COMBAT_HOLY_CITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BYZANTIUM_COMBAT_HOLY_CITIES",
		"MODIFIER_PLAYER_UNIT_ADJUST_COMBAT_FOR_NUMBER_HOLY_CITIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BYZANTIUM_COMBAT_HOLY_CITIES",
		"Amount",
		3
	);
	
```

