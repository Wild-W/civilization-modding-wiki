---
tags:
- EffectType
title: EFFECT_ADJUST_MOST_ADVANCED_STRATEGIC_RESOURCE_COUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_MOST_ADVANCED_STRATEGIC_RESOURCE_COUNT
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOODY_MILITARY_ADJUST_STRATEGIC_RESOURCES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_MILITARY_ADJUST_STRATEGIC_RESOURCES",
		"MODIFIER_PLAYER_ADJUST_MOST_ADVANCED_STRATEGIC_RESOURCE_COUNT",
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
		"GOODY_MILITARY_ADJUST_STRATEGIC_RESOURCES",
		"Amount",
		"ScaleByGameSpeed",
		20
	);
	
```

