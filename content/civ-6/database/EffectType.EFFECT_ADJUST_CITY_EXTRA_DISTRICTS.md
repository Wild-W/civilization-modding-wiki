---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_EXTRA_DISTRICTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_EXTRA_DISTRICTS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_EXTRA_DISTRICT_EACH_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_EXTRA_DISTRICT_EACH_CITY",
		"MODIFIER_PLAYER_CITIES_EXTRA_DISTRICT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EXTRA_DISTRICT_EACH_CITY",
		"Amount",
		1
	);
	
```

