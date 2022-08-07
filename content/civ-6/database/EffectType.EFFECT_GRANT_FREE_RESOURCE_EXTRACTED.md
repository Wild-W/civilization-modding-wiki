---
tags:
- EffectType
title: EFFECT_GRANT_FREE_RESOURCE_EXTRACTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_RESOURCE_EXTRACTED
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples
```SQL {title="JEBELBARKAL_GRANT_FOUR_IRON_PER_TURN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"JEBELBARKAL_GRANT_FOUR_IRON_PER_TURN",
		"MODIFIER_SINGLE_CITY_ADJUST_FREE_RESOURCE_EXTRACTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"JEBELBARKAL_GRANT_FOUR_IRON_PER_TURN",
		"Amount",
		6
	),
	(
		"JEBELBARKAL_GRANT_FOUR_IRON_PER_TURN",
		"ResourceType",
		"RESOURCE_IRON"
	);
	
```

