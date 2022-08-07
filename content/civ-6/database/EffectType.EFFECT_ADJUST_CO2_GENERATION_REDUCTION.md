---
tags:
- EffectType
title: EFFECT_ADJUST_CO2_GENERATION_REDUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CO2_GENERATION_REDUCTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ResourceUsageType `String`
>		* RESOURCE_USAGE_UNIT

## Samples

```SQL {title="UNIT_CO2_REDUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNIT_CO2_REDUCTION",
		"MODIFIER_PLAYER_ADJUST_CO2_GENERATION_REDUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_CO2_REDUCTION",
		"Amount",
		50
	),
	(
		"UNIT_CO2_REDUCTION",
		"ResourceUsageType",
		"RESOURCE_USAGE_UNIT"
	);
	
```

