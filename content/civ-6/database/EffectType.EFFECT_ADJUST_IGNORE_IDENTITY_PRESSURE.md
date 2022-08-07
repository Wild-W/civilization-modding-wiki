---
tags:
- EffectType
title: EFFECT_ADJUST_IGNORE_IDENTITY_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IGNORE_IDENTITY_PRESSURE
>
> * Class: `Unknown`
> * Parameters:
>	* Ignore `Boolean`

## Samples
```SQL {title="GRAND_VIZIER_ADJUST_IGNORE_CULTURAL_IDENTITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GRAND_VIZIER_ADJUST_IGNORE_CULTURAL_IDENTITY",
		"MODIFIER_GOVERNOR_ADJUST_IGNORE_CULTURAL_IDENTITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GRAND_VIZIER_ADJUST_IGNORE_CULTURAL_IDENTITY",
		"Ignore",
		1
	);
	
```

