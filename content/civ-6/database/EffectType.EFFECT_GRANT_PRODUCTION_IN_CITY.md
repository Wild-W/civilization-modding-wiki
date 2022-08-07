---
tags:
- EffectType
title: EFFECT_GRANT_PRODUCTION_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PRODUCTION_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* KeepOverflow `Boolean`

## Samples
```SQL {title="GREATPERSON_GRANT_PRODUCTION_IN_CITY_MEDIEVAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GRANT_PRODUCTION_IN_CITY_MEDIEVAL",
		"MODIFIER_SINGLE_CITY_GRANT_PRODUCTION_IN_CITY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_GRANT_PRODUCTION_IN_CITY_MEDIEVAL",
		"Amount",
		"ScaleByGameSpeed",
		215
	),
	(
		"GREATPERSON_GRANT_PRODUCTION_IN_CITY_MEDIEVAL",
		"KeepOverflow",
		"ARGTYPE_IDENTITY",
		0
	);
	
```

