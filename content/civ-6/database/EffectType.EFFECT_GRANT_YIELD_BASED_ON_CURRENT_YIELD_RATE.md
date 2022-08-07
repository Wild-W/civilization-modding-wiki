---
tags:
- EffectType
title: EFFECT_GRANT_YIELD_BASED_ON_CURRENT_YIELD_RATE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_YIELD_BASED_ON_CURRENT_YIELD_RATE
>
> * Class: `ANY`
> * Parameters:
>	* Multiplier `Integer`
>	* YieldToBaseOn `String`
>		* [Yields.YieldType]
>	* YieldToGrant `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_SCIENCE_RATE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_SCIENCE_RATE",
		"MODIFIER_PLAYER_GRANT_YIELD_BASED_ON_CURRENT_YIELD_RATE",
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
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_SCIENCE_RATE",
		"Multiplier",
		10
	),
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_SCIENCE_RATE",
		"YieldToBaseOn",
		"YIELD_SCIENCE"
	),
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_SCIENCE_RATE",
		"YieldToGrant",
		"YIELD_CULTURE"
	);
	
```

