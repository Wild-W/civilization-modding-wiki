---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_FREE_POWER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_FREE_POWER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* SourceType `String`

## Samples

```SQL {title="HYDROELECTRIC_DAM_FREE_POWER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HYDROELECTRIC_DAM_FREE_POWER",
		"MODIFIER_SINGLE_CITY_ADJUST_FREE_POWER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HYDROELECTRIC_DAM_FREE_POWER",
		"Amount",
		6
	),
	(
		"HYDROELECTRIC_DAM_FREE_POWER",
		"SourceType",
		"FREE_POWER_SOURCE_WATER"
	);
	
```

