---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_RANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_RANGE
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GREATPERSON_EXTRA_REGIONAL_BUILDING_RANGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_RANGE",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_EXTRA_REGIONAL_RANGE",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_RANGE",
		"Amount",
		3
	);
	
```

