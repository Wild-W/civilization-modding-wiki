---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_RANGED_VS_DISTRICT_PENALTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_RANGED_VS_DISTRICT_PENALTY
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`

## Samples

```SQL {title="GDR_SIEGE_LASER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_SIEGE_LASER",
		"MODIFIER_PLAYER_UNIT_IGNORE_RANGED_VS_DISTRICT_PENALTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_SIEGE_LASER",
		"Ignore",
		1
	);
	
```

