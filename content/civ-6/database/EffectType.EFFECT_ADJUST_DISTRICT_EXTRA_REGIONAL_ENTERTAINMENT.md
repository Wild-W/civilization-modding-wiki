---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_ENTERTAINMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_ENTERTAINMENT
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GREATPERSON_EXTRA_REGIONAL_BUILDING_ENTERTAINMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_ENTERTAINMENT",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_EXTRA_REGIONAL_ENTERTAINMENT",
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
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_ENTERTAINMENT",
		"Amount",
		1
	);
	
```

