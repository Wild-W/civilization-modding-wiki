---
tags:
- EffectType
title: EFFECT_GRANT_FREE_ENVOYS_HERE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_ENVOYS_HERE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="GREATPERSON_GAIN_THREE_ENVOYS_HERE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GAIN_THREE_ENVOYS_HERE",
		"MODIFIER_CITY_GRANT_FREE_ENVOYS_HERE",
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
		"GREATPERSON_GAIN_THREE_ENVOYS_HERE",
		"Amount",
		3
	);
	
```

