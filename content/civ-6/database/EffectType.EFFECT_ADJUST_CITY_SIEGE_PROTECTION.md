---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_SIEGE_PROTECTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_SIEGE_PROTECTION
>
> * Class: `CITIES`
> * Parameters:
>	* Protected `Boolean`

## Samples

```SQL {title="DEFENSE_LOGISTICS_SIEGE_PROTECTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DEFENSE_LOGISTICS_SIEGE_PROTECTION",
		"MODIFIER_CITY_ADJUST_SIEGE_PROTECTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DEFENSE_LOGISTICS_SIEGE_PROTECTION",
		"Protected",
		1
	);
	
```

