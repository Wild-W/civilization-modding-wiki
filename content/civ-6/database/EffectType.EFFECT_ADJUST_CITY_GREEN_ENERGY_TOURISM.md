---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_GREEN_ENERGY_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_GREEN_ENERGY_TOURISM
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="BIOSPHERE_GREEN_ENERGY_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BIOSPHERE_GREEN_ENERGY_TOURISM",
		"MODIFIER_PLAYER_CITIES_ADJUST_GREEN_ENERGY_TOURISM_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BIOSPHERE_GREEN_ENERGY_TOURISM",
		"Amount",
		100
	);
	
```

