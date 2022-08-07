---
tags:
- EffectType
title: EFFECT_GRANT_CITY_LOYALTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_CITY_LOYALTY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="PROJECT_COMPLETION_LOYALTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_LOYALTY",
		"MODIFIER_SINGLE_CITY_GRANT_LOYALTY",
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
		"PROJECT_COMPLETION_LOYALTY",
		"Amount",
		20
	);
	
```

